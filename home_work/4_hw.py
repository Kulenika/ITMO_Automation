#ЗАДАЧА 1

class Rectangle:   # ПРЯМОУГОЛЬНИК
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def s(self):
        return self.width * self.length
    def p(self):
        return 2 * (self.width + self.length)

print('Вычислим площадь прямоугольника')
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))
figure = Rectangle(a, b)
print("Ответ:", figure.s())
print('\n')

print('Вычислим периметр прямоугольника')
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))
figure = Rectangle(a, b)
print("Ответ:", figure.p())
print('\n')

class Triangle:   # ТРЕУГОЛЬНИК
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def s1(self):
        return (self.base * self.height) // 2   # Площадь треугольника

print('Вычислим площадь треугольника')
a = float(input("Введите основание треугольника: "))
b = float(input("Введите высоту треугольника: "))
figure1 = Triangle(a, b)
print("Ответ:", figure1.s1())
print('\n')

class Triangle:
    def __init__(self, a, base, c):
        self.a = a
        self.base = base
        self.c = c

    def p1(self):
        return self.a + self.base + self.c  #ПЕРИМЕТР
print('Вычислим периметр треугольника')
a = float(input("Введите первую сторону треугольника: "))
b = float(input("Введите вторую сторону треугольника: "))
c = float(input("Введите третью сторону треугольника: "))
figure1 = Triangle(a, b, c)
print("Ответ:", figure1.p1())
print('\n')

class Trapeze:      # ТРАПЕЦИЯ
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def p3(self):    # ПЕРИМЕТР
        return self.a + self.b + self.c + self.d
print('Вычислим периметр трапеции. Введите длины 4-х сторон: ')
a = float(input("Первая сторона: "))
b = float(input("Вторая сторона: "))
c = float(input("Третья сторона: "))
d = float(input('Четвертая сторона: '))
figure3 = Trapeze(a, b, c, d)
print("Ответ:", figure3.p3())
print('\n')

class Trapeze:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def s3(self):  # ПЛОЩАДЬ
        return ((self.a + self.b) // 2) * self.h
print('Вычислим площадь трапеции. Введите длины оснований и высоты: ')
a = float(input("Основание1: "))
b = float(input("Основание2: "))
c = float(input("Высота: "))

figure3 = Trapeze(a, b, c)
print("Ответ:", figure3.s3())
print('\n')


class Circle:  # КРУГ
    def __init__(self, r, pi=3.14):
        self.pi = pi
        self.r = r
    def s4(self):  # ПЛОЩАДЬ
        return self.pi * (self.r ** 2)
    def p4(self):  # ОКРУЖНОСТЬ
        return 2 * self.pi * self.r
print('Вычислим площадь круга: ')
a = float(input("Введите длину радиуса: "))
figure4 = Circle(a)
print("Ответ:", figure4.s4())
print('\n')
print('Вычислим длину окружности: ')
a = float(input("Введите длину радиуса: "))
figure4 = Circle(a)
print("Ответ:", figure4.p4())
print('\n')


# ЗАДАЧА 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b   # сложение
    def multiplication(self):
        return self.a * self.b   # умножение
    def division(self):
        return self.a // self.b   # деление
    def subtraction(self):
        return self.a - self.b   # вычитание

print('Сложение чисел')
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
result1 = Math(a, b)
print('Результат: ', result1.addition())
print('\n')
print('Умножение чисел')
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
result2 = Math(a, b)
print('Результат: ', result2.multiplication())
print('\n')
print('Деление чисел')
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
result3 = Math(a, b)
print('Результат: ', result3.division())
print('\n')
print('Вычитание чисел')
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
result3 = Math(a, b)
print('Результат: ', result3.subtraction())
print('\n')

# ЗАДАЧА 3
class Button:
    type: str = 'Кнопка'
    text = None
    loc = None

Button1 = Button()
Button1.text = 'Elements'
Button2 = Button()
Button2.text = 'Forms'
Button3 = Button()
Button3.text = 'Alerts'
Button4 = Button()
Button4.text = 'Widgets'
Button5 = Button()
Button5.text = 'Interaction'
Button6 = Button()
Button6.text = 'Bookstore'

    def __init__(self, link):
        self.link = link

    def click(self):
        return 'клик по кнопке'- {}".format(self.link")

