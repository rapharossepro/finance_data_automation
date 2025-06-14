import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def exportar_excel_com_grafico(csv_path, plot_path, output_path):
    # Carrega os dados do CSV
    df = pd.read_csv(csv_path)

    # Salva em Excel
    df.to_excel(output_path, index=False)

    # Abre o Excel e adiciona o gráfico
    wb = load_workbook(output_path)
    ws = wb.active

    img = Image(plot_path)
    img.anchor = 'H2'
    ws.add_image(img)

    wb.save(output_path)
    print(f"Relatório Excel com gráfico salvo em: {output_path}")
