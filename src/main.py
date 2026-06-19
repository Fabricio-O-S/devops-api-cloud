from fastapi import FastAPI

app = FastAPI(
    title="DevOps API Cloud",
    description="API base para estudos de infraestrutura, Docker e pipelines CI/CD.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "DevOps API Cloud está ativa e rodando!",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "disconnected"  # Será atualizado após configurar a conexão
    }
