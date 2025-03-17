from dotenv import load_dotenv
from myllm import MyLLM
from app.crews.crewEnergetica import crewEnergetica


load_dotenv()


resultado = crewEnergetica.kickoff(inputs={})

print(f"Resultado: {resultado}")