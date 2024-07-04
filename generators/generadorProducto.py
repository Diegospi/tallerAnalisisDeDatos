import random

def generarDatosProductos():
    productos=["Musica","TV","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]
    for producto in productos:
        tipoProducto={}
        categoria=random.choice(["Plus","Mega","Basic"])
        tipoProducto=[producto,categoria]
        datos.append(tipoProducto)
    return datos

print(generarDatosProductos())
