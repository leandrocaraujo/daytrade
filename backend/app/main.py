from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, assets

app = FastAPI(
    title="Plataforma Analítica Financeira",
    description="API para análise de mercado financeiro em tempo real",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(auth.router)
app.include_router(assets.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Plataforma Analítica Financeira"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
