# 🚀 API de Usuários com FastAPI

Este projeto é uma API simples desenvolvida com FastAPI e PostgreSQL para gerenciamento de usuários.

---

# 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

- Python 3.10 ou superior
- PostgreSQL
- pip (gerenciador de pacotes do Python)

Verifique sua versão do Python:

```bash
python --version
```

---

# 📦 1️⃣ Clonar o Repositório

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
```

---

# 🧪 2️⃣ Criar e Ativar Ambiente Virtual (Recomendado)

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

Ativar no Mac/Linux:

```bash
source venv/bin/activate
```

---

# 📥 3️⃣ Instalar as Dependências

Se houver `requirements.txt`:

```bash
pip install -r requirements.txt
```

Caso precise instalar manualmente:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

---

# 🗄 4️⃣ Configurar o Banco de Dados

Certifique-se de que o PostgreSQL esteja em execução.

## Criar o banco:

```sql
CREATE DATABASE fastapi_db;
```

---

## Configurar a conexão

Abra o arquivo `database.py` e ajuste a variável:

```python
DATABASE_URL = "postgresql://postgres:SUA_SENHA@localhost:5432/fastapi_db"
```

Substitua `SUA_SENHA` pela senha do seu PostgreSQL.

---

# ▶️ 5️⃣ Executar o Projeto

Dentro da pasta do projeto, execute:

```bash
uvicorn main:app --reload
```

Se necessário:

```bash
py -m uvicorn main:app --reload
```

---

# 🌐 6️⃣ Acessar a Aplicação

Após iniciar o servidor, acesse no navegador:

```
http://127.0.0.1:8000
```

---

# 📖 7️⃣ Documentação Interativa

A documentação automática da API está disponível em:

```
http://127.0.0.1:8000/docs
```

Nessa página é possível testar todas as rotas diretamente pelo navegador.

---

# ✅ Observações

- O banco deve estar ativo antes de iniciar o servidor.
- As tabelas são criadas automaticamente na primeira execução.
- Caso ocorra erro de conexão, verifique usuário, senha e porta do PostgreSQL.