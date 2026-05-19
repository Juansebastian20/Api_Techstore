from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import login, clientes, productos, pedidos

app = FastAPI(
    title="API Comercial",
    description="API para gestionar clientes, productos y pedidos con autenticación JWT",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "API funcionando"}
    
app.include_router(login.router)
app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(pedidos.router)