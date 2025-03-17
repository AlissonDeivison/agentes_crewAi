from crewai import Agent
from crewai_tools import SerperDevTool


serper_tool = SerperDevTool()
serper_tool.n_results = 50

pesquisadorConfig = {
    "role":"Pesquisador de Matriz Energética",
    "goal":"""Pesquisar a previsão de consumo energético global por tipo de fonte para o ano de 2025, incluindo porcentagens de uso para as seguintes fontes: Petróleto e derivados, Carvão, Gás natural, Hidráulicam Nuclear, Biomassa e outras renováveis.""",
    "backstory":"""Especialista em pesquisa de dados energéticos e fontes de energia sustentáveis.""",
    "tools":[serper_tool],
    "allow_delegations":False,
    "verbose":True,
    "llm":"gpt-4o"
}

agenteDePesquisa = Agent(config=pesquisadorConfig)

