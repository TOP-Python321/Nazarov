def countable_nouns(num: int, word_form: tuple[str, str, str]) -> str:

    """ возвращает str, которая соответствует переданному int"""
    
    if 11 <= num % 100 <= 14:
        return word_form[2]
    else:
        digit = num % 10
        if digit == 1:
            return word_form[0]
        elif 2<= digit <= 4:
            return word_form[1]
        else:
            return word_form[2]
            
            
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(21, ("год", "года", "лет"))
# 'год'