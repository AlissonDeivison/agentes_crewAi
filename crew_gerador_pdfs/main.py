from fpdf import FPDF
from PIL import Image
import os

# Definindo a classe personalizada
class MyCustomTool:
    name: str = "PDF Generator Tool"
    description: str = """Esta ferramenta gera um arquivo PDF que inclui um título, uma descrição e uma imagem de gráfico. 
    O PDF resultante terá o título e a descrição seguidos pela imagem especificada no caminho."""

    def _run(self, title: str, text: str, image_path: str) -> str:
        # Verificar se a imagem existe
        if not os.path.exists(image_path):
            return "Erro: O caminho da imagem não é válido."
        
        # Criar um objeto PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Adicionar título
        pdf.set_font("Arial", size=16, style='B')
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        
        # Adicionar descrição
        pdf.ln(10)  # Espaço entre título e texto
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=text)

        # Adicionar a imagem
        try:
            # Abre a imagem e calcula o tamanho para ajustar à página
            image = Image.open(image_path)
            image_width, image_height = image.size
            pdf.ln(10)  # Espaço entre o texto e a imagem
            pdf.image(image_path, x=10, w=180)  # Ajuste de largura (w=180)
        except Exception as e:
            return f"Erro ao adicionar a imagem: {e}"

        # Gerar o arquivo PDF
        output_pdf = "output_file.pdf"
        pdf.output(output_pdf)
        
        return f"PDF gerado com sucesso: {output_pdf}"

tool = MyCustomTool()
result = tool._run("Gráfico de distribuição da matriz energética", "Este gráfico mostra a distribuição da matriz energética", "distribuição_percentual_da_matriz_energética_global_para_2025.png")
print(result)
