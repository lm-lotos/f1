def countdown(n):
    if n == 0
        print("Start!")
    else:

    print(n)
    countdown(n -1)  # n -= 1 
    # countdown(n)


    # ----------- порахувати і вивести

    # це перехресний виклик

    def sum_numbers(a, b): 
        return a + b
    

    def multi(n):
        return sum_numbers(a, b) ** 2
    
    
# print(sqr(2, 7)) # це рекурсія

#-----------------------

# 5 + 4
# 5+1 + 4 _1 = 6 + 3
#7 + 2 
# 8 + 1
# 9 + 0
    def add_number(a, b):
        if b == 0:
            return a
        return helper( a + 1, b - 1)
    
    def helper(a, b):
        if b ==0:
            return a
        return add_number(a + 1, b - 1)
    
    print(add_number(5, 4))

# 13 --------------
# def task13()


# 7 + 5
# 7 (+1) + 5 (-1)

# 7 + (-5)
# 7 (+1) + (-5) (+1) -> 6 + (-4)

b ==0 -> a
b > 0 -> (a + 1, d - 1)
b > 0 -> (a - 1, d + 1)

def add_number(a, b):
    if b == 0
    elif b > 0:
        return add_number(a + 1, b - 1)
    else: # b < 0
        return add_number(add_number(a - 1, b + 1))
#-----------

# 14
# вводяться значення
# while True:
#     n = int(input("Enter mumber: "))
#     if n == 0:
#         break

def print_number():
    n = int(input("Enter mumber: "))
    if n == 0:
       return
    else:
        print_number()
    print(n)
   
print_number()

# 2-----

def print_number_str():
    n = int(input("Enter mumber: "))
    if n == 0:
       return
    else:
        print_number_str()
    print(n)
   


