# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Введите трехзначное число:", end=" ")
number = int(input())
sum = 0
temp = 0
while number > 0:
    temp = number % 10
    sum = sum + temp
    number= number // 10
print("Сумма цифр введеного числса = ",sum)
