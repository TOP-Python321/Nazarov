divisible = int(input())
divisor = int(input())

if divisible % divisor == 0:
    print(f'{divisible} делится на {divisor} нацело \n'
          f'частное: {(divisible // divisor)}')
          
else:
    print(f'{divisible} не делится на {divisor} нацело \n'
          f'неполное частное: {divisible // divisor} \n'
          f'остаток: {divisible % divisor}')
          

# 8 делится на 2 нацело
# частное: 4

# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1