# 🚗 Car API

API REST desenvolvida com **FastAPI** para gerenciamento de veículos.

## 📋 Informações do Projeto

| Item | Valor |
|------|--------|
| Nome | Car API |
| Versão | 0.1.0 |
| Autor | Lucas |
| E-mail | contato.lucas55@gmail.com |

---

# 🚀 Tecnologias

- Python 3.14+
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Ruff
- Taskipy

---

# 📁 Estrutura do Projeto

```
app/
├── cars/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   └── presentation/
│
├── shared/
│   ├── database/
│   ├── exceptions/
│   └── utils/
│
main.py
```

---

# ⚙️ Instalação

Clone o projeto

```bash
git clone <repositorio>
```

Entre na pasta

```bash
cd car-api
```

Crie o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

Instale as dependências

```bash
pip install -e .
```

---

# ▶️ Executando a aplicação

Utilizando o Taskipy

```bash
task run
```

Ou diretamente

```bash
fastapi dev main.py
```

---

# 📖 Documentação da API

Após iniciar a aplicação:

Swagger

```
http://localhost:8000/docs
```

Redoc

```
http://localhost:8000/redoc
```

---

# 🧹 Qualidade de Código

Este projeto utiliza **Ruff** para lint e formatação.

## Verificar problemas

```bash
task lint
```

ou

```bash
ruff check
```

---

## Corrigir automaticamente

```bash
task lint_fix
```

ou

```bash
ruff check --fix
```

---

## Formatar código

```bash
task format
```

ou

```bash
ruff format
```

---

# 📝 Configuração do Ruff

```toml
[tool.ruff]
line-length = 79
extend-exclude = ["migrations"]

[tool.ruff.lint]
preview = true
select = ["I", "F", "E", "W", "PL", "PT"]

[tool.ruff.format]
preview = true
quote-style = "single"
```

---

# 🏗️ Taskipy

Comandos disponíveis

| Comando | Descrição |
|----------|-----------|
| task run | Executa a API |
| task lint | Executa o lint |
| task lint_fix | Corrige problemas automaticamente |
| task format | Formata o código |

---

# 📦 Versionamento

```
0.1.0
```

Primeira versão da API.

---

# 📄 Licença

Este projeto está disponível para fins de estudo e desenvolvimento.

---

# 👤 Autor

**Lucas**

contato.lucas55@gmail.com