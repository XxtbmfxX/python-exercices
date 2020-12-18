def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")      
        elif i % 3 == 0 :
            print("fizz") 
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
if __name__ == "__main__":
    fizzbuzz(int(input("colque un numerito por favor ")))            
    
    # for i in range(1,101):
    # fizz = 'Fizz' if i%3==0 else ''
    # buzz = 'Buzz' if i%5==0 else ''
    # print(f'{fizz}{buzz}' or i)         
    # -------------------------__-_______-___________-_____--__
    # print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')
