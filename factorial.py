#factorial
# def fac(n):
#   a=1
#   for i in range(1, n+1):
#       a *= i#
#   return(a)
#  


def strong_num(n):   
    print(n)
    total=1
    for i in range(1, n+1):
       total *= i
       #de 1 a n
    print(total)
      


if __name__ == "__main__":
    strong_num(abs(int(input("coloque un numero entero por favorsito "))))