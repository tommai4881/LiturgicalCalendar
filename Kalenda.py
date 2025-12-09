"""
A python module to print the text of the Proclamation of the Nativity of the Lord (from Roman Martyrology) to be read on Midnight Mass.
"""

def ChristmasMoon(year) -> int:
    """
    Calculating the moon of Christmas Day. Based on Knuthian Computus Algorithm.
    
    Args:
        year (int): The year to calculate the moon of Christmas Day for.
    
    Returns:
        int: The moon of Christmas Day.
    """
    golden_number = year % 19 + 1
    epact1582 = (11 * golden_number - 10) % 30
    if year >= 1582:
        century = year // 100 + 1
        solar_correction = (3 * century) // 4 - 12
        lunar_correction = (8 * century + 5) // 25 - 5
        epact = (epact1582 - solar_correction + lunar_correction) % 30
    else:
        epact = (epact1582 + 7) % 30
    moon = (epact + 4) % 30 + 1
    if epact == 25 and golden_number > 11: moon -= 1
    return moon

def OrdinalMoon(moon) -> str:
    """
    This function returns the ordinal of a given moon.
    
    Args:
        moon (int): The moon to calculate the ordinal for.
    
    Returns:
        str: The ordinal of the moon.
    """
    if moon == 1: return "first"
    elif moon == 2: return "second"
    elif moon == 3: return "third"
    elif moon == 4: return "fourth"
    elif moon == 5: return "fifth"
    elif moon == 6: return "sixth"
    elif moon == 7: return "seventh"
    elif moon == 8: return "eighth"
    elif moon == 9: return "ninth"
    elif moon == 10: return "tenth"
    elif moon == 11: return "eleventh"
    elif moon == 12: return "twelfth"
    elif moon == 13: return "thirteenth"
    elif moon == 14: return "fourteenth"
    elif moon == 15: return "fifteenth"
    elif moon == 16: return "sixteenth"
    elif moon == 17: return "seventeenth"
    elif moon == 18: return "eighteenth"
    elif moon == 19: return "nineteenth"
    elif moon == 20: return "twentieth"
    elif moon == 21: return "twenty-first"
    elif moon == 22: return "twenty-second"
    elif moon == 23: return "twenty-third"
    elif moon == 24: return "twenty-fourth"
    elif moon == 25: return "twenty-fifth"
    elif moon == 26: return "twenty-sixth"
    elif moon == 27: return "twenty-seventh"
    elif moon == 28: return "twenty-eighth"
    elif moon == 29: return "twenty-ninth"
    elif moon == 30: return "thirtieth"
    else: return "unknown" # If the moon is not between 1 and 30, return "unknown".
    
class Kalenda:
    """
    This class prints the text of the Proclamation of the Nativity of the Lord (from Roman Martyrology) to be read on Midnight Mass.
    """
    def __init__(self, year):
        """
        This method initializes the Kalenda class.
        """
        self.year = year
        self.moon = ChristmasMoon(self.year)
        self.ordinal_moon = OrdinalMoon(self.moon)
    def Proclamation(self):
        """
        This property prints the text of the Proclamation of the Nativity of the Lord (from Roman Martyrology) to be read on Midnight Mass.
        """
        print(f"THE Eighth Kalends of January, the {self.ordinal_moon} day of the moon.") # The Eighth Kalends of January means December 25.
        print(f"In the year 5199 since the world was created,")
        print(f"when ages beyond number had run their course from the creation of the world,")
        print(f"when God in the beginning created heaven and earth,")
        print(f"and formed man in His own likeness;")
        print(f"2957 years after the Flood,")
        print(f"when century upon century had passed")
        print(f"since the Almighty set His bow in the clouds after the Great Flood,")
        print(f"as a sign of covenant and peace;")
        print(f"2015 years since Abraham's birth;")
        print(f"In the twenty-first century since Abraham, our father in faith,")
        print(f"came out of Ur of the Chaldees;")
        print(f"1510 years since the People of Israel")
        print(f"were led by Moses in the Exodus from Egypt;")
        print(f"1032 years since David was anointed king of Israel;")
        print(f"In the 65th week of the prophecy of Daniel;")
        print(f"In the 194th Olympiad;")
        print(f"In the year 752 since the founding of Rome;") # AUC 752 = 2 BC
        print(f"and in the 42nd year of the rule of Caesar Octavian Augustus,")
        print(f"the whole world being at peace,")
        print(f"--------------------------------")
        print(f"JESUS CHRIST, eternal God and Son of the eternal Father,")
        print(f"desiring to consecrate the world by His most loving presence,")
        print(f"was conceived by the Holy Spirit,")
        print(f"and when nine months had passed since His conception,")
        print(f"was born of the Virgin Mary in Bethlehem of Judah, and was made man:")
        print(f"THE NATIVITY OF OUR LORD JESUS CHRIST ACCORDING TO THE FLESH.")
        
if __name__ == "__main__":
    # Testing Kalenda text for any given year.
    year = 2024 # Any given calendar year
    Kalenda(year).Proclamation()