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
#Задание_2
str1 = input()
str2 = input()
if str1 == str2:
  print("True")
else:
  print("False")
#Задание_3
def check_color():
    try:
        r = int(input("Введите значение R (0-255): "))
        g = int(input("Введите значение G (0-255): "))
        b = int(input("Введите значение B (0-255): "))

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Некорректное значение (вне диапазона 0-255)")
            return

        if r == 0 and g == 0 and b == 0:
            print("Чёрный цвет")
        elif r == 255 and g == 255 and b == 255:
            print("Белый цвет")
        elif r == 255 and g == 0 and b == 0:
            print("Красный цвет")
        elif g == 255 and r == 0 and b == 0:
            print("Зелёный цвет")
        elif b == 255 and r == 0 and g == 0:
            print("Синий цвет")
        else:
            print("Нет цвета")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа.")
check_color()
#Задание_1/Вариант_3
num = int(input("Введите число: "))
if num > 0:
    print(f"Результат: {num - 1}, {num}, {num + 1}")
else:
    num = 1
    print(f"Результат: {num - 1}, {num}, {num + 1}")
#Задание_2
filename = input("Введите имя файла с расширением (например, 'file.doc'): ")
extension = filename.split('.')[-1].lower()

if extension == 'doc':
    print("Word file")
elif extension == 'py':
    print("Python file")
elif extension == 'txt':
    print("Text file")
else:
    print(f"Неизвестное расширение файла: {extension}")
#Задание_3
try:
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    c = float(input("Введите длину стороны C: "))
except ValueError:
    print("Ошибка: введите корректные числовые значения для сторон.")
    exit()

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Треугольник равносторонний (все стороны равны).")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный (две стороны равны).")
    else:
        print("Треугольник разносторонний (все стороны разные).")

else:
    print("Треугольник с заданными сторонами не существует (нарушено правило суммы сторон).")
#Задание_1/Вариант_4
text = 'important information in one line'
letter = input("Введите букву: ")

if letter in text:
    print(True)
else:
    print(False)
#Задание_2
try:
    side1 = float(input("Введите длину первой стороны: "))
    side2 = float(input("Введите длину второй стороны: "))
except ValueError:
    print("Ошибка: введите корректные числовые значения для сторон.")
    exit()
if side1 <= 0 or side2 <= 0:
    print("Ошибка: длины сторон должны быть положительными числами.")
    exit()
if side1 == side2:
    figure_type = "Квадрат"
    area = side1 * side2
    print(f"{figure_type}. Площадь: {area}")
else:
    figure_type = "Прямоугольник"
    area = side1 * side2
    print(f"{figure_type}. Площадь: {area}")
#Задание_3
def check_mood(response):  
    positive = ['хорошо', 'нормально', 'отлично']     
    negative = ['плохо', 'не хорошо']   
    response = response.lower()  
    if response in positive:  
        return '😊'  
    elif response in negative:  
        return '🙁'  
    else:  
        return '😐'
user_response = input("Как твои дела? ")  
print(check_mood(user_response))  
#Задание_1/Вариант_5
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:

    result = num1 ** num2
    print(f"Первое число больше. Результат: {result}")
elif num2 > num1:

    result = num2 ** num1
    print(f"Второе число больше. Результат: {result}")
else:
    result = num1 + num2
    print(f"Числа равны. Сумма: {result}")
#Задание_2
new_message = "Hello! How are you?"


user_answer = input("Введите ваш ответ на сообщение 'Hello! How are you?': ")

if len(new_message) > 0 and len(user_answer) > 0:
    if new_message[0] == user_answer[0]:
        print(True)
    else:
        print(False)
else:
    print(False) 
