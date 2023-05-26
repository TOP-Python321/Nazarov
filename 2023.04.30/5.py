import ref_5

word = input('Введите слово: ').upper().replace('Ё', 'Е')

scores = 0

print(sum(
    # ИСПРАВИТЬ: в генераторном выражении значение scores на каждой итерации будет равно нулю
    # КОММЕНТАРИЙ: а если подразумевается, что значение scores будет меняться, то это двойная ошибка: 1) int объекты являются неизменяемыми; 2) если бы были изменяемыми и вы бы как-то прописали это изменение на каждой итерации, то каждое число, возвращаемое генератором во время итерации, содержало бы сумму всех предыдущих очков и очки за очередную букву — а потом все эти числа вы ещё снаружи суммируете функцией sum() — итог вышел бы сильно больше ожидаемого числа
    scores + key
    for i in word for key, value in ref_5.scores_letters.items()
    if i in value
    # СДЕЛАТЬ: напишите генераторную функцию, эквивалентную данному генераторному выражению, и поэкспериментируйте с разными способами суммирования
))


# Введите слово: синхрофазатрон
# 29

# Введите слово: ёлочная игрушка
# 32

# Введите слово: ёлка
# 6


# ИТОГ: почти хорошо, но требует осмысления — 4/6
