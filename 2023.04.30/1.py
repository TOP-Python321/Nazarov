email = input("Введите адрес электронной почты: ")

if email[0] != '@' \
    and email.count('.') > 0 \
    and email.rfind('.') > email.find('@'):
    print("Да")
else:
    print("Нет")
    
# Введите адрес электронной почты: roman.nazarov@mail
# Нет
# Введите адрес электронной почты: romannazarov@mail.ru
# Да
