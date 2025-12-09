"""
A Python module to calculate Easter date for any given year.
"""

from datetime import date, timedelta # import date and timedelta from datetime module to convert to Gregorian calendar to be compatible with the Gregorian calendar.

def easter(year, calendar = True):
    """
    This calculates the date of Easter for a given year. Based on Gaussian Computus Algorithm.
    
    Args:
        year (int): The year to calculate the Easter date for.
        calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar).
    
    Returns:
        tuple: The date of Easter for the given year (not converted to Gregorian calendar).
    """
    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (13 + 8 * k) // 25
    q = k // 4
    m = (15 + k - p - q) % 30 if calendar and year > 1582 else 15
    n = (4 + k - q) % 7 if calendar and year > 1582 else 6
    # Note: If calendar but year <= 1582, then the date is calculated using the Julian calendar.
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    if d == 29 or (d == 28 and a > 10): # Edge cases corrections for Gregorian epact.
        d -= 1
    march = 22 + d + e
    april = d + e - 9
    if march > 31: # If march value exceeds 31, then Easter is in April.
        return (april, 4) 
    else: return (march, 3)
    
def easterdate(year, calendar = True):
    """
    This converts the nominal date of Easter for a given year to the Gregorian calendar. Since datetime module only supports Gregorian calendar, we need to convert the nominal date of Easter to the Gregorian calendar.
    
    Args:
        year (int): The year to convert the nominal date of Easter to.
        calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar but Julian Easter if before 1583).
    
    Returns:
        date: The nominal date of Easter for the given year in the Gregorian calendar.
    """
    if not (0 < year < 10000): raise ValueError("Year must be between 1 and 9999")
    # Gregorian-Julian day difference correction.
    d = year // 100 - year // 400 - 2 if not (calendar and year > 1582) else 0
    day, month = easter(year, calendar)
    return date(year, month, day) + timedelta(d) # Add the correction to the date.

if __name__ == "__main__":
    print(easter(2025, True))
    print(easter(2025, False))
    print(easterdate(2025, True))
    print(easterdate(2025, False))