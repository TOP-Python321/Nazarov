def numbers_strip(sample: list, n = 1, copy = False) -> list:

    """ возвращает исходный объект списка с внесёнными изменениями или изменённую копию """
    
    for _ in range(n):
        sample.remove(min(sample))
        sample.remove(max(sample))
    if copy:
        return sample.copy()
    else:
        return sample
        
    
# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False    
        
     
        