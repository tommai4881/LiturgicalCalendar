"""
A Python module to print the information of a given year.
"""

from easter import easter # Insert nominal date of Easter from easter.py to calculate the boundary key.

def weekdaystring(weekday) -> str:
    """
    This function converts a weekday number to a string.
    """
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][weekday % 7]

def isleapyear(year) -> bool:
    """
    This function checks if a given year is a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 or year <= 1582)

class YearInfo:
    """
    This class prints the information of a given year.
    """
    def __init__(self, year, calendar = True):
        """
        This method initializes the YearInfo class.
        
        Args:
            year (int): The year to calculate the information for.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar).
        """
        self.year = year
        self.calendar = calendar
    @property
    def indiction(self) -> int:
        """
        This property calculates the indiction of a given year.
        Indiction is a cycle of 15 years used for tax purposes in the Roman Empire.
        """
        return (self.year + 2) % 15 + 1
    @property
    def golden_number(self) -> int:
        """
        This property calculates the golden number of a given year.
        The golden number is a cycle of 19 years used for calculating the date of Easter.
        """
        return (self.year % 19) + 1
    @property
    def Epact(self) -> int:
        """
        This property calculates the epact of a given year.
        The epact is the age of the moon on the day before first day of the year.
        It is used to calculate the date of Easter.
        """
        epact1582 = (11 * self.golden_number - 10) % 30
        if self.year > 1582:
            century = self.year // 100 + 1
            solar_correction = (3 * century) // 4 - 12
            lunar_correction = (8 * century + 5) // 25 - 5
            ep = (epact1582 - solar_correction + lunar_correction) % 30
        else:
            ep = (epact1582 + 7) % 30
        return ep
    @property
    def epactstring(self) -> str:
        """
        This property calculates the epact string of a given year.
        The epact string is the epact of a given year in string format.
        Note: 
        - Epact 0 is represented by an asterisk.
        - Epact 25 and golden number greater than 11 is represented by the Arabic numeral "25". This is called "black epact 25" due to the fact that epact 25 has Paschal full moon date on 17 April instead of 18 April if Golden Number exceeds 11 and is historically written with black ink instead of red ink (the ink of the epact).
        - Otherwise, the epact is represented by the Roman numeral of the epact.
        """
        def roman_numeral(number):
            """
            This sub-function converts a number to a Roman numeral.
            Args:
                number (int): The number to convert to a Roman numeral.
            Returns:
                str: The Roman numeral of the given number.
            """
            roman_numerals = {
                1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
                11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV", 16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX",
                21: "XXI", 22: "XXII", 23: "XXIII", 24: "XXIV", 25: "XXV", 26: "XXVI", 27: "XXVII", 28: "XXVIII", 29: "XXIX", 30: "XXX"
            }
            return roman_numerals[number]
        if self.Epact == 0: return "*" # Epact 0 is represented by an asterisk.
        elif self.Epact == 25 and self.golden_number > 11: return "25" # Black Epact 25
        else: return f"{roman_numeral(self.Epact)}"
    @property
    def martyrology(self) -> str:
        """
        This property calculates the martyrology letter of a given year.
        """
        return ["P", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "A", "B", "C", "D", "E", "F", "G", "H", "M", "N"][self.Epact]
    @property
    def paschalfullmoon(self) -> int:
        """
        This property calculates the paschal full moon of a given year.
        The paschal full moon is the first full moon after the vernal equinox.
        """
        if (self.Epact == 25 and self.golden_number > 11) or self.Epact == 24: self.Epact += 1
        fullmoon = 44 - self.Epact if self.Epact < 24 else 74 - self.Epact
        march = fullmoon
        april = fullmoon - 31
        if march > 31: return f"April {april}"
        else: return f"March {march}"
    @property
    def solarcycle(self) -> int:
        """
        This property calculates the solar cycle of a given year.
        The solar cycle is a cycle of 28 Julian years, used for calculating the date of Easter.
        """
        return (self.year + 8) % 28 + 1
    @property
    def doomsday(self) -> int:
        """
        This property calculates the doomsday of a given year. Based on Conway's Doomsday Algorithm.
        The doomsday is the anchor day of a given year, e.g. the last day of February, March 14, April 4, May 9, June 6, July 11, August 8, September 5, October 10, November 7, December 12.
        
        Returns:
            int: The doomsday of the given year (0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday).
        """
        k = self.year // 100
        d = (5 * (k % 4) + 2) % 7 if self.year > 1582 else 6 * k % 7 # Century anchor
        t = self.year % 100 # Last 2 digits
        a = t // 12
        b = t % 12
        c = b // 4
        return (a + b + c + d) % 7
    @property
    def doomsdaystring(self) -> str:
        """
        This property calculates the doomsday string of a given year.
        The doomsday string is the doomsday of a given year in string format.
        """
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][self.doomsday]
    class ChineseZodiac:
        """
        This subclass calculates the Chinese Zodiac of a given year.
        """
        def __init__(self, year):
            """
            This method initializes the ChineseZodiac class.
            
            Args:
                year (int): The year to calculate the Chinese Zodiac for.
            """
            self.year = year
        @property
        def animal(self) -> str:
            """
            This property calculates the animal of a given year.
            The animal is the animal of the year.
            """
            return ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"][self.year % 12]
        @property
        def element(self) -> str:
            """
            This property calculates the element of a given year.
            The element is the element of the year.
            """
            return ["Metal", "Water", "Wood", "Fire", "Earth"][(self.year // 2) % 5]
        def __str__(self) -> str:
            """
            This method returns the string representation of the Chinese Zodiac.
            """
            return f"{self.element} {self.animal}"
    @property
    def chinesezodiac(self) -> str:
        """
        This property calculates the Chinese Zodiac of a given year.
        """
        return self.ChineseZodiac(self.year)
    @property
    def dominicalletter(self) -> str:
        """
        This property calculates the dominical letter of a given year.
        The dominical letter is the letter of the week on which the first Sunday of the year falls. Based on the Doomsday Algorithm.
        e.g. 2024 was a leap year, so the dominical letter was GF since the doomsday was 4 (Thursday).
        2025 is a common year, so the dominical letter is E since the doomsday is 5 (Friday).
        """
        if isleapyear(self.year):
            return ["DC", "CB", "BA", "AG", "GF", "FE", "ED"][self.doomsday]
        elif self.year == 1582:
            return "GC" # 1582 was the year of the Gregorian calendar reform, so the dominical letter was GC coz of the omission of 5-14 October 1582.
        else:
            return ["C", "B", "A", "G", "F", "E", "D"][self.doomsday]
    @property
    def boundarykey(self) -> int:
        """
        This property calculates the boundary key of a given year.
        The boundary key is the key of the boundary of a given year, it corresponds to the date of Easter in the year.
        """
        day = easter(self.year, self.calendar)[0]
        month = easter(self.year, self.calendar)[1]
        if month == 4: day += 31 # If Easter is in April, then add 9 days.
        day = day - 22 # Subtract 22 to get the boundary key.
        boundarykey = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'Ѕ', 'З', 'И', 'І', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ѿ', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Ѣ', 'Ю', 'Ѫ', 'Я']
        return boundarykey[day]
        
    
if __name__ == "__main__": # Testing program, testing all the information of a given year.
    from easter import easter # import easterdate from easter.py to calculate the date of Easter in the testing program.
    year = 2025
    yearinfo = YearInfo(year)
    
    def eastersstring(year, calendar = True) -> str:
        """
        This function converts the date of Easter to a string.
        """
        day, month = easter(year, calendar)
        month = ["March", "April"][month - 3]
        return f"{month} {day}"
    
    print(f"The Indiction of the year {year} is {yearinfo.indiction}.")
    print(f"The Chinese Zodiac of the year {year} is {yearinfo.chinesezodiac}.")
    print(f"The Golden Number of the year {year} is {yearinfo.golden_number}.")
    print(f"The Epact of the year {year} is {yearinfo.epactstring}.")
    print(f"The Martyrology Letter of the year {year} is {yearinfo.martyrology}.")
    print(f"The Paschal Full Moon of the year {year} is {yearinfo.paschalfullmoon}.")
    print(f"The Solar Cycle of the year {year} is {yearinfo.solarcycle}.")
    print(f"The Doomsday of the year {year} is {yearinfo.doomsdaystring}.")
    print(f"The Dominical Letter of the year {year} is {yearinfo.dominicalletter}.")
    # Important dates of the year
    print(f"--------------------------------")
    print(f"New Year {year} is on {weekdaystring(yearinfo.doomsday - (3 if isleapyear(year) else 2))}.")
    print(f"The date of Easter {year} is {eastersstring(year)} (Boundary Key: {yearinfo.boundarykey}).")
    print(f"Christmas {year} is on {weekdaystring(yearinfo.doomsday - 1)}.")