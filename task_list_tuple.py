# # 1.Створіть список на основі введеної послідовності цілих чисел і надрукуйте другу половину списку. Якщо кількість не парна, то вивести більшу кількість.
# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))
# print(value_list[len(value_list)//2:])

# ----------------------------------------------------
# # 2.Створіть список на основі введеної послідовності цілих чисел і надрукуйте його елементи таким чином: два останні елементи переміщені з кінця в початок списку без зміни їх початкового порядку.

# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))
# v_l2 = value_list[:-2]
# v_l1 = value_list[-2:]
# result = v_l1 + v_l2
# print(result)

# ---------
# v_list = value_list[-2:]
# print(v_list)
# v_list.extend(v_l2)
# print(v_list)

# --------------------------------------------------
# # 3.Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.

# # варіан 1: 

# languages = "Ukrainian French Bulgarian Norwegian Latvian"

# list_lang = languages.split()
# print(list_lang)

# sorted_list = sorted(list_lang)
# print(" ".join(sorted_list))

# # ----------------
# # 2 варіант:

# # пояснення ДЛЯ СЕБЕ, як працює програма:

# # input().split() зчитує рядок і розбиває його на елементи списку за пробілом.

# # # Початковий порядок зберігається (тобто без автоматичного сортування).

# # Метод .sort() сортує список за алфавітом.

# # ' '.join(languages) виводить елементи списку в одному рядку через пробіл.


# # користувач вводить назви мов через пробіл:

# # languages = input("Введіть назви мов через пробіл: ").split()

# # список зберігається у тому порядку, в якому введено

# # print("Початковий список:", languages)

# # сортуємо список в алфавітному порядку

# # languages.sort()

# # виводимо відсортований список в один рядок через пробіл:

# # print("Відсортований список:", ' '.join(languages))

# # перевага: оригінальний список не змінюється.
# # sorted() зручно використовувати, коли треба зберегти два варіанти — вихідний і відсортований.


# # -------------
# # 3 аріант:

# # введення назв мов:

# languages = input("Введіть назви мов через пробіл: ").split()

# # вивід початкового списку:

# print("Початковий список:", languages)

# # сортування за допомогою sorted()

# sorted_languages = sorted(languages)

# # відсортований список:

# print("Відсортований список:", ' '.join(sorted_languages))


# # -------------
# # варіант 4 : Сортування без вбудованих методів (власний алгоритм)

# # можна, наприклад, написати сортування бульбашкою (bubble sort)

# languages = input("Введіть назви мов через пробіл: ").split()

# print("Початковий список:", languages)


# # --------------
# # варіант 5: сортування бульбашкою
# for i in range(len(languages) - 1):
#     for j in range(len(languages) - i - 1):
#         if languages[j] > languages[j + 1]:
#             languages[j], languages[j + 1] = languages[j + 1], languages[j]

# print("Відсортований список:", ' '.join(languages))

# # перевага: показує розуміння принципу сортування.
# # недолік: неефективний для великих списків, але гарний для навчання.


# # ----------
# # варіант 6: сортування з урахуванням регістру (без чутливості до великих/малих літер)

# languages = input("Введіть назви мов через пробіл: ").split()

# print("Початковий список:", languages)

# # Сортуємо, ігноруючи регістр
# languages = sorted(languages, key=str.lower)

# print("Відсортований список:", ' '.join(languages))

# #  “Англійська” і “англійська” будуть поряд, і не розділені великими літерами.

# # ----------------------------------------------------

# # 4.Виведіть елементи списку в зворотному порядку, не змінюючи сам список.

# languages = input("Enter language names separated by space: ").split()

# print("Initial list:", languages)

# print("Reversed list:", ' '.join(languages[::-1]))

# # пояснення:
# [::-1] створює копію списку у зворотному порядку, не змінюючи сам languages.

# # -------
# # варіант 2 (через зріз):

# languages = input("Enter language names separated by space: ").split()

# print("Initial list:", languages)
# print("Reversed list:", ' '.join(languages[::-1]))

# # --------
# #  варіант 3 (через функцію reversed()):

# languages = input("Enter language names separated by space: ").split()

# print("Initial list:", languages)
# print("Reversed list:", ' '.join(reversed(languages)))

# # пояснення:

