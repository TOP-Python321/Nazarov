# ввод без текста приглашения пользователю, согласно условиям задачи
num = int(input())

# КОММЕНТАРИЙ: объявление данных переменных можно считать избыточным, если принять во внимание простоту используемых выражений выражений и то, что в дальнейшем каждая из переменных используется только единожды
# Убрал лишние "сущности" )) старый вариант закомментировал
# num_next = num + 1
# num_prev = num - 1

# print("Следующее за числом", num, "число:", num_next, "\nДля числа", num, "предыдущее число:", num_prev)
# вариант с f-строкой
# ИСПОЛЬЗОВАТЬ: альтернативный вариант записи строковых литералов в несколько строчек (только внутри скобок)
# print(f'Следующее за числом {num} число: {num_next} \n'
     #f'Для числа {num} предыдущее число: {num_prev}')
     
print(f'Следующее за числом {num} число: {num+1} \n'
      f'Для числа {num} предыдущее число: {num-1}')


# Следующее за числом 20 число: 21
# Для числа 20 предыдущее число: 19


# КОММЕНТАРИЙ: PEP 8 рекомендует отделять пробелом символ # от последующего текста комментарий — команда Вкл./Выкл. комментарий в большинстве редакторов так и делает


# ИТОГ: отлично — 3/3
