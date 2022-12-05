# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9



import re
import itertools


with open('file5_1.txt', 'w',) as data:
   data.write('2*x^2 + 4*x + 5')
 

with open('file5_2.txt', 'w',) as data:
    data.write('4*x^2 + 1*x + 4')


with open('file5_1.txt','r') as data:
    file5_1 = data.readline()
    list_of_file5_1 = file5_1.split()
print(f'Первый многочлен: {file5_1}')   

with open('file5_2.txt','r') as data:
    file5_2 = data.readline()
    list_of_file5_2 = file5_2.split()
print(f'Второй многочлен: {file5_2}')   

file1 = 'file5_1.txt'
file2 = 'file5_2.txt'
file_sum = 'sum.txt'



def read_pol(file):
    """ Получает данные из файла"""
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol



def convert_pol(pol):
    """ Получает список кортежей каждого (коэффициент, степень)"""
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol



def fold_pols(pol1, pol2):   
    """Получает список кортежей суммы """
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res



def get_sum_pol(pol):
    """ Составляет итоговый многочлен"""
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    """Записывает данные в файл"""
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)


print(f'Результирующий многочлен: {pol_sum}')