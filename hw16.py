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


