def automorphic():
    numbers = '1 2 3 4 5 6 7 8'
    nums = {'evens': [], 'odds': []}

    for number in numbers.split(' '):
       if int(number) % 2:
           nums['odds'].append(number)
       else:
           nums['evens'].append(number)
    print(nums)

if __name__ == "__main__":
    automorphic()
    