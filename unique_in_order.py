#si el caracter aparece de nuevo depues de uno mayor a este, se debe agregar no sumar a uno anterior
#try rxcept?
def unique(n):
    result = []
    anterior = None
     
    for i in n:
        if i != anterior:
            result.append(i)
        anterior = i
    print(result)    

if __name__ == "__main__":
    unique(list(input("coloque un conjunto alfanumerico por favor ")))