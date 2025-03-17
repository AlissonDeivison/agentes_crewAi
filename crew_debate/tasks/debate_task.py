from crewai import Task


class DebateTask(Task):
    def __init__(self, agent, rodada, i):
        super().__init__(
            description=f"Rodada {rodada + 1}, apresente sua solução parcial para o problema",
            expected_output="Uma solução atualizada para o problema. Todas as saídas devem ser em português do Brasil.",
            agent=agent,
            output_file=f"data/solucoes/solucao_debatedor_{i}_rodada_{rodada + 1}.txt",
        )
