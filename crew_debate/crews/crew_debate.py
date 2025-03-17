from crewai import Crew, Process
from agents.debatedor_agent import DebatedorAgent
from tasks.debate_task import DebateTask
from agents.coordenador_agent import CoordenadorAgent
from tasks.coordenador_task import CoordenarDebate

def inciar_crew_debate(tema_debate, num_debatedores):
    debatedores = []
    tasks = []
    
    # Cria o coordenador
    coordenador_agent = CoordenadorAgent(tema_debate=tema_debate)
    
    # Cria os debatedores e suas tarefas
    for i in range(num_debatedores):
        debatedor_agent = DebatedorAgent(i=i, tema_debate=tema_debate)
        # Removido o argumento "coordenador" pois DebateTask não o aceita
        crew_debate_task = DebateTask(agent=debatedor_agent, rodada=0, i=i)
        
        debatedores.append(debatedor_agent)
        tasks.append(crew_debate_task)
    
    # Cria a tarefa do coordenador
    coordenar_debate_task = CoordenarDebate(agent=coordenador_agent)
    tasks.append(coordenar_debate_task)
    
    # Cria a crew com todos os agentes e tarefas
    crew = Crew(
        agents=[coordenador_agent] + debatedores, 
        tasks=tasks,  
        process=Process.sequential  
    )
    
    return crew, debatedores, coordenador_agent  
