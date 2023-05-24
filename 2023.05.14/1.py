def strong_password(password) -> bool:

    """ Возвращает булевое значение True or False в зависимости
        от соответствия введенного пароля заданным условиям """
    
    upper_letter = {chr(code) for code in range(65, 91)}
    lower_letter = {chr(code) for code in range(97, 123)}
    digits = {chr(code) for code in range(48, 58)}
    
    if (len(password) >= 8 and
       set(password) & upper_letter and
       set(password) & lower_letter and
       set(password) - (set(password) & (upper_letter | lower_letter | digits)) and
       len([i for i in password if i in digits]) >= 2
       ):
        return True
        
    return False
        
# >>> strong_password("Rdgh!fy25")
# True
# >>> strong_password("pass")
# False