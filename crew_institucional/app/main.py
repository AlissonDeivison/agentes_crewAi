from dotenv import load_dotenv
from crews.crewPrincipal import crew

load_dotenv()
site_url = "https://unifacisa.edu.br/"

pergunta = "Informações sobre o 034/2025 da Unifacisa"

input = {"input_pergunta": pergunta, "site_url": site_url}
resposta = crew.kickoff(inputs=input)

print(resposta)