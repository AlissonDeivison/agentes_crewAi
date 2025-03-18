from crewai import Task
from agents.agenteDeTopicos import agenteDeTopicos

tarefaGerarTopicos = Task(
    description=(
        "Com base no documento fornecido pelo Agente Pesquisador, gerar uma sequência lógica de tópicos principais "
        "para um conteúdo educacional. A estrutura deve seguir a progressão: introdução, desenvolvimento e conclusão. "
        "Os tópicos devem ser claros, objetivos e organizados para facilitar o desenvolvimento posterior pelo Agente de Conteúdo. "
        "Ao final da sequência, incluir uma atividade prática para reforçar o aprendizado do usuário."
    ),
    expected_output=(
        "Uma lista numerada contendo tópicos principais organizados logicamente, sem explicações adicionais ou subtópicos. "
        "A estrutura deve conter uma introdução, desenvolvimento e conclusão, finalizando com uma atividade prática "
        "para aplicação ou reflexão do conteúdo."
    ),
    agent=agenteDeTopicos
)