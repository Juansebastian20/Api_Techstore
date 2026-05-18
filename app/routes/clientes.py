from fastapi import APIRouter, HTTPException, Depends
from app.security.auth import verificar_token
from app.models.cliente import Cliente

router = APIRouter(tags=["Clientes"])

clientes = [
    {
        "id": 1,
        "nombre": "Daniela Pañi",
        "correo": "daniela@gmail.com",
        "telefono": "0999999999",
        "direccion": "Cuenca"
    },
    {
        "id": 2,
        "nombre": "Luis Pinos",
        "correo": "luis@gmail.com",
        "telefono": "0988888888",
        "direccion": "Azogues"
    }
]

# GET
@router.get("/clientes")
def obtener_clientes(user=Depends(verificar_token)):
    return clientes

# POST
@router.post("/clientes")
def agregar_cliente(cliente: Cliente, user=Depends(verificar_token)):

    nuevo = cliente.dict()

    if len(clientes) == 0:
        nuevo["id"] = 1
    else:
        nuevo["id"] = max(c["id"] for c in clientes) + 1

    clientes.append(nuevo)

    return {
        "mensaje": "Cliente agregado correctamente"
    }

# PUT
@router.put("/clientes/{id}")
def actualizar_cliente(
    id: int,
    cliente: Cliente,
    user=Depends(verificar_token)
):

    for i, c in enumerate(clientes):

        if c["id"] == id:

            clientes[i] = cliente.dict()
            clientes[i]["id"] = id

            return {
                "mensaje": "Cliente actualizado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )

# DELETE
@router.delete("/clientes/{id}")
def eliminar_cliente(
    id: int,
    user=Depends(verificar_token)
):

    for i, c in enumerate(clientes):

        if c["id"] == id:

            clientes.pop(i)

            return {
                "mensaje": "Cliente eliminado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )