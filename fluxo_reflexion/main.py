from crewai.flow.flow import Flow, listen, start, router
from crews.gerar_topicos.main import CrewGerarTopicos
from crews.gerar_analise.main import CrewDeAnalise
from pydantic import BaseModel
from datetime import datetime
import os
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReflexionState(BaseModel):
    topico: str = ""
    artigo: str = ""
    critica: str = ""
    validacao: str = ""
    tentativas: int = 0

class ReflexionFlow(Flow[ReflexionState]):

    def _criar_diretorio(self):
        """Cria diretório único para os resultados"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_pasta = f"{self.state.topico.lower().replace(' ', '_')}_{timestamp}"
        self.diretorio = os.path.join("resultados", nome_pasta)
        os.makedirs(self.diretorio, exist_ok=True)
        logger.info(f"Diretório criado: {self.diretorio}")

    def _salvar_arquivo(self, nome_arquivo, conteudo):
        """Salva um arquivo no diretório de resultados"""
        caminho_completo = os.path.join(self.diretorio, nome_arquivo)
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo.strip())
        logger.info(f"Arquivo salvo: {caminho_completo}")

    def _salvar_arquivos(self):
        """Salva os arquivos apenas quando o processo estiver concluído"""
        self._criar_diretorio()
        self._salvar_arquivo("artigo.md", self.state.artigo)
        self._salvar_arquivo("critica.md", self.state.critica)
    
    @start()
    def inicio(self):
        logger.info(f'🚀 Iniciando fluxo para: "{self.state.topico}"')
        self.state.artigo = ""
        self.state.critica = ""
        self.state.validacao = ""
        self.state.tentativas = 0

    @listen("inicio")
    def idealista(self):
        logger.info("🔍 Gerando versão inicial do artigo...")
        crew = CrewGerarTopicos()
        self.state.artigo = crew.kickoff(inputs={"topico": self.state.topico})

    @router(idealista)
    def analisador(self):
        logger.info("🛠️ Analisando e validando conteúdo...")
        crew = CrewDeAnalise()
        resultados = crew.kickoff(
            inputs={
                "topico": self.state.topico,
                "conteudo": self.state.artigo,
                "critica": self.state.critica,
                "objetivo": "Artigo Científico bem embasado e claro..."
            }
        )

        if "---VALIDACAO---" in resultados:
            self.state.critica, self.state.validacao = resultados.split("---VALIDACAO---")
        else:
            self.state.critica = resultados
            self.state.validacao = "Validação automática não disponível"

        self.state.tentativas += 1
        
        # Atualiza o artigo conforme as críticas e melhorias
        self.state.artigo += f"\n\n## Revisão {self.state.tentativas}\n{self.state.critica}"
        
        if self.state.tentativas >= 3 or 'perfeito' in self.state.critica.lower():
            return "completed"
        return "inicio"

    @listen("completed")
    def sucesso(self):
        logger.info("\n✅ Processo concluído com sucesso!")
        self._salvar_arquivos()
        logger.info("\n" + "="*50)
        logger.info(f"📄 Artigo Final:\n{self.state.artigo[:300]}...")
        logger.info("\n" + "="*50)
        logger.info(f"📊 Dados de Validação:\n{self.state.validacao[:200]}...")

if __name__ == "__main__":
    os.makedirs("resultados", exist_ok=True)
    reflexion = ReflexionFlow()
    reflexion.kickoff(inputs={"topico": "IA generativa na Educação Superior"})