# multiplicar sin signo multiplicativo
#MULT es el numero a sumar b es la cantidad de veces
#le sumo MULT a mi resultado n veces
def multiplicar(a, b):
    MULT = int(a)
    resultado = 0
    for n in range(int(b)):
        resultado += MULT
    print(f'su resultado es {resultado}')


if __name__ == "__main__":
    multiplicar(input("multiplicando "), input("multiplicador "))