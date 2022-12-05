#4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.(записать в строку)

# Пример:

# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5


import random




def write_file(str):
    """ Открывает файл для записи """
    with open('file4.txt', 'w') as data:
        data.write(str)


def coefficient():
    """ Coздаёт случайные числа от 0 до 100 """
    return random.randint(0,101)


def create_polynomials(k):
    """Создаёт коэффициенты многочлена"""
    list = [coefficient() for i in range(k+1)]
    return list


    
    
def create_str(sp):
    """ Создаёт многочлен в виде строки """
    list= sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i+1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Задайте натуральную степень k = "))
koef = create_polynomials(k)
write_file(create_str(koef))
