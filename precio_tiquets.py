#"SI" si tengo cambio suficiente para el voleto "NO" si no
#El cabio es la suma de los voletos pagados en la queue
#los voletos valen 25 dolarucos
#comprobar que la tengo cambio para el siguiente comprador

def cola(fila):
    lista = []
    for i in fila:
        lista.append(i)
    print (type(lista))
   

datos = input("coloque su fila por favor ")

if __name__ == "__main__":
    cola(datos)