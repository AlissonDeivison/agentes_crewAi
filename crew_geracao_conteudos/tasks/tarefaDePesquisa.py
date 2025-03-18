from crewai import Task
from agents.agentePesquisador import agentePesquisador
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv ()
search_tool = SerperDevTool ()

gpt_4o = 'gpt-4o'

tarefaDePesquisa = Task(
    description=(
        "Pesquisar informações detalhadas e relevantes sobre o tema: {tema}. "
        "Concentre-se em aspectos únicos e dados importantes que podem enriquecer o {conteudo}. "
        "Todo o texto deve estar em Português Brasil."
    ),
    expected_output='Um documento com as principais informações e dados sobre {tema}.',
    tools=[search_tool],
    agent=agentePesquisador
)