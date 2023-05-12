import ref_7 

general_dictionary = {}

for dict in ref_7.list_of_dicts:
    for key, value in dict.items():
        if key not in general_dictionary:
            general_dictionary[key] = {value}
        else:
            general_dictionary[key] = general_dictionary[key] | {value}

print(*{f'{key!r}: {value}' for key, value in general_dictionary.items()}, sep=',\n')

# 'Тула': {2, 3},
# 'Пермь': {9, 3},
# 'Ростов-на-Дону': {5, 6},
# 'Ульяновск': {4, 7},
# 'Махачкала': {5},
# 'Барнаул': {5},
# 'Хабаровск': {7},
# 'Краснодар': {9, 4},
# 'Самара': {2},
# 'Санкт-Петербург': {4, 6},
# 'Ярославль': {9},
# 'Тольятти': {9},
# 'Новосибирск': {7},
# 'Липецк': {1},
# 'Красноярск': {9, 1},
# 'Тюмень': {5},
# 'Москва': {1}