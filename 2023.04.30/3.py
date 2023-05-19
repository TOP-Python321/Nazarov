inp_int_1 = input("Введите числа через пробел: ").split()
inp_int_2 = input("Введите числа через пробел: ").split()

answer = 'Нет'
list_1, list_2 = [int(i) for i in inp_int_1], [int(i) for i in inp_int_2]

if not list_2:
    answer = 'Да'
else:
    for i in range(len(list_1)):

        for k in list_1:

            if list_1[i] == k and list_2 == list_1[i:i + len(list_2)]:
                answer = 'Да'
                break

print(answer)

# Введите числа через пробел: 3 4 5 6 7 78
# Введите числа через пробел: 7 78
# Да

# Введите числа через пробел: 314 1234 2342 3 3 2 7
# Введите числа через пробел: 5 43 3 2 2
# Нет