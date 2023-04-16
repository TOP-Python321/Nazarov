number = int(input())

# КОММЕНТАРИЙ: цифра — digit, число — number, num

# Переписал наименования переменных для тренировки. Должен отметить, что с самого начала была мысль
# использовать digit, но подумал, что редко раньше такое имя переменной встречал. 
# Очевидно, что мало профессионального кода видел )))


first_digit = number // 100
second_digit = (number - first_digit*100) // 10
third_digit = number % 10

sum_of_digits = first_digit + second_digit + third_digit
# КОММЕНТАРИЙ: произведение — product, факториал — factorial
product = first_digit * second_digit * third_digit

print(f'Сумма цифр = {sum_of_digits} \n'
      f'Произведение цифр = {product}')

# first_num = number // 100
# second_num = (number - first_num*100) // 10
# third_num = number % 10

# sum_of_num = first_num + second_num + third_num
# КОММЕНТАРИЙ: произведение — product, факториал — factorial
# factorial = first_num * second_num * third_num

# print(f'Сумма цифр = {sum_of_num} \n'
      # f'Произведение цифр = {factorial}')

# Сумма цифр = 15
# Произведение цифр = 125


# ИТОГ: отлично — 4/4
