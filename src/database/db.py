import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Carrega as variáveis de ambiente do arquivo .env local
# Se o arquivo não existir (como no container, onde as variáveis são passadas diretamente),
# o dotenv apenas ignora sem gerar erros.
load_dotenv()

# Recupera as credenciais de forma segura (Regra 4 - Zero Hardcoded)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sua_senha_segura")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "devops_db")

# Constrói a URL de conexão para o PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria o motor de conexão do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Configura a sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para a criação dos modelos (declarative base)
Base = declarative_base()

# Dependência (Session Generator) injetada nas rotas do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
