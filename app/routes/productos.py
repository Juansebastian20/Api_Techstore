from fastapi import APIRouter, HTTPException, Depends
from app.security.auth import verificar_token
from app.models.producto import Producto

router = APIRouter(tags=["Productos"])

productos = [
    {
        "id": 1,
        "nombre": "Laptop HP",
        "descripcion": "Laptop para oficina",
        "precio": 850.5,
        "stock": 5
    },
    {
        "id": 2,
        "nombre": "Mouse Logitech",
        "descripcion": "Mouse inalámbrico",
        "precio": 25.0,
        "stock": 20
    }
]

# GET
@router.get("/productos")
def obtener_productos(user=Depends(verificar_token)):
    return productos

# POST
@router.post("/productos")
def agregar_producto(producto: Producto, user=Depends(verificar_token)):

    nuevo = producto.dict()

    if len(productos) == 0:
        nuevo["id"] = 1
    else:
        nuevo["id"] = max(p["id"] for p in productos) + 1

    productos.append(nuevo)

    return {
        "mensaje": "Producto agregado correctamente"
    }

# PUT
@router.put("/productos/{id}")
def actualizar_producto(
    id: int,
    producto: Producto,
    user=Depends(verificar_token)
):

    for i, p in enumerate(productos):

        if p["id"] == id:

            productos[i] = producto.dict()
            productos[i]["id"] = id

            return {
                "mensaje": "Producto actualizado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )

# DELETE
@router.delete("/productos/{id}")
def eliminar_producto(
    id: int,
    user=Depends(verificar_token)
):

    for i, p in enumerate(productos):

        if p["id"] == id:

            productos.pop(i)

            return {
                "mensaje": "Producto eliminado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )