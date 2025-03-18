from crewai import Agent, Task, Crew
from crewai.tools import tool
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests

load_dotenv()
ultima_consulta = None
gpt_4o = 'gpt-4o'

@tool
def ferramenta_cotacao_dolar() -> str:
    """Consulta a cotação do dólar em relação ao real (USD-BRL)."""
    url_cotacao = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    
    resposta = requests.get(url_cotacao)
    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao_dolar = dados["USDBRL"]["bid"]
        return f"A cotação do dólar em relação ao real é de R$ {cotacao_dolar}."
    else:
        return "Erro ao consultar a cotação do dólar."
    
def funcao_cache(argumentos, resultado):
    global ultima_consulta
    agora = datetime.now()

    if ultima_consulta and (agora - ultima_consulta) < timedelta(minutes=1):
        return True
    ultima_consulta = agora
    return False

ferramenta_cotacao_dolar.cache_function = funcao_cache

exchange_agent = Agent (
    role = "Agente de Câmbio",
    goal = "Monitorar a cotação do dólar em relação ao real.",
    backstory="""Você é responsável por consultar e reportar a cotação atual do dolar em relação ao real.""",
    tools = [ferramenta_cotacao_dolar],
    allow_delegation=False,
    llm=gpt_4o
)


exchange_agent_task = Task (
    description="Consultar a cotação do dólar em relação ao real e reportar o resultado.",
    expected_output="Um texto contendo a cotação do dólar em relação ao real.",
    agent=exchange_agent,
)

crew = Crew(
    agents=[exchange_agent],
    tasks=[exchange_agent_task],
)

resposta = crew.kickoff(inputs={})

print(resposta)