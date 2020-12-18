# A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

# Given a number determine if it special number or not .
# The number passed will be positive (N > 0) .

# All single - digit numbers with in the interval[0:5] 
# are considered as special number.
# Input >> Output Examples
# specialNumber(2) ==> return "Special!!"
# Explanation:
# It's a single-digit number within the interval [0:5] .

# specialNumber(9) ==> return "NOT!!"
# Explanation:
# Although, it's a single-digit number but Outside the interval [0:5] .

# specialNumber(23) ==> return "Special!!"

def specialNumber(n):
    S = {'0', '1', '2', '3', '4', '5'}
    B = set(n)  
    if B.issubset(S):
       print("Special!!")
    else:
        print("NOT!!")


if __name__ == "__main__":
    specialNumber(input("alo -----> "))


#     SPECIAL = set('012345')

# def special_number(number):
#     return "Special!!" if set(str(number)) <= SPECIAL else "NOT!!"