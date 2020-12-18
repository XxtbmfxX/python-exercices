# to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 
# 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns an integer

"""separar numeros, elevarlos, juntarlos
indices"""

def square(n):
    resultado = ''
    for d in range(len(n)):
        resultado += str(int(n[d])** 2)
        
    #|---------puedo recorrer un string?----------|
    #|for x in str(num):                          |  
    #|     ret += str(int(x)**2)                  |
    #|--------------------------------------------| 
    print(resultado)    


if __name__ == "__main__":
    square(input("coloque su numero por favor "))

#forma mas corta:
# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))