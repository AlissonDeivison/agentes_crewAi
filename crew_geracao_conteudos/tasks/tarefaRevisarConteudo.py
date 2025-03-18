from crewai import Task
from agents.agenteRevisor import agenteRevisor

tarefaRevisarConteudo = Task(
    description=(
        "Revisar os tópicos e conteúdos gerados pelos outros agentes, "
        "garantindo que estejam alinhados com as necessidades do usuário. "
        "Verifique a clareza, relevância e qualidade educacional do material. "
        "Caso necessário, sugira ajustes ou correções antes da aprovação final."
    ),
    expected_output=(
        "Uma versão revisada e aprovada dos tópicos e conteúdos "
    ),
    agent=agenteRevisor
)