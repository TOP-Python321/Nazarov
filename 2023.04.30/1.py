email = input("Введите адрес электронной почты: ")

if (
    # ИСПРАВИТЬ: много лишних похожих действий выполняете: например, если метод find() для некоторой подстроки возвращает значение > -1, то это означает, что подстрока найдена — а это в свою очередь означает что количество вхождений этой же подстроки в исходную > 0, верно? так нужно ли отдельное выполнение метода count()?
    #  оптимизируйте
    email[0] != '@'
    # исправил - закомментировал, действительно, дополнительный метод count здесь не нужен
    # and email.count('@') > 0
    # and email.count('.') > 0
    and email.rfind('.') > email.find('@') + 1
):
    print("Да")
else:
    print("Нет")


# Введите адрес электронной почты: roman.nazarov@mail
# Нет

# Введите адрес электронной почты: romannazarov@mail.ru
# Да


# ИТОГ: хорошо, но можно лучше — 2/3
