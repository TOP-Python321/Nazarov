import time
start_time = time.time()

n = int(input())
 
last_value = int('9'*n)
first_value = (last_value + 1)//10

print(f'Количество простых чисел {n}-й разрядности:')
counter = 0
for number in range(first_value, last_value + 1): 
    if number > 1:
        # ИСПРАВИТЬ: вот здесь нужно было использовать алгоритм нахождения делителей из прошлой задачи: такой производительности как в решете Эратосфена или Аткина не получили бы, но в 4–5 раз тоже неплохо, 6 разрядов за 10–15 с обсчитывает — а здесь у вас куча итераций лишних с проверками на каждой: ясно дело, будет тормозить
        for div in range(2, number):
            # ИСПОЛЬЗОВАТЬ: круглые скобки не нужны
            if number % div == 0:
                break 
        else: 
            counter += 1

print(counter)
# ИСПРАВИТЬ: ох и древность вы откопали... я зачем вам f-строки показывал? закопайте %s-тюардессу обратно и больше не доставайте
print("--- %s seconds ---" % (time.time() - start_time))

# 3
# Количество простых чисел 3-й разрядности:
# 143


# -----------------------------------------------------------------------
# Помимо стандартного решения данной задачи, существуют различные способы,
# основанные по большей части на математических формулах, позволяющих значительно
# ускорить процесс обработки, за счет выборочного прохождения по range.
# Ниже приведен пример через "решето Аткина": 

# import time
# start_time = time.time()

# is_prime = list()
# limit = int(input('Введите конечное число диапазона: '))
    
# is_prime = [False] * (limit + 1)
# counter = 0
# for x in range(1, int(limit**0.5)+1):
    # for y in range(1, int(limit**0.5)+1):
        # n = 4 * x**2 + y**2
        # if n<=limit and (n%12==1 or n%12==5):
            # is_prime[n] = not is_prime[n]
        # n = 3 * x**2 + y**2
        # if n<= limit and n%12==7:
            # is_prime[n] = not is_prime[n]
        # n = 3 * x**2 - y**2
        # if x>y and n<=limit and n%12==11:
            # is_prime[n] = not is_prime[n]

# for n in range(5, int(limit**0.5)):
    # if is_prime[n]:
        # for k in range(n**2, limit+1, n**2):
            # is_prime[k] = False
# counter += 2 

# for n in range(5, limit):
#     if is_prime[n]:
#         counter += 1

# print(counter)
# print("--- %s seconds ---" % (time.time() - start_time))

# Введите конечное число диапазона: 999999
# 78498


# Счетчик я прикрутил, от библиотеки math избавился,
# но вот с установкой нижней границы диапазона возникли 
# сложности из-за математической формулы.

# Считает, конечно, очень быстро


# ИТОГ: отлично — 5/6
