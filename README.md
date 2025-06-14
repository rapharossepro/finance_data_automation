
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

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script:

```bash
python main.py
```

5. Veja os resultados nas pastas `data/` e `reports/`

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
