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

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def checking_quaters (x,y):
    if (x>0) & (y>0):
        print ('It\'s in the first quater')
    elif (x<0) & (y>0):
        print ('It\'s in the second quater') 
    elif (x<0) & (y<0):
        print ('It\'s in the third quater')
    elif (x>0) & (y<0):
        print ('It\'s in the fouth quater')
    elif (x==0) & (y<0):
        print ('It\'s located on the axis Y between the third and fouth quater')
    elif (x>0) & (y==0):
        print ('It\'s located on the axis X between the second and third quater')
    elif (x==0) & (y>0):
        print ('It\'s located on the axis Y between the first and second quater')
    elif (x<0) & (y==0):
        print ('It\'s located on the axis X between the first and third quater')
    elif (x==0) & (y==0):
        print ('Sorry, it can't be in ZERO. Bu if you wonder - it\'s in the center of the coordinate system')
    else:
        print ('wow')

print ('Hello, this program let you check the quaters for X and Y values in 2D dimension ')
print ('Pls, input integer or float values for X:')
x = float(input())
print ('Pls, input integer or float values for Y:')
y = float(input())
checking_quaters(x,y)