#Задание_3
try:
    length1 = float(input("Введите длину первого отрезка: "))
    length2 = float(input("Введите длину второго отрезка: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()

if length1 > length2:
    difference = length1 - length2
    print(f"Первый отрезок длиннее второго на **{difference}**.")
elif length2 > length1:
    difference = length2 - length1
    print(f"Второй отрезок длиннее первого на **{difference}**.")
else:
    print("Отрезки **равны**.")
Задание_1/Вариант_6
input_string = input("Введите произвольную строку: ")

if len(input_string) > 0:

    first_char = input_string[0]
    last_char = input_string[-1]

    if first_char == last_char:
        print(True)
    else:
        print(False)
else:

    print(False)
#Задание_2
try:
    number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Введено не целое число.")
    exit()
result = 0
if number % 2 == 0:
    result = number ** 2
    print(f"Число кратно двум. Результат (число в квадрате): {result}")
elif number % 3 == 0:
    result = number ** 3
    print(f"Число кратно трём. Результат (число в кубе): {result}")
else:
    result = number * 100
    print(f"Число не кратно ни двум, ни трём. Результат (число * 100): {result}")
#Задание_3
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()
if num1 < 0 and num2 < 0:
    print(False)
elif num1 >= 0 and num2 >= 0:
    print(True)
elif num1 < 0:
    num1 += 1000
    print(f"Первое число было отрицательным. Результат: num1 = {num1}, num2 = {num2}")
elif num2 < 0:
    num2 += 1000 
    print(f"Второе число было отрицательным. Результат: num1 = {num1}, num2 = {num2}")
#Задание_1/Вариант_7
input_string = input("Введите произвольную строку: ")
target_chars = ['я', 'и', 'е', 'ю']
if len(input_string) > 0:
    last_char = input_string[-1]
    if last_char in target_chars:
        print(True)
    else:
        print(False)
else:
    print(False)
#Задание_2
try:
    a = float(input("Введите длину первой стороны (a): "))
    b = float(input("Введите длину второй стороны (b): "))
    c = float(input("Введите длину третьей стороны (c): "))
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
    exit()
if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print(True)
    else:
        print(False)
else:
    print(False)
#Задание_3
try:
    number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Введено не целое число.")
    exit()
last_digit = abs(number) % 10
result = None

print(f"Последняя цифра числа: {last_digit}")
if last_digit == 0:
    result = number ** 10
    print(f"Результат (число в степени 10): {result}")
elif last_digit == 1:
    result = number % 3
    print(f"Результат (деление на 3 с остатком): {result}")
elif last_digit == 2:
    result = number // 2
    print(f"Результат (деление на 2 без остатка): {result}")
else:
    result = number ** 2
    print(f"Результат (число в степени 2): {result}")
#Задание_1/Вариант_8
def check_password(password):  
    if len(password) < 8 or password == 'qwerty123':  
        return False  
    return True  
password = input("Введите пароль:")  
print(check_password(password))  
#Задание_2
pc_number = 777
try:
    user_num1 = float(input("Введите первое число: "))
    user_num2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()
condition1 = (user_num1 < pc_number) and (user_num2 > pc_number)
condition2 = (user_num2 < pc_number) and (user_num1 > pc_number)
if condition1 or condition2:
    print(True)
else:
    print(False)
#Задание_3
lamp_1 = 0
lamp_2 = 0
user_choice = input("Какую лампочку зажечь? (Введите '1' или '2'): ")
if user_choice == "1":
    lamp_1 = 1
    print(f"Лампочка 1 зажжена. Статус: lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
elif user_choice == "2":
    lamp_2 = 1
    print(f"Лампочка 2 зажжена. Статус: lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
else:
    print("Обе лампочки не горят")
    print(f"Статус: lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
#Задание_1/Вариант_9
switch_1 = False
switch_2 = False
user_input = input("Включить? ")
if user_input.lower() == "да":
    switch_1 = True
    switch_2 = True
    print("Всё включено")
    print(f"switch_1 = {switch_1}")
    print(f"switch_2 = {switch_2}")
else:
    print(f"switch_1 = {switch_1}")
    print(f"switch_2 = {switch_2}")
#Задание_2
try:
    number = int(input("Введите целое число: "))
    if number > 0:
        if number % 2 == 0:
            print(True, "even")
        else:
            print(True, "odd")
    else:
        print(False)
except ValueError:
    print("Ошибка ввода: введено не целое число.")
#Задание_3
input_string = input("Введите строку: ")
if input_string:
    if input_string[0] == '/':
        print("command")
    else:
        print("It’s string")
else:
    print("Была введена пустая строка. Это строка.")
#Задание_1/Вариант_10
input_string = input("Введите строку: ")
string_length = len(input_string)
if string_length == 0:
    print(None)
elif string_length <= 5:
    print("short")
elif 6 <= string_length <= 10:
    print("normal")
else:
    print("long")
#Задание_2
try:
    number = int(input("Введите целое число: "))
    if number < 0:
        number = 1_000_000
        print(f"Число было отрицательным. Новое значение: {number}")
    elif number == 0:
        number = 2 ** 2 
        print(f"Число было равно нулю. Новое значение (2^2): {number}")
    else:
        number = number ** 3
        print(f"Число было положительным. Новое значение (в степени 3): {number}")
except ValueError:
    print("Ошибка ввода: введено не целое число.")
#Задание_3
number_1 = 10
number_2 = 100
try:
    user_number = int(input("Введите целое число: "))
    if number_1 < user_number < number_2:
        print(True)
    else:
        print(False)
except ValueError:
    print(False)