# # Обидва працюють однаково.
# # Різниця тільки в тому, що [::-1] створює копію списку,
# # а reversed() повертає ітератор — тобто трохи економніший за пам’яттю.

# #  ---------------------------------------------------

# # 5.Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

# numbers = input("Enter numbers separated by space: ").split()

# # Вивести елементи з парними індексами (0, 2, 4, ...)
# print("Elements with even indexes:", ' '.join(numbers[::2]))

# # пояснення:------
# # Якщо числа потрібні саме як числа (а не рядки), то краще одразу перетворити:

# # numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# # print("Elements with even indexes:", *numbers[::2])


# # --------------
# # варіан 2 з циклом   for ----

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# print("Elements with even indexes:", end=" ")

# for i in range(0, len(numbers), 2):
#     print(numbers[i], end=" ")

# # поястення тут:--------

# range(0, len(numbers), 2) бере індекси 0, 2, 4, 6, ...

# numbers[i] — це елемент із парним індексом.

# end=" " дозволяє виводити все в один рядок через пробіл.



# # ------------------------------------------------------
# # 6.Визначте, скільки різних слів у введеному рядку.

# Вхідні дані:

# New Delhi New York Paris Prague Reykjavik
# Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend
# Вихідні дані:

# 6
# 19

# #1 варіант----------

# text = "New Delhi New York Paris Prague Reykjavik"

# text = text.split()

# new_text = [] # New Delhi

# for word in text^
#     print(word)

# for word_i in range(len(text))
#     # print(word_i)
#     if word not in new_text:
#         new_text = append(word)
# print(len(new_text))
    
# # 2 варіан -----------

# result = len(text)

# [0, 1, 2, 3, 4, 5, 6]

# for word_i in range(len(text)):
#     print("/n")
#     print(word_i, end=" ")
#     print("/n")
#     for i in range(word_1 + 1, len (text)):
#         # print(word_i, end=" ")
#         if text[word_i] == text[i]
#             continue
#         else:

#         print(text[word_i])
#         print(text[i])
#         result += 1
#         result -= 1

# result_finall = result + 1
# print(result_finall)

# # 3 варіант----------

# text = "New Delhi New York Paris Prague Reykjavik"

# text = text.split()

# print(len(text))



# # ----------------------------------------------------------
# # 7.Напишіть програму, яка приймає послідовність чисел, розділених комами, від користувача і створює список і кортеж з цими числами.

# Вхідні дані:

# 7, 9, 12, 4
# Вихідні дані:

# [7, 9, 12, 4]
# (7, 9, 12, 4)

# # варіан 1:--------------
# numbers = input("Enter numbers separated by commas: ").split(',')

# # перетворюємо кожен елемент у число
# numbers = [int(num.strip()) for num in numbers]

# # створюємо кортеж
# numbers_tuple = tuple(numbers)

# print(numbers)
# print(numbers_tuple)

# # пояснення:------------
# .split(',') розбиває введений рядок за комами,

# .strip() прибирає пробіли після ком,

# [int(...)] переводить елементи у числа,

# tuple() створює кортеж із того самого списку.

# # Результат:

# Enter numbers separated by commas: 7, 9, 12, 4  
# [7, 9, 12, 4]  
# (7, 9, 12, 4)



# # -------------------------------------------
# # 8.Напишіть програму для отримання частини рядка URL, що позначає назву ресурсу.

# Вхідні дані:

# https://www.namesite.com/folder/index.html
# Вихідні дані:

# index.html
# Middle level


# # рішення:----------

# url = input("Enter URL: ")

# # Розділяємо URL за символом '/'
# parts = url.split('/')

# # Беремо останній елемент — назву ресурсу
# resource_name = parts[-1]

# print(resource_name)

# # пояснення:-------------
# # Якщо треба ще вивести “Middle level” — тобто назву папки перед файлом (folder у моєму прикладі), можна додати:

# url = input("Enter URL: ")

# parts = url.split('/')

# resource_name = parts[-1]
# middle_level = parts[-2]

# print(resource_name)
# print(middle_level)
# # ----------
# Введення:
# https://www.namesite.com/folder/index.html

# Вивід:
# index.html
# folder



# # -------------------------------------------------
# # 9.Для введеної послідовності унікальних цілих чисел, поміняйте місцями мінімальний та максимальний елементи цієї послідовності. Надрукуйте отриманий список.

