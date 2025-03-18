from dotenv import load_dotenv
from crewai.flow.flow import Flow, listen, start, and_
from pydantic import BaseModel

load_dotenv()

# Definindo o estado estruturado com Pydantic
class State(BaseModel):
    tema: str = 'IA na Saúde'  # Tema principal do fluxo
    info: str = ''  # Informações geradas ao longo do fluxo
    etapas_concluidas: int = 0  # Contador de etapas concluídas
    validacao: str = ''  # Registro de validações

# Definindo o fluxo com condição AND
class FlowWithAND(Flow[State]):
    state_class = State  # Associando o estado estruturado ao fluxo

    @start()
    def etapa_inicial(self):
        # Inicializando as variáveis de estado
        self.state.info = f'Vamos falar sobre: {self.state.tema}'
        self.state.info += '\nInformação gerada pela PRIMEIRA Crew'
        self.state.etapas_concluidas = 1

    @listen(etapa_inicial)
    def validar_dados_1(self):
        self.state.validacao += 'Validação 1 concluída.\n'

    @listen(etapa_inicial)
    def validar_dados_2(self):
        self.state.validacao += 'Validação 2 concluída.\n'

    @listen(and_(validar_dados_1, validar_dados_2))
    def consolidar_validacao(self):
        self.state.info += '\nTodas as validações foram concluídas.'
        self.state.etapas_concluidas += 1

    @listen(consolidar_validacao)
    def etapa_final(self):
        self.state.info += '\nInformação gerada pela etapa final.'
        self.state.etapas_concluidas += 1
        return self.state

# Inicializando o fluxo com condição AND
processo = FlowWithAND()
state = processo.kickoff()

print(f"Estado final:\n{state.info}")
print(f"Validações realizadas:\n{state.validacao}")

# Especificar o caminho onde o plot será salvo
plot_path = './fluxo_estruturado/plot'

# Gerar e salvar o gráfico do fluxo
processo.plot(plot_path)
