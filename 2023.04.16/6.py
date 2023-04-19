first_position = input()
second_position = input()

# использовал функцию  ord(), которая возвращает код Юникода заданного символа 
if -1 <= ord(first_position[0]) - ord(second_position[0]) <= 1 and -1 <= int(first_position[1]) - int(second_position[1]) <= 1:
    print('да')
else:
    print('нет')
    
# f4
# f5
# да

# d3
# a7
# нет

