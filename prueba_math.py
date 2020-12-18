import math, re
 

def lol(n):
    i = 0
    while i < len(n):
        elevado = len(n)    
        numero_primero = int(n) // 10
        print("el primer dijito es " + str(numero_primero))
        numero_segundo = int(n) % 10
        print("el segundo dijito es " + str(numero_segundo))

        resultado = math.pow(numero_segundo, elevado)
        resultado_2 = math.pow(numero_primero, elevado - 1)
        print(resultado + resultado_2)
        i+=1    
        

if __name__ == '__main__':
    lol(input("a "))    