def auto(n):
    x = n**2
    if x < 100:        
        num = x % 10
        
    elif x < 1000:
        num = x % 100
        
    elif x < 100000:
        num = x % 1000
        
    elif n < 100000:
        num = x % 1000
        
    if int(num) == n:
        print("Automorphic")
    else:
        print("Not!!")    
if __name__ == "__main__":
    auto(int(input("coloque un nuero por favor ")))
    #versión más correcta usando .endwith()
    #def automorphic(n):
    #return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"