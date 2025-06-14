import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

from utils.plot_graph import gerar_grafico
from utils.export_excel import exportar_excel_com_grafico

# Configurações
ticker = "PETR4.SA"
period = "1d"
interval = "1m"

# Diretórios
data_dir = "data"
report_dir = "reports"
os.makedirs(data_dir, exist_ok=True)
os.makedirs(report_dir, exist_ok=True)

# Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Baixa os dados
print(f"Buscando dados para {ticker}...")
df = yf.download(ticker, period=period, interval=interval)

# Salva CSV
csv_path = os.path.join(data_dir, f"{ticker}_{timestamp}.csv")
df.to_csv(csv_path)
print(f"Dados salvos em: {csv_path}")

# Gera gráfico
plot_path = os.path.join(report_dir, f"{ticker}_{timestamp}.png")
gerar_grafico(df, ticker, timestamp, output_dir=report_dir)

# Gera Excel com gráfico embutido
excel_path = os.path.join(report_dir, f"{ticker}_{timestamp}.xlsx")
exportar_excel_com_grafico(csv_path, plot_path, excel_path)