# def set_numbers(numbers):
#     # знаходимо мінімальне і максимальне значення
#     min_value = min(numbers)
#     max_value = max(numbers)

#     # знаходимо їхні індекси
#     min_index = numbers.index(min_value)
#     max_index = numbers.index(max_value)

#     # міняємо місцями
#     numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

#     return numbers


# numbers = list(map(int, input("Enter unique integers separated by space: ").split()))
# print(set_numbers(numbers)) 


# # або:------------
# numbers = list(map(int, input("Enter unique integers separated by space: ").split()))

# min_value = min(numbers)
# max_value = max(numbers)

# min_index = numbers.index(min_value)
# max_index = numbers.index(max_value)

# numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# print(numbers)


# # Приклад:---------------
# Enter unique integers separated by space: 1 2 3 6 8 4 9 3 22 67 87

# Результат:

# [87, 2, 3, 6, 8, 4, 9, 3, 22, 67, 1]



# # ------------------------------------------
# # 10.lines = []

# while True:
#     line = input("Enter text: ")
#     if line == "":
#         break
#     lines.append(line.upper())

# for el in lines:
#     print(el)

# # пояснення:------
# Вводимо:
# python
# ruby
# go

# Результат:
# PYTHON
# RUBY



# # ---------------------------------------------------
# # 11.У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.

# Вхідні дані:

# 1 -2 -3 5 6 -3 7 8
# Вихідні дані:

# -2 -3
# 5 6
# 7 8

# #-----

# numbers = [1, -2, -3, 5, 6, -3, 7, 8, -4]

# for i in range(len(numbers) - 1):
#     if numbers[i] * numbers[i + 1] > 0:
#         print(numbers[i], numbers[i + 1])

        

# # --------------------------------------------------
# # 12.Напишіть програму для обчислення добутку цілих чисел (без використання циклу for), які вводяться через пропуск користувачем в одному рядку.

# Вхідні дані:

# 2 5 3
# Вихідні дані:

# 30

# # 1 рішення без циклу:-------------
# from math import prod

# numbers = list(map(int, input("Enter integers separated by space: ").split()))
# print(prod(numbers))

# # або------
# from functools import reduce
# import operator

# numbers = list(map(int, input("Enter integers separated by space: ").split()))
# print(reduce(operator.mul, numbers))

# # Приклад:-------------
# Enter integers separated by space: 2 5 3

# Результат:
# 30

# # 2 рішення з циклом:---------
# numbers = list(map(int, input("Enter integers separated by space: ").split()))

# product = 1
# for n in numbers:
#     product *= n

# print(product)

# # Приклад:-----------
# Enter integers separated by space: 2 5 3

# Результат:
# 30

# # пояснення:----------
# product = 1 — початкове значення,
# product *= n — множимо кожне наступне число на попередній результат.


# # ------------------------------------------------------------------
# # 13.Напишіть програму для друку елементів певного цілочисельного списку після видалення з нього парних чисел. Значення списку вводяться через пропуск в одному рядку.

# Вхідні дані:

# 3 44 6 8 9 12 7
# Вихідні дані:

# [3, 9, 7]

# # варіант 1:--------------
#  numbers = list(map(int, input("Enter integers separated by space: ").split()))

# # Видаляємо парні числа
# numbers = [n for n in numbers if n % 2 != 0]

# print(numbers)



# # -------------------------------------------------------------------------
# # 14.Напишіть програму, яка приймає послідовність 4-цифрових двійкових чисел, розділених комами, і друкує числа, які ділиться на 5 без остачі, в рядку і розділені комами.

# Вхідні дані:

# 0100,0011,1010,1001,1100
# Вихідні дані:

# 1010

# # рішення:--------------
# # вводимо двійкові числа через кому
# binary_numbers = input("Enter 4-digit binary numbers separated by commas: ").split(',')

# # відбираємо ті, що діляться на 5 без остачі
# divisible_by_5 = [b for b in binary_numbers if int(b, 2) % 5 == 0]

# # виводимо через кому
# print(','.join(divisible_by_5))

# # --------------------

# # Введення:
# # 0100,0011,1010,1001,1100

# # Вивід:
# # 1010

# # Пояснення:
# # int(b, 2) переводить двійкове число у десяткове,
# # % 5 == 0 перевіряє, чи ділиться на 5.

