from crewai import Task


class CoordenarDebate(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Coordenar um debate sobre o tema. "
                "Você deve garantir que todas as informações utilizadas no relatório sejam baseadas exclusivamente nas discussões dos debatedores. "
                "Evite adicionar informações não mencionadas durante o debate."
            ),
            expected_output=(
                """
                Um relatório detalhado sobre o debate no formato markdown, incluindo:
                - Os temas discutidos
                - As regras estabelecidas
                - As intervenções realizadas
                - Os conflitos resolvidos
                - As decisões tomadas
                - As lições aprendidas"
                O relatório deve conter apenas informações mencionadas pelos debatedores. 
                Verifique a memória do debate antes de redigir o relatório final.
                Muito importante, retire coisas como '''yaml''' e ''' da saída final.
                """
            ),
            agent=agent,
            output_file="data/relatorios/debate.md"
        )
