binary_number = input("Введите двоичное число: ")
# if set(binary_number) <= {"1", "0", "b"}:
    # КОММЕНТАРИЙ: ох, накрутили проверок... есть такой эмпирический способ оптимизации кода: каждый раз когда у вас возникает третий подряд уровень вложенности условий (and — это те же вложенные условия), задавайте себе вопрос: "точно-точно-точно нельзя проще?" — в 95–97% случаев окажется, что можно =)
    # if binary_number == "0b" or binary_number == "b":
        # print("Нет")
    # elif (
            # set(binary_number[2:]) <= {"1", "0"}
        # and {binary_number[:2]} != {"1b"}
        # and {binary_number[:2]} != {"bb"}
    # ):
        # print("Да")
    # else:
        # print("Нет")
# else:
    # print("Нет")

# ИСПОЛЬЗОВАТЬ: пожалуй, я просто оставлю здесь более короткий вариант, а вы его сами осмыслите и прокомментируете во время работы над ошибками:
answer = 'нет'
if set(binary_number[2:]) <= {'0', '1'}:
    if binary_number[:2] in {'01', '10', 'b1', 'b0', '0b', '11', '00', '1', '0'}:
        answer = 'да'
print(answer)

# Да, много навернулось проверок, изначально и думали над таким вариантом. Сейчас ещё добавил '11', '00', '1', '0', потому что это тоже двоичные числа.
# Сбил тот факт, что слишком большое множество предполагалось к проверке на вхождение в [:2]. Вручную десять вариантов вписать. 

# Введите двоичное число: 0b010100101
# Да

# Введите двоичное число: 1b10101100101001
# Нет

# Введите двоичное число: 1
# Да

# Введите двоичное число: 0
# Да

# Введите двоичное число: 10101001001010
# Да

# Введите двоичное число: b1010101010
# Да

# Введите двоичное число: b
# Нет

# Введите двоичное число: 1b101001010
# Нет

    
# ИТОГ: хорошо, но можно лучше — 2/3