# # 15.Ви вирішили написати перетворювач коду на Python в код на Java. Так як на Java прийнятий стандарт найменування CamelCase, то ви вирішили навчитися перетворювати імена з underscore в цей формат. Стиль underscore характеризується тим, що слова в імені пишуться маленькими літерами і розділяються між собою символом підкреслення _. Стиль CamelCase означає, що кожне слово пишеться з великої літери і роздільників між словами немає. Отже, вводиться один рядок, що містить ім’я, записане в форматі underscore. Програма виводить рядок, що містить ім’я в форматі CamelCase.

# Вхідні дані:

# my_class
# c
# Вихідні дані:

# MyClass
# C


# # -------------------------------------------------------------------
# # 16.Напишіть програму для видалення кожного третього елемента із цілочисельного списку і друку результуючого списку, доки список не стане порожнім. Початковий список цілих чисел вводиться в одному рядку через пропуск.

# Вхідні дані:

# 2 5 8 9 4 78 7 1
# Вихідні дані:

# [2, 5, 9, 4, 78, 7, 1]
# [2, 5, 4, 78, 7, 1]
# [2, 5, 78, 7, 1]
# [2, 5, 7, 1]
# [2, 5, 1]
# [2, 5]
# [5]
# []

# numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# while len(numbers) > 0:
#     if len(numbers) > 2:           # якщо є хоча б 3 елементи
#         numbers.pop(2)             # видаляємо третій елемент (індекс 2)
#     else:
#         numbers.pop(-1)            # якщо залишилось менше трьох — видаляємо останній
#     print(numbers)

# # варіант 2:----------

# numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# while numbers:
#     numbers.pop(2 if len(numbers) > 2 else -1)
#     print(numbers)

# # пояснення:------------
# while numbers: — цикл крутиться, доки список не стане порожнім.
# pop(2 if len(numbers) > 2 else -1) — якщо у списку є хоча б 3 елементи, прибирає третій (індекс 2); інакше прибирає останній.
# після кожного видалення — друк поточного списку.

# # варіант 3:---------------
# numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# while len(numbers) > 0:
#     if len(numbers) > 2:
#         numbers.pop(2)   # видаляє третій елемент
#     else:
#         numbers.pop()    # якщо залишилося менше трьох, просто видаляє останній
#     print(numbers)

# # по порядку пояснення:----------
# користувач вводить числа, наприклад 2 5 8 9 4 78 7 1
# цикл while крутиться, доки список не спорожніє
# .pop(2) прибирає кожен третій елемент
# коли менше трьох елементів — просто добиває їх до кінця



# # --------------------------------------------------------
# # # користувач вводить розміри
# n, m = map(int, input("Введіть n і m через пробіл: ").split())

# result = []  # тут збиратимемо всі рядки

# for row in range(n):  # ідемо по рядках
#     m_list = []       # тимчасовий список для одного рядка
#     for col in range(m):  # ідемо по стовпчиках
#         if (row + col) % 2 == 0:
#             m_list.append(".")   # парна сума → крапка
#         else:
#             m_list.append("*")   # непарна сума → зірочка
#     result.append(m_list)

# # тепер виведемо красиво
# for row in result:
#     print(" ".join(row))

# # поясненн:------------
# n, m = map(int, input().split()) — читає, наприклад, 6 8
# зовнішній for row — створює кожен рядок
# внутрішній for col — додає символи в рядок
# (row + col) % 2 визначає, що ставити:
# парне → "."
# непарне → "*"
# result.append(m_list) — додає готовий рядок у таблицю
# потім проходимось по result і виводимо рядок за рядком.



# # --------------------------------------------------------------------
# # 18.У рядку через кому перераховані слова. Сформувати з цих слів новий рядок. Слова мають бути відсортовані за спаданням (від Z до A) без урахування регістру і записані через пропуск.

# Вхідні дані:

# horse, cat, parrot, goldfish, dog
# Вихідні дані:

# parrot horse goldfish dog cat


# # Варіант 1
# text = "horse, cat, parrot, goldfish, dog"
# text_list = text.split(", ")
# text_list.sort(key=str.lower, reverse=True)

# print(text_list)
# print(" ".join(text_list))

# # ---------------------------

# # Варіант 2
# text = "horse, cat, parrot, goldfish, dog"
# text_list = text.split(", ")
# text_list = [w.strip() for w in text_list]

