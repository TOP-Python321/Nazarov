number_of_ticket = input('Введите номер билета: ')

if sum(int(digit) for digit in (number_of_ticket[:3])) == sum(int(digit) for digit in (number_of_ticket[3:])):
    print('Да')
else:
    print('Нет')
    
# Введите номер билета: 123321
# Да

# Введите номер билета: 555777
# Нет