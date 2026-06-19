from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from src.database.db import engine, Base, get_db
from src.routes import tasks_router

# Cria as tabelas no banco de dados automaticamente na inicialização da API
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Erro ao tentar criar tabelas no banco de dados: {e}")

app = FastAPI(
    title="DevOps API Cloud",
    description="API base para estudos de infraestrutura, Docker e pipelines CI/CD.",
    version="1.0.0"
)

# Registra a rota de tarefas
app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "DevOps API Cloud está ativa e rodando!",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Valida o estado da aplicação e da conexão com o banco de dados."""
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected (error: {str(e)})"

    return {
        "status": "healthy" if db_status == "connected" else "degraded",
        "database": db_status
    }
