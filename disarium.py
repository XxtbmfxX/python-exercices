# The idea is to fist count digits in given numbers. 
# Once we have count, we traverse all digits from right most 
# (using % operator), raise its power to digit count and decrement the digit count.

import math    
# Method to check whether a number is disarium or not 
def check(n):
    count_digits = len(number)        
    print(count_digits)
    sum = 0  
    number = n 
    while (number!=0) :   
        rest = number % 10           
        sum = sum + math.pow(rest, count_digits)
        count_digits -= 1
        number /=10         
    if sum == number : 
        return 1
    else : 
        return 0        

  
if __name__ == "__main__":
    sas = check(input("coloque su numerito por favor "))
        # Driver method 
    if (sas == 1) : 
        print ("Disarium Number")
    else : 
        print ("Not a Disarium Number")