def add_numbers(start, end):
    b = 0
    for number in range(start, end+1):
        b= b+ number
    return b
test1 = add_numbers(1,2)
print(test1)
test2 = add_numbers(1, 100)
print(test2)
test3 = add_numbers(1000, 5000)
print(test3)
caleb = add_numbers(333, 777)
print(caleb)
    
