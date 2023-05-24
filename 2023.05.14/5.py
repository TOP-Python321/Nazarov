def central_tendency(num1: float, num2: float, / , *numbers: float) -> dict[str, float]:
    
    """возвращает словарь: ключи - меры центральной тенденции, а значения вычислены из заданных аргументов"""

    numbers = sorted((num1, num2) + numbers)
    middle_index = len(numbers) // 2
    arithmetic = sum(numbers) / len(numbers)
    multi = 1
    numerator_sum= 0
    
    if len(numbers) % 2:
        median = float(numbers[middle_index])
    else:
        median = sum(numbers[middle_index - 1 : middle_index + 1]) / 2
        
    for i in numbers:       
        multi *= i 
        numerator_sum += 1 / i
        geometric = multi ** (1 / len(numbers))
        harmonic = len(numbers) / numerator_sum
    
    dict_tendency = {
                'median': median,
                'arithmetic': arithmetic,
                'geometric': geometric,
                'harmonic': harmonic
                }
                
    return dict_tendency
    
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>>
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>>