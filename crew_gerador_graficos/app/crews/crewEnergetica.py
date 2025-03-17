from crewai import Crew, Process
from app.tasks.pesquisaEnergeticaTask import pesquisaEnergeticaTask
from app.tasks.geradorDeGraficosTask import geradorDeGraficosTask
from app.agents.agenteDePesquisa import agenteDePesquisa
from app.agents.agenteGeradorDeGraficos import agenteGeradorDeGraficos

crewEnergetica = Crew(
    agents=[agenteDePesquisa, agenteGeradorDeGraficos],
    tasks=[pesquisaEnergeticaTask, geradorDeGraficosTask],
    process=Process.sequential,
)