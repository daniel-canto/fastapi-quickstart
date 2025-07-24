# 🚀 FastAPI Quickstart Project with SQLite

Uma API RESTful construída com **FastAPI** e **SQLite**, com autenticação via **JWT** e boas práticas de arquitetura de projeto. 
Ideal para um rápido estudo sobre o **FastAPI**.

---

## 🛠️ Tecnologias Utilizadas

-------------------------------------------------------------------------
| Ferramenta            | Descrição                                     |
|-----------------------|-----------------------------------------------|
| 🐍 **Python 3.12+**   | Linguagem principal do projeto                |
| ⚡ **FastAPI**         | Framework moderno e performático para APIs    |
| 🛢️ **SQLite**         | Banco de dados leve, baseado em arquivos      |
| 🔐 **JWT (JOSE)**     | Autenticação segura baseada em token          |
| 🧰 **SQLAlchemy**     | ORM para manipulação de banco de dados        |
| 🧪 **Pydantic**       | Validação de dados e schemas com segurança    |
| 🌐 **Uvicorn**        | Servidor ASGI leve para rodar a aplicação     |
-------------------------------------------------------------------------

---

## ✅ Funcionalidades

- 📌 Cadastro e login de usuários
- 🔐 Autenticação JWT (Token dinâmico e expiração configurável)
- 🧱 SQLite com SQLAlchemy configurado e instanciado corretamente
- 🧼 Middleware global para proteger rotas autenticadas
- 🎯 Boas práticas de organização de projeto
- ⚠️ Retorno de erros customizados com mensagens amigáveis

---

## 📁 Estrutura do Projeto
fastapi-quickstart/
├── main.py # Ponto de entrada da aplicação <br>
├── db.py # Instância do banco (engine + session) <br>
├── models/ # Models SQLAlchemy (ex: User) <br>
├── schemas/ # Schemas Pydantic (validação de dados) <br>
├── routes/ # Rotas organizadas por funcionalidade <br>
├── utils/ <br>
│ └── auth/ # Lógica JWT (criação e validação de token) <br>
├── middleware/ # Middleware para verificar autenticação <br>

---

## ▶️ Como rodar o projeto

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/fastapi-quickstart.git
cd fastapi-quickstart


# 2. Crie o ambiente virtual
python -m venv .venv

# 3. Ative o ambiente Virtual
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Rode a aplicação
uvicorn main:app --reload
```

Acesse: http://localhost:8000/docs para testar a API com Swagger UI.

---

🙌 Autor

Daniel Canto

📧 Entre em contato: [daniel.canto.contato@gmail.com]
💼 LinkedIn: Daniel Canto(www.linkedin.com/in/daniel-canto-767399234)