from crewai import Agent


class DebatedorAgent(Agent):
    def __init__(self, i, tema_debate):
        super().__init__(
            role=f"Debatedor {i}",
            goal=f"Propor e aprimorar soluções para o problema proposto no tema {tema_debate}. Todas as saídas devem ser em português do Brasil.",
            verbose=True,
            memory=True,
            backstory=f"Você é o Debatedor {i}. Sua tarefa é propor soluções inovadoras para o problema e aprimorar suas ideias baseadas nas soluções dos outros debatedores.",
            allow_delegation=False
        )
