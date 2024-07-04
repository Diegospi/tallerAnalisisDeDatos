from generators.generadorProducto import generarDatosProductos
import pandas as pd

def analizarDatos():
    datos=generarDatosProductos()
    tabla=pd.DataFrame(datos,columns=["producto","categoria"])
    tabla.to_csv("./data/tipoProducto.csv",index=False)
analizarDatos()