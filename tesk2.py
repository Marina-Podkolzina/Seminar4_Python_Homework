#2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#* 6 -> [2,3]
#* 144 -> [2,3]




num = int(input("Введите число: "))
i = 2 
list = []
old = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1

l = [] 

for i in list: 
    if i not in l: 

        l.append(i) 
print(f"Простые множители числа {old}  : {l}")

