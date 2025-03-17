from crewai import Task
from crewai_tools import SerperDevTool
from app.agents.agenteDePesquisa import agenteDePesquisa

from crewai_tools import SerperDevTool


serper_tool = SerperDevTool()
serper_tool.n_results = 10

pesquisaEnergeticaTaskConfig = {
    "description": """User o SerperDevTool para pesquisar a previsão de consumo energético global por tipo de fonte para o ano de 2025. As fontes de energia devem incluir: Petróleo e derivados, Carvão, Gás natural, Hidráulica, Nuclear, Biomassa e outras renováveis (Incluíndo solar, eólica e geotérmica). As pesquisas na web devem ser feitas em fontes renomadas e retornar porcentagens para cada tipo de fonte.""",
    "expected_output": """Um dicionário com as porcentagens de consumo energético previstas para cada fonte em 2025:

    {
        "Petróleo e derivados": <valor>%,
        "Carvão": <valor>%,
        "Gás natural": <valor>%,
        "Hidráulica": <valor>%,
        "Nuclear": <valor>%,
        "Biomassa": <valor>%,
        "Outras renováveis": <valor>%
    }
    """,
    "tools":[serper_tool],
    "agent":agenteDePesquisa
}

pesquisaEnergeticaTask = Task(config=pesquisaEnergeticaTaskConfig)
