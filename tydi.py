def lel(n):
    # de atras para adelante podemos usar esto <lista.reverse()>
    num= []
    numEntero = int(n)
    while numEntero != 0:
        num.append(numEntero % 10)
        numEntero //= 10
    num.reverse()
    if num[0] < num[1]:
        print(f"ta bien{num}")
    else:
        print(f"ta mal {num}")    
        
if __name__ == "__main__":
    lel(input("coloque su numero por favor: "))