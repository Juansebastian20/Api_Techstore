from typing import Optional
from pydantic import BaseModel

class Cliente(BaseModel):
    id: Optional[int] = None
    nombre: str
    correo: str
    telefono: str
    direccion: str