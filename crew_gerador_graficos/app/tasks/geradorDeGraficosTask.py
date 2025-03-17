from crewai import Task
from app.tools.graphTool import GraphTool
from app.tasks.pesquisaEnergeticaTask import pesquisaEnergeticaTask
from app.agents.agenteDePesquisa import agenteDePesquisa

geradorDeGraficosConfig = {
    "description":"""Utilize os dados de consumo energético previstos para 2025 para criar um gráfico de barra que ilustre a distribuição percentual de cada tipo de fonte de energia: Petróleo e derivados, Carvão, Gás natural, Hidraúlica, Nuclear, Biomassa e outras renováveis.""",
    "expected_output":"Um gráfico de pizza salvo como arquivo PNG que mostra a distribuição percentual da matriz energética global prevista para 2025.",
    "tools":[GraphTool()],
    "context":[ pesquisaEnergeticaTask ],
    "agent": agenteDePesquisa
}

geradorDeGraficosTask = Task(config=geradorDeGraficosConfig)