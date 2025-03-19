from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewDePesquisa:
    """Crew de Pesquisa"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def analise(self) -> Agent:
        return Agent(
            config=self.agents_config["pesquisador"],
        )

    @task
    def analise_dados(self) -> Task:
        return Task(
            config=self.tasks_config["escrever_topicos"],
        )

    @crew
    def crew(self) -> Crew:
        """Cria a Crew de Pesquisa"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )