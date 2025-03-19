import random
from crewai.flow.flow import Flow, listen, start, router
from pydantic import BaseModel


class EstadoExemplo(BaseModel):
    indicador_sucesso:bool = False
    
class FluxoRoteado(Flow[EstadoExemplo]):
    
    @start
    def metodo_inicial(self):
        print("Iniciando o fluxo")
        self.state.indicador_sucesso = random.choice([True, False])
    
    @router
    def segundo_metodo(self):
        if self.state.indicador_sucesso:
            return 'Sucesso'
        else:
            return 'Falha'
    
    @listen('Sucesso')
    def metodo_sucesso(self):
        print("O método de sucesso foi chamado")
        
    @listen('Falha')
    def metodo_falha(self):
        print("O método de falha foi chamado")
        
fluxo = FluxoRoteado()
fluxo.kickoff()