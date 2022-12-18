# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли 
# этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def checking_weekends (user_input):
#     user_input = int (user_input)
#     if type(user_input) == int:
#         while (user_input < 1) or (user_input > 7):
#                 print ('incorrect input, please try again')
#                 user_input = int(input())
#         else:
#             if (user_input == 6) or (user_input == 7) :
#                 print ('YES! It\'s the weekend, congratulations! No work today')
#             elif (user_input > 0) and (user_input < 6):
#                 print ('Sorry, this is weekday, you better get back to work')
#     elif type(user_input) == str:
#         print ('Sorry, but you\'re not a winner, run the program again')
#     else:
#         print ('Sorry, but you\'re not a winner, run the program again')


# print ('Input the number of the day in week: ')
# day_week = input()
# if (day_week.isdigit()==True):
#     checking_weekends(day_week)
# else:
#     print ('Sorry, but you\'re not a winner, run the program again')

# Задача 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             print(f'x = {x}, y = {y}, z = {z} ->',not (x or y or z) == (not x and not y and not z))

# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def checking_quarters (x,y):
#     if (x>0) & (y>0):
#         print ('It\'s in the first quarter')
#     elif (x<0) & (y>0):
#         print ('It\'s in the second quarter') 
#     elif (x<0) & (y<0):
#         print ('It\'s in the third quarter')
#     elif (x>0) & (y<0):
#         print ('It\'s in the fouth quarter')
#     elif (x==0) & (y<0):
#         print ('It\'s located on the axis Y between the third and fouth quarter')
#     elif (x>0) & (y==0):
#         print ('It\'s located on the axis X between the first and fouth quarter')
#     elif (x==0) & (y>0):
#         print ('It\'s located on the axis Y between the third and fouth quarter')
#     elif (x<0) & (y==0):
#         print ('It\'s located on the axis X between the second and third quarter')
#     elif (x==0) & (y==0):
#         print ('Sorry, it can\'t be in ZERO. But if you wonder - It\'s in the center of the coordinate system')
#     else:
#         print ('wow')

# print ('Hello, this program let you check the quarters for X and Y values in 2D dimension ')
# print ('Pls, input integer or float values for X:')
# x = float(input())
# print ('Pls, input integer or float values for Y:')
# y = float(input())
# checking_quarters(x,y)

# Задача 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# def checking_quaters_range (quarter):
#     if quarter == 1: 
#         print("In the first quarter x>0 and y>0")
#     elif quarter == 2:
#         print("In the second quarter x<0 and y>0")
#     elif quarter == 3:
#         print("In the third quarter x<0 and y<0")
#     elif quarter == 4:
#         print("In the fouth quarter x>0 and y<0")
#     else:
#         print("There isn't such a quarter")

# print ('Hello, this program let you check which X and Y values in your input quarter ')
# print ('Pls, input integer quarter value (e.g. 1 or 2 or 3 or 4 only) :')
# input_quarter = int (input())
# checking_quaters_range(input_quarter)

# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math #пошел по пути наименьшего сопротивления, хотя можно было просто умножить на 0.5

def distance_between_two_dots (xa, xb, ya, yb):
    return math.sqrt(((xb-xa)**2) + ((yb-ya)**2))

print("Input coordinate xa: ")
xa = float(input()) #тут бы double, конечно
print("Input coordinate xb: ")
xb = float(input())
print("Input coordinate ya: ")
ya = float(input())
print("Input coordinate yb: ")
yb = float(input())
result = distance_between_two_dots (xa,xb,ya,yb)

print(f"The distance between two dots is {round(result, 3)}")


