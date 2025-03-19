from crewai.flow.flow import Flow, listen, start, router

from fluxo_reflexion.crews.crew_analise.crew_analise import CrewDeAnalise
from fluxo_reflexion.crews.crew_pesquisa.crew_pesquisa import CrewDePesquisa

from pydantic import BaseModel


class ReflexionState(BaseModel):
    """Estado de Reflexão"""
    ideia: str = ""
    topicos: str = ""
    critica: str = ""
    tentativas: int = 0


class FluxoReflexion(Flow[ReflexionState]):
    
    @start
    def inicio(self):
        print(f"Iniciando o fluxo de reflexão com os tópicos: {self.state.topicos}")
        self.state.ideias = ""
        self.state.critica = ""
        self.state.tentativas = 0
        
    @listen("inicio")
    def pesquisador(self):
        print("Pesquisador: Vamos começar a pesquisa!")
        crew_pesquisa = CrewDePesquisa()
        ideia = crew_pesquisa.kickoff(
            topicos=self.state.topicos,
            ideia=self.state.ideias,
            critica=self.state.critica,
        )
        self.state.ideias = ideia
    
    @router(pesquisador)
    def critico(self):
        print("Crítico: Vamos analisar as ideias!")
        crew_analise = CrewDeAnalise()
        critica = crew_analise.kickoff(
            topicos=self.state.topicos,
            ideia=self.state.ideias,
            critica=self.state.critica,
            objetivo="Melhorar para um contexto acadêmico",
        )
        self.state.critica = critica
        self.state.tentativas += 1
        
        if self.state.tentativas > 3 or 'perfeito' in self.state.critica.lower():
            return "concluido"
        else:
            return "inicio"
        
    @listen("concluido")
    def final(self):
        print(f"Finalizando o fluxo de reflexão com as ideias: {self.state.ideias} e críticas: {self.state.critica}")
        print("Reflexão concluída!")
        
reflexao = FluxoReflexion()
ret = reflexao.kickoff(inputs={"ideia":"IA generativa na Saúde"})