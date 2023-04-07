# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input()
sum = 0
for i in range(0, len(number)):
    sum += int(number[i])
print(sum)