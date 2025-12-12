#Задание_1
def upper(t):
    for i in t:
        if i.isupper():
            print(i,'', end='')
upper('Privet')

#Задание_2
def punct(text):
    y = 0
    for i in text:
        if i == '!' or i == '?' or i == '.' or i == ',' or i == '(' or i == ')':
            y += 1
    print(f"\n{y}")

punct('(Как дела?)')

#Задание_3
def create_cube(x, y):
    if x > 0 and y > 0:
        for i in range(y):
            print('*' * x)
    else:
        print("Введите значения заново")

create_cube(5, 3)

#Задание_4
def double(x):
    y = ''
    for i in x:
        y += i * 2
    print(y)

double('строка')

#Задание_5
def Constructor(q, w, e, r):
    a = q // 72
    b = w // 4
    c = e // 2
    d = r // 7

    return min(a,b,c,d)

print(Constructor(144, 8, 4, 14))
print(Constructor(10000, 16, 6, 2))

#Задание_6
z = []

def fun(x, y):
    global z
    for i in range(x+1):
        z.append(y)
    print(z)

fun(5,3)

#Задание_7
def fun(x):
    z = []
    summ = 0
    for i in x:
        if isinstance(i, int):
            z.append(i)
    for i in z:
        if i // 7:
            summ += i
    if summ < 83:
        p = True
    else:
        p = False
    print("сумма: ", summ)
    print(p)

fun([7, 10.5, 'txt', 14, 2, 56])

#Задание_8
def square(x, y):
    for i in range(1, x + 1):
        row = ([f"|{j}|" for j in range(1, y + 1)])
        print(row)

square(2,3)
