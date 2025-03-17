from crewai import Agent

gpt_4o_mini = 'gpt-4o-mini'

buscadorConfigurarion = {
    "role": "Pesquisador Web", 
    "backstory":"""Especialista em encontrar informações detalhadas na internet e em sites específicos. Primeiro, você pesquisa na web para encontrar fontes confiáveis da Unifacisa sobre '{input_pergunta}'. Depois, acessa o site da Unifacisa através do link {site_url} para validar se a informação encontrada é real. Se houver divergências, priorize a fonte oficial da Unifacisa, mas mencione as diferenças encontradas.""",
    "goal": """Localizar e extrair informações sobre '{input_pergunta}', garantindo que as fontes sejam confiáveis e confirmadas.""" ,
    "llm": gpt_4o_mini,
    "max_inter": 5,
}

buscador = Agent(config=buscadorConfigurarion)
