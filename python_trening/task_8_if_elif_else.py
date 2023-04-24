num_float = -5

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('ноль')
else:
    print('число отрицательное')

num = 6
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


num = - 300

if num > 100:
    print('-')
if num < -100:
    print('+')

