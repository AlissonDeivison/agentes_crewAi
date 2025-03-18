from dotenv import load_dotenv
from crewai.flow.flow import Flow, listen, start
load_dotenv()

class FluxoSimples(Flow):
    @start()
    def saudacao(self):
        #Aqui pode ser uma crew inteira
        print("Iniciando o fluxo simples")
        mensagem = "Olá! Bem-vindo ao fluxo matemático simples."
        print(mensagem)
        
        return mensagem
    
    @listen(saudacao)
    def obter_numeros(self, mensagem):
        #Aqui pode ser uma segunda crew que espera a saída da primeira
        print(f"Mensagem do usuário: {mensagem}")
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print(f"Os números digitados foram: {numero1} e {numero2}")
        
        return numero1, numero2
    
    @listen(obter_numeros)
    def calcular_soma(self, numeros):
        #Aqui pode ser uma terceira crew que espera a saída da segunda
        numero1, numero2 = numeros
        soma = numero1 + numero2
        print(f"A soma dos números é: {soma}")
        
        return soma

fluxo = FluxoSimples()
resultado = fluxo.kickoff()

fluxo.plot()