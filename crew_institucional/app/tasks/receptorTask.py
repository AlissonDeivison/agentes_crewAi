from crewai import Task
from app.agents.receptorAgent import receptor

receptorTaskConfiguraton = {
    "description":"Receber mensagens de usuários no WhatsApp e encaminhá-las para o agente de classificação.",
    "expected_output":"Mensagem encaminhada para o agente de classificação.",
    "agent":receptor
}

receptorTask = Task(config=receptorTaskConfiguraton)