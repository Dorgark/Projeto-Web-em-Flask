# Sistema Web Flask MVC

Projeto acadêmico desenvolvido em **Python** com **Flask**, aplicando a arquitetura **MVC** (*Model-View-Controller*), mapeamento objeto-relacional com **SQLAlchemy**, banco de dados **MySQL** e renderização de páginas com **Jinja2**.

## Funcionalidades
- **Cadastro, login e logout** de usuários com gerenciamento de sessão e mensagens *flash*.
- **Perfil de usuário** exibindo dados da conta autenticada.
- **Controle de acesso por perfil (RBAC)** com listagem de usuários restrita a administradores.
- **Estrutura modular** separando configuração, modelos (*Models*), rotas/regras (*Controllers* via *Blueprints*) e interfaces (*Views*).

## Estrutura do Projeto
- `app/__init__.py`: *Application Factory* (`create_app`), inicialização do SQLAlchemy e registro de *Blueprints*.
- `app/config.py`: leitura de variáveis de ambiente via `python-dotenv`.
- `app/models/user.py`: modelo relacional `User` (`usuarios`).
- `app/controllers/`: rotas e lógica de autenticação (`auth_controller.py`), usuário (`user_controller.py`) e administração (`admin_controller.py`).
- `app/templates/`: templates HTML com herança Jinja2 (`base.html`, `index.html`, `login.html`, `cadastro.html`, `perfil.html`, `admin_lista.html`).
- `app/static/style.css`: estilos da aplicação.
- `run.py`: ponto de entrada que cria as tabelas e inicia o servidor.

## Como Executar Localmente
1. Crie e ative um ambiente virtual (`venv`) e instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure o arquivo `.env` na raiz com `SECRET_KEY` e `DATABASE_URL` apontando para o MySQL.
3. Execute a aplicação:
   ```bash
   python run.py
   ```
