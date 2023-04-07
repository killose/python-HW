# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
#     001001 -> yes

# ticket = input()
# sum = 0

# for i in range(0, len(ticket)):
#     sum += int(ticket[i])
#     print(sum)
    
# if sum % 2 == 0: 
#     print("yes") 
# else:     
#     print("no")

number = input("Введите номер билета: ")
sum_of_first_three = int(number[0]) + int(number[1]) + int(number[2])
sum_of_last_three = int(number[3]) + int(number[4]) + int(number[5])
if sum_of_first_three == sum_of_last_three:
    print("yes")
else:
    print("no")