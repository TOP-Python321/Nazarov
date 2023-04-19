year = int(input())

# скобки не нужны, потому что у and приоритет выше, чем у or
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:

    print ('да')
    
else:

    print ('нет')
    
# 2020
# да

# 1900
# нет
    

    