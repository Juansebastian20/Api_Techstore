from fastapi import APIRouter, HTTPException, Depends
from app.security.auth import verificar_token
from app.models.pedido import Pedido

router = APIRouter(tags=["Pedidos"])

pedidos = [
    {
        "id": 1,
        "cliente_id": 1,
        "productos_ids": [1],
        "total": 850.5,
        "estado": "pendiente"
    }
]

# GET → sigue protegido (solo login)
@router.get("/pedidos")
def obtener_pedidos(user=Depends(verificar_token)):
    return pedidos


# POST → PUBLICO (sin token)
@router.post("/pedidos")
def agregar_pedido(pedido: Pedido):

    nuevo = pedido.dict()

    if len(pedidos) == 0:
        nuevo["id"] = 1
    else:
        nuevo["id"] = max(p["id"] for p in pedidos) + 1

    pedidos.append(nuevo)

    return {
        "mensaje": "Pedido agregado correctamente",
        "pedido": nuevo
    }


# PUT → protegido
@router.put("/pedidos/{id}")
def actualizar_pedido(
    id: int,
    pedido: Pedido,
    user=Depends(verificar_token)
):

    for i, p in enumerate(pedidos):

        if p["id"] == id:

            pedidos[i] = pedido.dict()
            pedidos[i]["id"] = id

            return {
                "mensaje": "Pedido actualizado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Pedido no encontrado"
    )


# DELETE → protegido
@router.delete("/pedidos/{id}")
def eliminar_pedido(
    id: int,
    user=Depends(verificar_token)
):

    for i, p in enumerate(pedidos):

        if p["id"] == id:

            pedidos.pop(i)

            return {
                "mensaje": "Pedido eliminado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Pedido no encontrado"
    )