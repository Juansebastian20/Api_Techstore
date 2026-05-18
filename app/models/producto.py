from typing import Optional
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: str
    precio: float
    stock: int