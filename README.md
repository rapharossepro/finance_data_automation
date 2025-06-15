
# 📈 Finance Data Automation

Automação em Python para extração, análise e geração de relatórios com dados financeiros em tempo real.  
Este projeto foi desenvolvido como parte do portfólio técnico com foco em automações para o setor financeiro, utilizando dados de ações da B3.

---

## 🚀 Funcionalidades

- Coleta automatizada de cotações de ações via API do Yahoo Finance (`yfinance`)
- Salvamento dos dados em arquivos `.csv`
- Geração de gráficos de variação intradiária com `matplotlib`
- Exportação para planilhas `.xlsx` com o gráfico embutido
- Organização em pastas estruturadas: `data/` e `reports/`

---

## 🧰 Tecnologias e Bibliotecas

- Python 3.11+
- [yfinance](https://pypi.org/project/yfinance/)
- pandas
- matplotlib
- openpyxl

---

## 📂 Estrutura do Projeto

```
finance_data_automation/
├── data/                  # Armazena os arquivos CSV com os dados
├── reports/               # Contém os gráficos gerados e relatórios Excel
├── utils/                 # Funções auxiliares para geração de gráfico e Excel
│   ├── plot_graph.py
│   └── export_excel.py
├── main.py                # Script principal da automação
├── requirements.txt       # Dependências do projeto
└── README.md
```

---

## ⚙️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/rapharossepro/finance_data_automation.git
cd finance_data_automation
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script:

```bash
python main.py
```

---

## 📊 Como acessar os dados gerados

Após executar o script, os seguintes arquivos serão criados automaticamente:

| Tipo de Arquivo | Caminho               | Conteúdo                                                                 |
|-----------------|------------------------|--------------------------------------------------------------------------|
| 📄 CSV          | `data/`                | Dados brutos da ação minuto a minuto                                     |
| 📈 PNG          | `reports/`             | Gráfico de variação do preço intradiário                                 |
| 📘 Excel        | `reports/`             | Planilha com os dados + gráfico embutido automaticamente (em `H2`)       |

### 🧪 Exemplo de nomes gerados:

```
data/PETR4.SA_2025-06-14_21-30-55.csv
reports/PETR4.SA_2025-06-14_21-30-55.png
reports/PETR4.SA_2025-06-14_21-30-55.xlsx
```

> Os nomes dos arquivos incluem a data e hora em que foram gerados.

---

## 🔁 Personalização

Você pode alterar o ticker (ação) dentro do `main.py`:

```python
ticker = "PETR4.SA"  # Ex: VALE3.SA, ITUB4.SA, AAPL, TSLA etc.
```

---

## 📌 Em desenvolvimento

- [ ] Envio automático do relatório por e-mail
- [ ] Agendamento da execução com `schedule`
- [ ] Interface web simples com Streamlit

---

## 🧠 Objetivo

Este projeto foi desenvolvido como parte do portfólio pessoal para demonstrar domínio em:

- Coleta e manipulação de dados financeiros
- Automação de tarefas com Python
- Geração de relatórios visuais e técnicos
- Organização de código para uso corporativo

---

## 📬 Contato

Feito por [Raphael Del Rosse](https://www.linkedin.com/in/raphaeldelrosse/)  
📧 rapharosseprofissional@gmail.com  
📦 GitHub: [github.com/rapharossepro](https://github.com/rapharossepro)

---

## 📄 Licença

MIT License © 2025 Raphael Del Rosse
