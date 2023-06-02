import ref_1

def pick_resistors (resistance: int) -> dict | None:

    """ возвращает словарь с ближайщими значениями номиналов резисторов, либо None, 
    если значение сопротивления за пределами диапазона от 100 до 999 включительно."""    
  
    if 100 < resistance < 999:
            
        result = {}
        
        for k in ref_1.nominals:
            result[k] = tuple(filter(lambda x: abs(x - resistance) == min(map(lambda x: abs(x - resistance), ref_1.nominals[k])), ref_1.nominals[k]))
            
        return result
        

# C:\Users\roman\Desktop\Python\local repository\Nazarov\2023.05.21
# 18:09:09 > python -i 1.py
# >>> pick_resistors(112)
# {'E6': (100,), 'E12': (120,), 'E24': (110,), 'E48': (110,), 'E96': (113,)}
# >>> pick_resistors(549)
# {'E6': (470,), 'E12': (560,), 'E24': (560,), 'E48': (536, 562), 'E96': (549,)}
# >>> print(pick_resistors(54))
# None