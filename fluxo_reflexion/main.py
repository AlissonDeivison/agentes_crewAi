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
        
        try:
            os.makedirs(self.diretorio, exist_ok=True)
            logger.info(f"Diretório criado: {self.diretorio}")
            return self.diretorio
        except Exception as e:
            logger.error(f"Erro ao criar diretório: {e}")
            raise

    def _salvar_arquivo(self, nome_arquivo, conteudo):
        """Salva um arquivo no diretório de resultados"""
        caminho_completo = os.path.join(self.diretorio, nome_arquivo)
        try:
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(conteudo.strip())
            logger.info(f"Arquivo salvo: {caminho_completo}")
        except Exception as e:
            logger.error(f"Erro ao salvar arquivo {nome_arquivo}: {e}")
            raise

    def _salvar_arquivos(self):
        """Salva todos os arquivos no diretório correto"""
        try:
            # Cria o diretório principal
            self._criar_diretorio()
            
            # Artigo Principal
            self._salvar_arquivo(
                "artigo.md",
                f"# Artigo: {self.state.topico}\n\n{self.state.artigo}"
            )
            
            # Relatório de Processo
            self._salvar_arquivo(
                "relatorio.md",
                f"""
# Relatório do Processo
**Tópico**: {self.state.topico}
**Data**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Iterações**: {self.state.tentativas}
**Status**: {'✅ Aprovado' if 'perfeito' in self.state.critica.lower() else '🔄 Em Revisão'}

## Análise Crítica
{self.state.critica}
"""
            )
            
            # Validação de Fontes
            self._salvar_arquivo(
                "validacao_fontes.md",
                f"# Relatório de Validação\n\n{self.state.validacao}"
            )
            
            print(f"\n📁 Pasta de resultados criada em: {os.path.abspath(self.diretorio)}")
            
        except Exception as e:
            logger.error(f"Erro ao salvar arquivos: {e}")
            raise

    @start()
    def inicio(self):
        print(f'🚀 Iniciando fluxo para: "{self.state.topico}"')
        self.state.artigo = ""
        self.state.critica = ""
        self.state.validacao = ""
        self.state.tentativas = 0

    @listen("inicio")
    def idealista(self):
        print("🔍 Gerando versão inicial do artigo...")
        crew = CrewGerarTopicos()
        self.state.artigo = crew.kickoff(
            inputs={"topico": self.state.topico}
        )

    @router(idealista)
    def analisador(self):
        print("🛠️ Analisando e validando conteúdo...")
        crew = CrewDeAnalise()
        resultados = crew.kickoff(
            inputs={
                "topico": self.state.topico,
                "conteudo": self.state.artigo,
                "critica": self.state.critica,
                "objetivo": "Artigo Científico bem embasado e claro. Utilizar referências recentes e confiáveis. Mínimo de 1500 palavras. Formatação em Markdown. Incluir seções de Introdução, Revisão da Literatura, Análise Crítica e Conclusões."
            }
        )
        
        # Verifica se o separador está presente
        if "---VALIDACAO---" in resultados:
            self.state.critica, self.state.validacao = resultados.split("---VALIDACAO---")
        else:
            # Fallback seguro
            self.state.critica = resultados
            self.state.validacao = "Validação automática não disponível"
        
        self.state.tentativas += 1

        if self.state.tentativas >= 3 or 'perfeito' in self.state.critica.lower():
            return "completed"
        return "inicio"

    @listen("completed")
    def sucesso(self):
        print("\n✅ Processo concluído com sucesso!")
        self._salvar_arquivos()
        
        # Resumo executivo
        print("\n" + "="*50)
        print(f"📄 Artigo Científico (1500 palavras):\n{self.state.artigo[:300]}...")
        print("\n" + "="*50)
        print(f"📊 Dados de Validação:\n{self.state.validacao[:200]}...")

if __name__ == "__main__":
    # Cria a pasta resultados se não existir
    os.makedirs("resultados", exist_ok=True)
    
    reflexion = ReflexionFlow()
    reflexion.kickoff(inputs={"topico": "IA generativa na Saúde"})