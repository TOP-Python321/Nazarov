names_cin = sorted(input('Введите имена файлов: ').split('; '))
original_names = {}
names_cout = []

for i in names_cin:
    original_names[i] = original_names.get(i, 0) + 1
    # КОММЕНТАРИЙ: хорошо, что в один цикл пошли
    if original_names[i] == 1:
        names_cout.append(i)        
    else:
        # ИСПРАВИТЬ: метод index() вызывается лишний раз — оптимизируйте
        names_cout.append(i[:i.index('.')] + '_' + str(original_names[i]) + i[i.index('.'):])
        
print(*names_cout, sep='\n')


# Введите имена файлов: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz


# ИТОГ: очень хорошо, требуется немного доработать — 4/5
