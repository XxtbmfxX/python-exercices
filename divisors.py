# Create a function named divisors/Divisors
# that takes an integer n > 1 and returns an array
# with all of the integer's divisors(except for 1 and the number itself), 
# from smallest to largest. If the number is prime return the string '(integer) 
# is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def divisors(n):
    resultado = []
    
    for i in range(2, n):
        if n % i == 0:
            resultado.append(i)
    if len(resultado) > 1:
        print(resultado)
    else:
        print(f"{n} is prime")
        
if __name__ == "__main__":
    divisors(int(input("coloque un numero por favor ")))


    # def divisors(num):
    # l = [a for a in range(2,num) if num%a == 0]
    # if len(l) == 0:
    #     return str(num) + " is prime"
    # return l