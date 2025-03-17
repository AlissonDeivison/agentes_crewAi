from dotenv import load_dotenv
from crews.crew_debate import inciar_crew_debate

load_dotenv()
tema_debate = "Vida extraterrestre existe?"

crew_debate, debatedores, coordenador_agent = inciar_crew_debate(tema_debate, num_debatedores=5)


print("Iniciando crew_debate...")
resultado = crew_debate.kickoff()

print("Resultado do debate:")
print(resultado)
