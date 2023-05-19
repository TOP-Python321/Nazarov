import ref_5

word = input('Введите слово: ').upper().replace('Ё', 'Е')

scores = 0

print(sum(scores + key for i in word for key, value in ref_5.scores_letters.items() if i in value))

# Введите слово: синхрофазатрон
# 29

# Введите слово: ёлочная игрушка
# 32

# Введите слово: ёлка
# 6