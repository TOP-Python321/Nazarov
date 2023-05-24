def orth_triangle(cathetus1:float=0, cathetus2:float=0, hypotenuse:float=0) -> float:

    """ вычисляет третью сторону прямоугольного треугольника по двум переданным """
    
    if cathetus1 and cathetus2:        
        hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
        return hypotenuse
    elif hypotenuse and cathetus1 and hypotenuse > cathetus1:
        cathetus2 = (hypotenuse ** 2 - cathetus1) ** 0.5
        return cathetus2
    elif hypotenuse and cathetus2 and hypotenuse > cathetus2:
        cathetus2 = (hypotenuse ** 2 - cathetus2) ** 0.5
        return cathetus1
    else:
        return None
        
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.69041575982343
# >>> orth_triangle(cathetus1=4, hypotenuse=5)
# 4.58257569495584
# >>> orth_triangle(cathetus1=3, hypotenuse=5.987)
# 5.730983248972204 
    
        
        