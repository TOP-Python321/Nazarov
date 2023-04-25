# divisible = int(input())
# divisor = int(input())

# СДЕЛАТЬ: подумайте и перепишите код так, чтобы обойтись только одним блоком if

# if divisible % divisor == 0:
    # print(f'{divisible} делится на {divisor} нацело \n'
          # КОММЕНТАРИЙ: круглые скобки не нужны, их можно опустить
          # f'частное: {(divisible // divisor)}')
# else:
    # print(f'{divisible} не делится на {divisor} нацело \n'
          # f'неполное частное: {divisible // divisor} \n'
          # ИСПРАВИТЬ: вы уже вычисляли остаток, а здесь повторно выполняете ту же операцию — неоптимально
          # f'остаток: {divisible % divisor}')


# 8 делится на 2 нацело
# частное: 4

# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1


# ИТОГ: хорошо — 2/3

# Переписал полностью, с одним блоком if и двумя новыми переменными, позволяющими сократить количество вычилений

divisible = int(input())
divisor = int(input())
res_of_div = int(divisible // divisor)
remainder = int(divisible % divisor)

answer = (f'{divisible} делится на {divisor} нацело \n' 
          f'частное: {res_of_div}')   
 
if remainder:
    answer = (f'{divisible} не делится на {divisor} нацело \n' 
             f'неполное частное: {res_of_div} \n'
             f'остаток: {remainder}')

print(answer)

# 50 делится на 5 нацело
# частное: 10

# 7 не делится на 3 нацело
# неполное частное: 2
# остаток: 1
