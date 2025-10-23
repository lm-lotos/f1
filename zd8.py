# 8 task

ex = input("Enter ex:\n")
# len_ex = len(ex)  # 5

# n = (len(ex) + 1) // 2 # кількість цифрgi

# 1 variant
# print(int(ex[0]) + (1 if ex[1] == "+" else -1) * int(ex[2]) + (1 if ex[3] == "+" else -1) * int(ex[4]))

# variant
sum = int(ex[0])
for i in range (len(ex)):
    sum += (1 if ex[i] == "+" else -1) * int(ex[i+1])

(ex[1 +1])

print(sum)

# 3 var
sum = int(ex[0])
for i in range(1, len(ex)):
    if i == "+":
        sum += int(ex[i+1])







# ex[::2]

ex.rep

# 4 war
# ex.replace("-", "+")
# map ()

#------------------------
  my_list = ["1", "2", 4, 7]
# for el in range(len(my_list)):
#    my_liste [el] = str(my_list[el])
# print(my_list))

# new_list = list(map(int, my_list))
# print(new_list)
#-----------------------------

ex = ex.replase("-", '+_')
parts = ex.split("+")

# map()
sum_ex = sum(map(int, parts))
print(sum_ex)



