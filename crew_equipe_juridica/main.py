from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool

reader_tool = FileReadTool()
gpt_mini = 'gpt-4o-mini'
gpt_4o = 'gpt-4o'

# Configuração dos agentes

leitor_yaml_config = {
    "role": "Leitor de dados",
    "goal": """Ler os dados do arquivo {yaml} de uma petição. Esses dados servirão de apoio para o escritor redigir a petição apropriadament e com os dados corretos. Crie uma lista de seções que devem ser usadas na petição e passe para o escritor.""",
    "verbose": True,
    "memory": True,
    "backstory": """Você é um especialista em leitura e interpretação de dados legais, com vasta experiencia em processar informações de documentos legais.""",
    "tools": [reader_tool],
    "allow_delegation": False,
    "llm": gpt_mini
}

escritor_config = {
    "role": "Escritor de petições",
    "backstory": """Você é um advogado altamente qualificado e experiente na elaboração de peças jurídicas precisas e persuasivas. É reconhecido por sua capacidade de articular argumentos convicentes que evidenciam os méritos de cada caso, garantindo que os interesses de seus clientes sejam representados de forma eficaz e justa. Você tem a grande habilidade de transformar dados brutos em belíssimas peças jurídicas.""",
    "goal": """Você receberá os dados do agente leitor de YAML, que devem ser usados como insumo para a escrita de uma nova petição. Todos os dados do YAML devem estar no texto. Não deixe faltar nenhuma informação proveninente do YAML na petição. Os textos de todas as informações das seções, como partes, fatos, fundamentação jurídica, pediro, provas ou qualquer outra seção que venha do YAML, devem conter o título da seção e o texto da seção deve ser escrito em parágrafos corridos, sem pontos (1. 2. 3.) ou listas.""",
    "verbose": True,
    "memory": True,
    "llm": gpt_4o,
    "allow_delegation": False,
}

revisor_config = {
    "role": "Revisor de petições",
    "backstory": """Você é um revisor meticuloso com um olhar aguçado para detalhes, garantindo que cada petição esteja livre de erros e bem formulada""",
    "goal": """Você revisará a petição escrita para garantir precisão e clareza. Estando tudo correto, salve todo o texto previsado da petição.""",
    "verbose": True,
    "memory": True,
    "llm": gpt_mini,
    "allow_delegation": False,
}

# Criação dos agentes
leitor_yaml = Agent(config=leitor_yaml_config)
escritor_de_peticoes = Agent(config=escritor_config)
revisor_de_peticoes = Agent(config=revisor_config)

# Configuração das tarefas
tarefa_leitura_config = {
    "description": "Use a ferramenta de leitura para ler o arquivo {yaml} e extrair os dados necessários para a petição.",
    "expected_output": "Dados estruturados da petição prontos para uso.",
    "agent": leitor_yaml,
}

escrever_peticao_config = {
    "description": """Escreva em Markdown uma petição baseada nos dados do YAML. Crie uma estutura de petição de acordo com os dados fornecidos.""",
    "expected_output": "Uma petição bem escrita e estrutura em Markdown.",
    "agent": escritor_de_peticoes,
}

revisar_peticao_config = {
    "description": """Revise a petição escrita em Markdown para garantir precisão e clareza. Estando tudo correto salve todo o texto revisado da perição. Retire o '''markdonw.'''""",
    "expected_output": """Um arquivo de texto em Markdown com a petição revisada e pronta para ser submetida. É muito importante que o texto não contenha coisas como " ''' markdown ''' " e " ''' ". """,
    "agent": revisor_de_peticoes,
    "output_file": "./Equipe Juridica/peticao.md"
}

# Criação das tarefas
tarefa_leitura = Task(config=tarefa_leitura_config)
escrever_peticao = Task(config=escrever_peticao_config)
revisar_peticao = Task(config=revisar_peticao_config)

# Criação da Crew
crew = Crew(
    agents = [leitor_yaml, escritor_de_peticoes, revisor_de_peticoes],
    tasks = [tarefa_leitura, escrever_peticao, revisar_peticao],
    process = Process.sequential,
    memory = True,
    cache = True
)

input = {'yaml': './dados.yaml'}
result = crew.kickoff(inputs=input)