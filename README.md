# crudtrainingpycharm
# Projeto CRUD de Vendas em Python com MySQL

Este é um projeto simples que demonstra as operações de Criar, Ler, Atualizar e Apagar (CRUD) em um banco de dados MySQL usando Python.

## Pré-requisitos

- Python 3.8+
- MySQL Server
- Git

## Como Configurar e Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados:**
    - Certifique-se de que seu servidor MySQL está rodando.
    - Abra o MySQL Workbench (ou outra ferramenta de sua preferência).
    - Crie um novo schema chamado `bdyoutube`.
    - Importe a estrutura e os dados executando o arquivo `dump.sql` que está neste projeto (`File > Run SQL Script...`).

5.  **Configure as Credenciais:**
    - **NÃO** coloque sua senha diretamente no código. Renomeie o arquivo `config.example.py` para `config.py`.
    - Abra o arquivo `config.py` e preencha com suas credenciais do MySQL.

6.  **Rode o script principal:**
    ```bash
    python main.py
    ```
