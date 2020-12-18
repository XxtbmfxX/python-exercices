def lel(n):
    last_num= []
    numEntero = int(n)
    while numEntero != 0:
        last_num.append(numEntero % 10)
        # elegimos el último digito de nuestro numero 
        numEntero //= 10
        # le quitamos el ultimo digito anuestro numero
        print(f"numEntero ahora vale {numEntero}")
        
        print(f"ahora tenemos la lista: {last_num}")
        


if __name__ == "__main__":
    lel(input("coloque su numero por favor: "))