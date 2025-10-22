# Розгалудження

# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..

# password = inpyt("Enter password: ")
# pasword = "qwerty"

# password_accept = "QwErTy"
# elif password != password_accept
 
 
# Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.

# name1 = inpyt("Enter name1: ")
# name2 = inpyt("Enter name2: ")

""" if name1 <= name2:
    print (name1, name2)
else 
    print (name2, name1)

if name1 <= name2:
# print (name1, name2)
       name1, name2 = name2, name1
print (name2, name1)
 """

# Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.

namber = int(inpyt("Enter nymber: "))

if number == 1:
     name
  print("One")  
elif number == 2:
    print("Two")
elif number == 3:
    print("Three")
else:
    print("Unknown")
# Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

a = input().lower()
b = input().lower()

if a < b:  
    print(f"{a} before {b}")
elif a > b:
    print(f"{a} after {b}")
else:
    print("Same letters")
   
or

letter1 = inpyt("Enter letter1: "). lover()
letter2 = inpyt("Enter letter2: "). lover()

if letter1 <= letter2:
     print ("First letter:", letter1, "Second letter:", letter2)
     


# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..

temp = int(input())

if temp <= 0:
    print("A cold, isn't it?")
elif temp < 10:
    print("Cool.")
else:  
    print("Nice weather we're having.")
    