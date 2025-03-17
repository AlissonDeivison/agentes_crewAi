from crewai.tools import BaseTool
import matplotlib.pyplot as plt

class GraphTool(BaseTool):
    name: str = "Ferramenta de criação de Gráficos"
    description: str = """Gera um gráfico com base em uma lista de valores e um tipo de gráfico específicado (linha, barras ou pizza) e salva o gráfico como um arquivo PNG."""

    def _run(self, values: list, labels: list = None, chart_type: str = "linha", title: str = "Gráfico de Linha") -> str:
        plt.figure(figsize=(6, 6))  # Define o tamanho para melhor visualização
        
        if chart_type == "linha":
            plt.plot(values, marker='o')  # Adiciona marcadores para maior clareza
            plt.title(title)
        elif chart_type == "barra":
            plt.bar(range(len(values)), values, tick_label=labels)
            plt.title(title)
        elif chart_type == "pizza":
            if labels is None:  # Garante que labels tenha um valor válido
                labels = [f"Item {i}" for i in range(len(values))]
            plt.pie(values, labels=labels, autopct='%1.1f%%')  # Corrigido o uso de labels
            plt.title(title)
        else:
            return "Tipo de gráfico inválido. Escolha entre: linha, barra ou pizza."
        
        file_name = f"{title.lower().replace(' ', '_')}.png"
        plt.savefig(file_name, dpi=300, bbox_inches="tight")  # Melhora qualidade da imagem
        
        plt.close()  # Fecha a figura para evitar consumo excessivo de memória
        
        return f"Gráfico salvo em {file_name}"
