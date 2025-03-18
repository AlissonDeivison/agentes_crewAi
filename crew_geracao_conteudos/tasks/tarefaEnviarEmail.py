from crewai import Task
from agents.agenteDeAutomacaoEmail import agenteEnvioEmail

tarefaEnviarEmail = Task(
    description=(
        "Enviar o conteúdo final aprovado para o e-mail do usuário, com o assunto e corpo da mensagem específicos."
    ),
    expected_output="Confirmação de envio do e-mail com o conteúdo final para o usuário.",
    agent=agenteEnvioEmail,
    output_file="resultado.md"
)