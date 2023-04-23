year = int(input())

# скобки не нужны, потому что у and приоритет выше, чем у or
# КОММЕНТАРИЙ: совершенно верно; впрочем, в отдельных случаях их можно использовать для повышения удобства (а значит и скорости) чтения кода — вы должны сами каждый раз решать, где это оправданно, а где нет =)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('да')
else:
    print('нет')


# 2020
# да

# 1900
# нет
    

# ИТОГ: отлично — 3/3
