number = int (input())

first_num = number // 100
second_num = (number - first_num*100)//10
third_num = number % 10

sum_of_num = first_num + second_num + third_num
factorial = first_num * second_num * third_num

print (f'Сумма цифр = {sum_of_num} \nПроизведение цифр = {factorial}')

# Сумма цифр = 15
# Произведение цифр = 125