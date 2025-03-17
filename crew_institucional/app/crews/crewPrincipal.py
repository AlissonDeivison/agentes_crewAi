from crewai import Crew, Process
from app.agents.classificadorAgent import classificador
from app.agents.receptorAgent import receptor
from app.agents.buscadorAgent import buscador

from app.tasks.classificadorTask import classificadorTask
from app.tasks.receptorTask import receptorTask
from app.tasks.buscadorTask import buscadorTask

crew = Crew(
    agents=[receptor, classificador, buscador],
    tasks=[receptorTask, classificadorTask, buscadorTask],
    process=Process.sequential,
    verbose=True
)
