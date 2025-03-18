from crewai import Agent
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv ()
search_tool = SerperDevTool ()

gpt_4o = 'gpt-4o'

agentePesquisador = Agent(
    role='Pesquisador de Tema',
    goal='Pesquisar informações detalhadas sobre {tema} na internet',
    backstory=(
        "Você é um especialista em pesquisa, com habilidades aguçadas para "
        "encontrar informações valiosas e detalhadas na internet."
    ),
    verbose=True,
    memory=True,
    tools=[search_tool],
    llm=gpt_4o
)