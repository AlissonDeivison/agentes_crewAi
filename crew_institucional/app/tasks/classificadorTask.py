from crewai import Task
from app.agents.classificadorAgent import classificador

classificadorTaskConfiguraton = {
    "description": "Classificar mensagens recebidas do WhatsApp através da mensagem recebida: '{input_pergunta}'.",
    "expected_output": "Retornar a classificação da mensagem obtida na função de callback.",
    "agent": classificador,
    "verbose": True
}

classificadorTask = Task(config=classificadorTaskConfiguraton)
