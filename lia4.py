#Задание_1/Вариант_1
num = int(input("Введите целое число: "))
if num < 0:
    result = -num
elif num == 0:
    result = 1
else:
    result = num
print (result)

#Задание_2
text = input("Введите число: ")
if "." in text or "," in text:
    print(True)
else:
    print(True)

#Задание_3
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
count = 0
if num1 % 3 == 0:
    count += 1
if num2 % 3 == 0:
    count += 1

if count == 2:
    print(True)
elif count == 1:
    print("Одно число делится на 3")
else:
    print(False)

#Задание_1/Вариант_2
num = int(input("Введите число: "))
if num > 100:
    print("*")
elif num > 0:
    print("*" * num)
else:
    print("Звездочки не выводятся")
