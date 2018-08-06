c = 0
for number in range(1, 100 + 1):
    print(number)
    c = c+number
print(c)    

def add_numbers(c):
    for number in range(1, 100 + 1):
        print(number)
        c = c + number
    return(c)

answer = add_numbers(0)
print(answer)

def add_numbers2(start, end):
    c = 0
    for number in range(start, end):
        c = c + nuumber
    return(c)
test1 = add_numbers2(1,2)
print(test1)

    
    
