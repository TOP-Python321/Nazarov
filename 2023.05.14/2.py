def taxi_cost(dist: int, wait_time = 0) -> int | None:

    """ возвращает стоимость поездки или None, если вычисление невозможно """
    
    price_start = 80
    price_dist = dist * 6 // 150
    price_wait_time = wait_time * 3
    cancel = 80
    
    price = price_start + price_dist + price_wait_time
    
    if dist == 0:
        price = price_start + price_wait_time + cancel
    elif dist < 0:
        price = None

    return(price)
    

# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None

 
    