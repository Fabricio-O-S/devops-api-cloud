# DevOps API Cloud

API em Python estruturada com foco em boas práticas de arquitetura, conteinerização com Docker e esteiras de CI/CD. Este projeto serve como base sólida para demonstrar minhas habilidades em DevOps, infraestrutura e deploy automatizado em nuvem.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.11, FastAPI (Fast, Async)
- **Banco de Dados:** PostgreSQL (Alpine Image no container)
- **Infraestrutura/Containers:** Docker & Docker Compose, Nginx (Proxy Reverso)
- **Ambiente de Produção/PaaS:** Configurações preparadas para Azure App Services (Procfile e runtime.txt)

---

## 📂 Estrutura do Projeto

A arquitetura do projeto segue o padrão profissional de pastas, separando claramente as responsabilidades:

```text
devops-api-cloud/
├── src/                    # Código-fonte principal da API
│   ├── main.py             # Entrada da aplicação (FastAPI)
│   ├── routes/             # Definição dos endpoints
│   ├── models/             # Modelos de dados (SQLAlchemy)
│   └── database/           # Gerenciamento de conexões com o BD
├── infra/                  # Arquivos de configurações de rede/infra
│   └── nginx/              # Proxy Reverso
├── docker/                 # Configurações de empacotamento
│   └── Dockerfile          # Build da imagem da API
├── config/                 # Arquivos de configuração e ambiente (.env.example)
├── logs/                   # Histórico de logs da aplicação
├── tests/                  # Testes automatizados da API
├── docs/                   # Documentação do projeto e estudos de caso
├── docker-compose.yml      # Orquestração local dos containers
├── requirements.txt        # Dependências do Python
├── Procfile & runtime.txt  # Configurações para deploy automatizado na nuvem
└── README.md               # Esta documentação
```

---

## 🚀 Como Executar Localmente

### 1. Clonar o Repositório e Configurar o Ambiente Virtual
Clone o projeto para sua máquina e crie o ambiente virtual:

```bash
# Criar o ambiente virtual (.venv)
python -m venv .venv

# Ativar o ambiente virtual:
# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# No Linux/Mac:
source .venv/bin/activate

# Atualizar o pip e instalar dependências
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente
Copie o arquivo de exemplo de ambiente e preencha com suas configurações:
```bash
cp config/.env.example .env
```

### 3. Rodar com Docker Compose
Para subir toda a infraestrutura local (API + PostgreSQL), certifique-se de que o Docker está ativo e execute:
```bash
docker-compose up --build
```
A API estará acessível em `http://localhost:8000`. A documentação automática interativa do FastAPI (Swagger) estará disponível em `http://localhost:8000/docs`.

---

## 🧠 O que aprendi

- **Arquitetura de Pastas Profissional:** Como estruturar um projeto escalável dividindo o código de negócio (`src/`) das configurações de infraestrutura (`docker/`, `infra/`).
- **Segurança de Credenciais:** Configuração de `.env.example` e isolamento de segredos no `.gitignore` para evitar vazamento de credenciais no controle de versão.
- **Estruturação de Container Docker:** Criação de um Dockerfile multiuso e orquestração local com `docker-compose` simulando uma API conectada a um banco de dados real em rede isolada.
