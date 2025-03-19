from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewDeAnalise:
    """Crew de Análise"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def analise(self) -> Agent:
        return Agent(
            config=self.agents_config["analista"],
        )

    @task
    def analise_dados(self) -> Task:
        return Task(
            config=self.tasks_config["gerar_opiniao_e_classificar_topicos"],
        )

    @crew
    def crew(self) -> Crew:
        """Cria a Crew de Análise"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )