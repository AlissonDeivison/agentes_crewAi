from crewai import Agent
from app.tools.graphTool import GraphTool

geradorDeGraficosConfig = {
    "role":"Criador de Gráficos",
    "goal":"""Gerar um gráfico de pizza visual com base nos dados de matriz energética fornecidos.""",
    "backstory":"""Você é um especialista em visualização de dados e transforma dados númericos em gráficos claros e informativos.""",
    "tools":[GraphTool()],
    "allow_delegations":False,
    "verbose":True,
    "llm":"gpt-4o-mini"
}

agenteGeradorDeGraficos = Agent(config=geradorDeGraficosConfig)