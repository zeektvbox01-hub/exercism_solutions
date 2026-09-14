"""Finds leap years"""

def leap_year(year:int) -> bool:
    """Check if a given year is a leap year
 
    Parameters:
        year: The year to be tested
 
    Returns:
        Is the year a leap year?
 
    """
    return year % 4 == 0 and not year % 100 == 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0
            
    
