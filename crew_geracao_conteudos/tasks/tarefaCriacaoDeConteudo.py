from crewai import Task
from agents.agenteDeConteuto import agenteDeConteudo

tarefaCriacaoDeConteudo = Task(
    description=(
        "Com base nos tópicos revisados, desenvolva um conteúdo educacional completo e estruturado. "
        "Garanta que o material siga a sequência lógica dos tópicos e esteja adequado ao formato definido como: {conteudo} "
        "Aplique storytelling, copywriting e design instrucional para tornar o aprendizado envolvente e eficaz. "
        "Certifique-se de que o conteúdo tenha introdução, desenvolvimento e conclusão bem definidos."
    ),
    expected_output=(
        "Um conteúdo educacional formatado corretamente de acordo com a solicitação do usuário. "
        "O material deve ser claro, estruturado e adequado ao público-alvo, sem perder profundidade ou qualidade. "
        "O conteúdo deve ser entregue nos formato:{conteudo}"
    ),
    agent=agenteDeConteudo
)