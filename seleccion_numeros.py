def lol():
    sumDigit, extNum = 0, 0

    numEntero = int(input("Ingrese un numero entero: "))
    
    while numEntero != 0:
        extNum = numEntero % 10
        # elegimos el último digito de nuestro numero 
        numEntero //= 10
        # le quitamos el ultimo digito anuestro numero
        print(f"numEntero ahora vale {numEntero}")

        sumDigit += extNum
        # guardamos el ultimo digito en nuestra sumDigit y se suma a esta misma
    print("La suma de los digitos es: {}".format(sumDigit))

if __name__ == "__main__":
    lol()