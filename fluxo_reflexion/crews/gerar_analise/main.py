from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()

class CrewDeAnalise:
    def __init__(self):
        self.llm = "gpt-4o-mini"
        self.crew = self._criar_crew()

    def _criar_crew(self):
        analisador = Agent(
            role="Analisador",
            goal="Criticar e sugerir melhorias em um texto proposto.",
            verbose=True,
            memory=True,
            llm=self.llm,
            backstory="""
            Especialista em análise crítica de textos acadêmicos com foco em clareza e rigor científico.
            """
        )

        analise_tarefa = Task(
            description=(
                """
                Avalie o seguinte texto com base nos parâmetros fornecidos:\n\n
                - **Tópico**: \"{topico}\"\n
                - **Texto atual**: \"{conteudo}\"\n
                - **Crítica anterior**: \"{critica}\"\n\n
                - **Objetivo do texto**: \"{objetivo}\"\n\n
                Forneça críticas construtivas ou 'perfeito' se adequado.
                """
            ),
            expected_output="Crítica detalhada ou 'perfeito'.",
            agent=analisador
        )

        return Crew(
            agents=[analisador],
            tasks=[analise_tarefa],
            process=Process.sequential
        )

    def kickoff(self, inputs):
        resposta = self.crew.kickoff(inputs=inputs)
        return resposta.raw