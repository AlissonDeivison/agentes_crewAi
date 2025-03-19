from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import re
from pydantic import BaseModel, ValidationError
import os

load_dotenv()

class InputValidator(BaseModel):
    topico: str
    conteudo: str = ""
    critica: str = ""

class CrewGerarTopicos():
    def __init__(self):
        self.search_tool = SerperDevTool()
        self.llm = "gpt-4o"
        self.crew = self._criar_crew()
        self.references = []

    def _validar_fontes(self, content):
        """Valida e formata as referências no texto"""
        matches = re.findall(r'\[(\d+)\]\((https?://[^\s]+)\)', content)
        fontes_validas = [
            'doi.org', 'nih.gov', 'science.org', 
            'jamanetwork.com', 'nejm.org', 'springer.com',
            'thelancet.com', 'elsevier.com', 'nature.com'
        ]
        validas = 0
        
        for num, url in matches:
            if any(dominio in url for dominio in fontes_validas):
                self.references.append(f"{num}. {url}")
                validas += 1
            else:
                content = content.replace(f'[{num}]({url})', f'[{num}]')
                self.references.append(f"{num}. Fonte inválida: {url[:30]}...")
        
        if validas < 3:
            content += "\n\n⚠️ ATENÇÃO: Menos de 3 fontes validadas encontradas"
        
        return content

    def _criar_crew(self):
        pesquisador = Agent(
            role="Pesquisador Científico Sênior",
            goal="Coletar fontes acadêmicas válidas sobre {topico}",
            backstory="""Especialista em pesquisa com 15 anos de experiência em bases científicas,
            mestre em recuperação de informação médica""",
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False,
            tool_config={
                "Search the internet with Serper": {
                    "search_query": "artigos científicos sobre {topico} (site:*.gov OR site:*.edu OR site:*.org) after:2020"
                }
            }
        )

        escritor = Agent(
            role="Redator Científico",
            goal="Escrever artigo acadêmico de 1500 palavras sobre {topico}",
            backstory="""Pesquisador doutor com mais de 50 publicações em revistas de alto impacto,
            especialista em redação técnica""",
            llm=self.llm,
            verbose=True
        )

        revisor = Agent(
            role="Revisor Chefe",
            goal="Validar integridade acadêmica do conteúdo",
            backstory="""Editor-chefe de revista científica indexada, especialista em ética de publicação""",
            llm=self.llm,
            verbose=True
        )

        pesquisa_task = Task(
            description="""Realizar busca acadêmica rigorosa sobre {topico} incluindo:
            1. Artigos publicados após 2020
            2. Fontes governamentais ou institucionais
            3. Dados de ensaios clínicos
            4. Estatísticas oficiais""",
            expected_output="Lista de 5-7 referências validadas com URLs completas",
            agent=pesquisador,
            tools=[self.search_tool],
            output_file="referencias.md"
        )

        escrita_task = Task(
            description="""Produzir artigo completo com:
            1. Introdução contextualizada
            2. Revisão da literatura
            3. Análise crítica
            4. Conclusões com recomendações
            5. Referências formatadas""",
            expected_output="Documento em markdown com 1500 palavras e citações [n]",
            agent=escritor,
            context=[pesquisa_task],
            output_file="artigo.md"
        )

        revisao_task = Task(
            description="""Realizar verificação final:
            1. Checar URLs das referências
            2. Validar consistência das citações
            3. Garantir padrão acadêmico""",
            expected_output="Relatório de validação técnico",
            agent=revisor,
            context=[pesquisa_task, escrita_task],
            async_execution=True,
            output_file="validacao.md"
        )

        return Crew(
            agents=[pesquisador, escritor, revisor],
            tasks=[pesquisa_task, escrita_task, revisao_task],
            process=Process.sequential,
            memory=True,
            verbose=True
        )

    def kickoff(self, inputs):
        try:
            validados = InputValidator(**inputs).dict()
            resultado = self.crew.kickoff(inputs=validados)
            conteudo_validado = self._validar_fontes(resultado.raw)
            
            return (
                f"{conteudo_validado}\n\n"
                "## Referências Validadas\n" + 
                "\n".join(self.references)
            )
            
        except ValidationError as e:
            return f"Erro nos inputs: {e.json()}"