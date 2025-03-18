from dotenv import load_dotenv
from crewai.flow.flow import Flow, listen, start

load_dotenv()


class FluxoNaoEstruturado(Flow):

    @start()
    def etapa_inicial(self):
        # info é um estado qualquer criado para armazenas uma informação ao longo do fluxo
        self.state['info'] = "Vamos falar sobre: " + self.state["tema"]
        self.state['info'] += "\nInformação gerada pela PRIMEIRA Crew"
        self.state['estapas_concluidas'] = 1

    @listen(etapa_inicial)
    def etapa_intermediaria(self):
        self.state['info'] += "\nInformação gerada pela SEGUNDA Crew"
        self.state['estapas_concluidas'] += 1

    @listen(etapa_intermediaria)
    def etapa_final(self):
        self.state['info'] += "\nInformação gerada pela TERCEIRA Crew"
        self.state['estapas_concluidas'] += 1
        # return self.state['info'], self.state['estapas_concluidas']
        return self.state



processo = FluxoNaoEstruturado()
state = processo.kickoff(inputs={"tema": "Fluxo Não Estruturado com CrewAI"})
print(f"Estado do processo final:\n{state['info']}")


processo.plot("c:/Users/005255/Documents/Projetos/agentes_crewAi/fluxo_nao_estruturado/fluxo")