number = int(input())

# КОММЕНТАРИЙ: цифра — digit, число — number, num
first_num = number // 100
second_num = (number - first_num*100) // 10
third_num = number % 10

sum_of_num = first_num + second_num + third_num
# КОММЕНТАРИЙ: произведение — product, факториал — factorial
factorial = first_num * second_num * third_num

print(f'Сумма цифр = {sum_of_num} \n'
      f'Произведение цифр = {factorial}')

# Сумма цифр = 15
# Произведение цифр = 125


# ИТОГ: отлично — 4/4
