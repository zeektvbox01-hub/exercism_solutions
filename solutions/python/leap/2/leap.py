"Finds leap years "

def leap_year(year):
    "No docstring avalible"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
            
    
