from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class State(BaseModel):
    tema: str = "IA na Saúde" # Tema principal do fluxo
    info: str = "" #Informações geradas ao longo do fluxo
    etapas_concluidas: int = 0 # Número de etapas concluídas
    
class FluxoEstruturado(Flow[State]):
    state_class = State # Classe que define o estado do fluxo
    
    @start()
    def etapa_inicial(self):
        #O estado já garante que as variáveis estáo previamente definidas
        self.state.info = f"Vamos falar sobre {self.state.tema}"
        self.state.info += "\nInformação gerada pela PRIMEIRA Crew"
        self.state.etapas_concluidas += 1
    
    @listen(etapa_inicial)
    def etapa_intermedia(self):
        self.state.info += "\nInformação gerada pela SEGUNDA Crew"
        self.state.etapas_concluidas += 1
    
    @listen(etapa_intermedia)
    def estapa_final(self):
        self.state.info += "\nInformação gerada pela TERCEIRA Crew"
        self.state.etapas_concluidas += 1
        return self.state
    
processo = FluxoEstruturado()
estado = processo.kickoff()

print(f"Estado final: {estado.info}")
processo.plot("c:/Users/005255/Documents/Projetos/agentes_crewAi/fluxo_estruturado/fluxo")