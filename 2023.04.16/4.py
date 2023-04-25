# КОММЕНТАРИЙ: клетка (для животных) — cage; клетка (часть разметки, ячейка) — cell; клетка (игрового поля) — square, field, cell
# КОММЕНТАРИЙ: один (количественное числительное) — one; первый (порядковое числ.) — first; два (кол. числ.) — two; второй (пор. числ.) — second

# Заменил имена переменных на рекомендованные. По поводу cage - меня сбил google переводчик, 
# ввел туда "шахматная клетка" в поиске дополнительного синонима через алгоритмы переводчика,
# в это время свой мозг выключился, понадеявшись на ИИ )))). Конечно же field или square здесь подходят.
# и конечно же, cage это металлическая клетка, видимо, ИИ предположил запереть в ней шахматные фигуры или доску )))

square_first = input()
square_second = input()

# КОММЕНТАРИЙ: здесь подойдёт odd_verticals (нечётные_вертикали)
odd_verticals = ['a', 'c', 'e', 'g'] 

# if square_first[0] in odd_verticals:
    # num_1 = 0
# else:
    # num_1 = 1

# if square_second[0] in odd_verticals:
    # num_2 = 0
# else:
    # num_2 = 1

# ИСПОЛЬЗОВАТЬ: а ещё можно вспомнить про преобразование типов:
# num_1 = int(cage_one[0] not in arr)
# num_2 = int(cage_second[0] not in arr)

# Использовал рекомендованное, действительно, здорово получилось: булевы значения с приведением к int заменили аж две ветки if-else
num_1 = int(square_first[0] not in odd_verticals)
num_2 = int(square_second[0] not in odd_verticals)

if (num_1 + int(square_first[1]) + num_2 + int(square_second[1])) % 2 == 0:
    print('да')
else:
    print('нет')


# a1
# e6
# нет

# d3
# f5
# да


# попробовал сделать без использования функции ord(), через объявление списка (list)
# ord() использовал в шестой задаче, всё в тренировочных целях, понятно, что с ord()
# получилось бы здесь короче, примерно вот так:
# if ((ord(square_one[0]) + int(square_one[1])) % 2 == (ord(square_second[0] + int(square_second[1])) % 2):
#     print('да')
# else:
#     print('нет')
# КОММЕНТАРИЙ: очень хорошо, что ищете различные решения — продолжайте в том же духе


# ИТОГ: отлично — 6/6
