cage_one = input()
cage_second = input()

arr = ['a', 'c', 'e', 'g'] 
 
if cage_one[0] in arr:
    num_1 = 0
else:
    num_1 = 1
if cage_second[0] in arr:
    num_2 = 0
else:
    num_2 = 1
 
if (num_1 + int(cage_one[1]) + num_2 + int(cage_second[1])) % 2 == 0:
    print('да')
else:
    print('нет') 


# a1
# e6
# нет

# d3
# f5
# да

# попробовал сделать без использования функции ord(), через объявление списка (list)
# ord() использовал в шестой задаче, всё в тренировочных целях, понятно, что с ord() 
# получилось бы здесь короче, примерно вот так:
# if ((ord(cage_one[0]) + int(cage_one[1])) % 2 == (ord(cage_second[0] + int(cage_second[1])) % 2):
#     print('да')
# else:
#     print('нет')