from crewai import Crew, Process
from agents.agenteDeAutomacaoEmail import agenteEnvioEmail
from agents.agenteDeConteuto import agenteDeConteudo
from agents.agenteDeTopicos import agenteDeTopicos
from agents.agentePesquisador import agentePesquisador
from agents.agenteRevisor import agenteRevisor

from tasks.tarefaCriacaoDeConteudo import tarefaCriacaoDeConteudo
from tasks.tarefaDePesquisa import tarefaDePesquisa
from tasks.tarefaDeTopicos import tarefaGerarTopicos
from tasks.tarefaEnviarEmail import tarefaEnviarEmail
from tasks.tarefaRevisarConteudo import tarefaRevisarConteudo

crew = Crew(
    agents=[agenteDeConteudo, agenteDeTopicos, agentePesquisador, agenteRevisor, agenteEnvioEmail],
    tasks=[tarefaGerarTopicos, tarefaDePesquisa, tarefaCriacaoDeConteudo, tarefaRevisarConteudo, tarefaEnviarEmail],
    process=Process.sequential,
    verbose=True
)