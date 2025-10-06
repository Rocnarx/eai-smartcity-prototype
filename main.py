from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API REST de Prueba - Smart City")

class Pedido(BaseModel):
    cliente: str
    valor: float

class Mensaje(BaseModel):
    destino: str
    contenido: str

@app.get("/api/status")
def get_status():
    return {"status": "ok", "message": "Servidor en línea 🚀"}

@app.post("/api/tienda")
def recibir_pedido(pedido: Pedido):
    return {"message": "Pedido recibido correctamente", "data": pedido.dict()}

@app.post("/api/mensajeria")
def enviar_mensaje(mensaje: Mensaje):
    return {"message": f"Mensaje enviado a {mensaje.destino}", "contenido": mensaje.contenido}