# text_list.sort(key=str.lower, reverse=True)

# print(text_list)
# print(" ".join(text_list))

# # тепер з кортежем:---------------
# # Варіант 1
# text = "horse, cat, parrot, goldfish, dog"
# text_list = text.split(", ")
# text_list.sort(key=str.lower, reverse=True)

# print(text_list)
# print(" ".join(text_list))
# print(tuple(text_list))  # додаємо вивід кортежу

# # ---------------------------

# # Варіант 2
# text = "horse, cat, parrot, goldfish, dog"
# text_list = text.split(", ")
# text_list = [w.strip() for w in text_list]

# text_list.sort(key=str.lower, reverse=True)

# print(text_list)
# print(" ".join(text_list))
# print(tuple(text_list))  # додаємо вивід кортежу



# # ------------------------------------------------------------------------
# # 19.Напишіть програму, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5... (число повторюється стільки разів, чому дорівнює). На вхід програми передається невід’ємне ціле число n - стільки елементів послідовності повинна надрукувати програма. На виході очікується послідовність чисел, записаних через пропуск в один рядок.

# Вхідні дані:

# 8
# Вихідні дані:

# 1 2 2 3 3 3 4 4

# # рішення:----------

# n = int(input("Введіть число n: "))

# sequence = []  # створюємо порожній список

# for i in range(1, n + 1):
#     for j in range(i):
#         sequence.append(i)
#         if len(sequence) == n:
#             break
#     if len(sequence) == n:
#         break

# print(*sequence)

# # приклад:--------------
# Приклад:

# Введіть число n: 8
# 1 2 2 3 3 3 4 4


# # -------------------------------------------------------------------------
# # 20.Використовуючи поняття списку, напишіть програму, яка створює 3D масив елементів a x b x c, кожен з яких має значення 0. Значення a, b, c вводяться в одному рядку через пропуск.

# Вхідні дані:

# 3 3 2
# 4 4 4
# Вихідні дані:

# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]
# [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

# # рішення: -----------------
# a, b, c = map(int, input("Введіть a, b, c через пробіл: ").split())

# array_3d = []  # створюємо порожній список

# for i in range(a):  # перший рівень
#     layer = []
#     for j in range(b):  # другий рівень
#         row = [0] * c  # третій рівень (рядок із нулів)
#         layer.append(row)
#     array_3d.append(layer)

# print(array_3d)

# # Приклад 1:-------------
# Введіть a, b, c через пробіл: 3 3 2
# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

# # Приклад 2:--------------
# Введіть a, b, c через пробіл: 4 4 4
# [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
#  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
#  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
#  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]


# # варіан ще:-------------
# a, b, c = map(int, input("Введіть a, b, c через пробіл: ").split())
# array_3d = [[[0 for _ in range(c)] for _ in range(b)] for _ in range(a)]
# print(array_3d)

# # Приклад:----------------
# Введіть a, b, c через пробіл: 3 3 2
# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]



# # ------------------------------------------------------------------
# # 21.В один ряд поставили n кеглів, пронумерувавши їх зліва направо числами від 1 до n. Потім в цей ряд кинули k куль, при цьому i-та куля збила всі кеглі з номерами від m до h включно. Визначте, які кеглі залишилися стояти на місці. Програма отримує на вхід кількість кеглів n і кількість кидків k. Далі йде k пар чисел m, h, при цьому 1 ≤ m ≤ h ≤ n ≤ 100. Програма повинна вивести послідовність з n символів, де j-й символ є I, якщо j-та кегля залишилася стояти, або ., якщо j-та кегля була збита.

# Вхідні дані:

# 10 3
# 8 10
# 2 5
# 3 6
# Вихідні дані:

# I.....I...

# # рішення:-------------

# n, k = map(int, input("Введіть n і k: ").split())

# pins = ["I"] * n  # спочатку всі кеглі стоять

# for i in range(k):
#     m, h = map(int, input(f"Введіть діапазон {i + 1}: ").split())
#     for j in range(m - 1, h):  # знімаємо кеглі з m по h включно
#         pins[j] = "."

# print("".join(pins))

# # Приклад роботи:--------------
# Введіть n і k: 10 3
# Введіть діапазон 1: 8 10
# Введіть діапазон 2: 2 5
# Введіть діапазон 3: 3 6
# I.....I...