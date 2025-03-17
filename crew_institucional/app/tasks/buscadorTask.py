from crewai import Task
from app.agents.buscadorAgent import buscador
from app.tools.buscadorTool import scrapeTool, pesquisaTool
from random import randint

buscadorTaskConfiguraton = {
    "description": "Use ferramentas de pesquisa na web para localizar fontes confiáveis da Unifacisa sobre {input_pergunta}, não faça a leitura de arquivos PDF. Depois, acesse o site da Unifacisa {site_url}para validar se a informação encontrada é real. A busca no site deve começar na página inicial e seguir links internos dentro do domínio. A resposta final deve ser baseada na confirmação das duas fontes. Sempre inclua a fonte exata (URL correta) junto da informação.",
    "expected_output": "Retornar informações confirmadas sobre {input_pergunta}, com base na pesquisa na web e validação no site {site_url}, formatadas em Markdown e sempre com links para as fontes.",
    "agent": buscador,
    "verbose": True,
    "tools": [pesquisaTool, scrapeTool],
    "output_file": f"./data/partial_output{randint(1, 100)}.md"
}


buscadorTask = Task(config=buscadorTaskConfiguraton)