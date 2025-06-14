import matplotlib.pyplot as plt
import os

def gerar_grafico(dataframe, ticker, timestamp, output_dir="reports"):
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe.index, dataframe["Close"], label="Preço de Fechamento")
    plt.title(f"Variação Intradiária - {ticker}")
    plt.xlabel("Horário")
    plt.ylabel("Preço (R$)")
    plt.legend()
    plt.grid(True)

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"{ticker}_{timestamp}.png")
    plt.savefig(filepath)
    plt.close()
    print(f"Gráfico salvo em: {filepath}")
