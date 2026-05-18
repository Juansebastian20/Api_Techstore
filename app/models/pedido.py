from typing import Optional
from pydantic import BaseModel

class Pedido(BaseModel):
    id: Optional[int] = None
    cliente_id: int
    productos_ids: list[int]
    total: float
    estado: str
    estado: str