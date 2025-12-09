"""
A Module to calculate the dates of the Ordinary Time for any given year.
"""

from datetime import date, timedelta
from lent import Lent, SolemnitiesoftheLord
from easter import easterdate
from advent import Advent, getSunday

class OrdinaryTime:
    """
    This class calculates the dates of the Ordinary Time for any given year.
    """
    def __init__(self, year, calendar = True):
        """
        This method initializes the OrdinaryTime class.
        
        Args:
            year (int): The year to calculate the Ordinary Time for.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar, but Julian Easter if before 1583).
        """
        self.year = year
        self.lent = Lent(year)
        self.easter = easterdate(year, calendar = True)
        self.solemnitiesofthelord = SolemnitiesoftheLord(year)
    def sunday(self, week: int, prelent: bool = False) -> date:
        """
        This method calculates the date of the Sunday of the given week.
        Note: The Sunday of Ordinary Time is overriden by Feasts of the Lord and all Solemnities (which themselves are overriden by Sundays of Advent, Lent and Eastertide), while also overriding all Memorials and Feasts not of the Lord:
        - Feasts of the Lord:
            + Candlemas (2 February) - Reading (#534): Luke 2:22-40 - Presentation of Jesus at the Temple
            + Transfiguration (6 August) - Reading (#614): The same Gospel read earlier in the 2nd Sunday of Lent (the Transfiguration narrative)
            + Exaltation of the Holy Cross (14 September) - Reading (#638): John 3:13-17 - The Bronze Serpent and the Cross
            + Dedication of the Lateran Archbasilica (9 November) - Reading (#671): John 2:13-22 - The Cleansing of the Temple
        - Solemnities:
            + Pentecost Sunday - Reading (#63): John 20:19-23 - Receive the Holy Spirit!
            + The Most Holy Trinity (Sunday after Pentecost) - Reading (##164-166)
            + Corpus Christi (Sunday after Trinity in where Corpus Christi is celebrated on Sunday) - Reading (##167-169)
            + Ss Peter and Paul (29 June) - Reading (#591): Matthew 16:13-19 - The Confession of Peter
            + The Assumption of the Blessed Virgin Mary (15 August) - Reading (#622): Luke 1:39-56 - The Visitation of the Virgin Mary
            + All Saints (1 November) - Reading (#667): Matthew 5:1-12a - The Beatitudes
            + All Souls (2 November) - Reading (#668): 
                + First Mass: John 6:37-40 - Works of the Lord
                + Second Mass: Luke 23:44-46, 50, 52-53 - The Good Thief
                + Third Mass: John 11:21-27 - I Am the Resurrection and the Life
            - By convention:
                + The 0th Sunday of Ordinary Time BEFORE Lent is the Sunday coinciding and after December 31 of the previous calendar year. So that the Baptism is the Sunday AFTER 6 January.
                + The 0th Sunday of Ordinary Time AFTER Pentecost is the Sunday coinciding and after March 27 of the current calendar year. So that Christ the King is the Sunday after 19 November and Advent start on another Sunday after Christ the King
        
        Args:
            week (int): The week number to calculate the date for.
            prelent (bool): Whether to calculate the date for the Sunday before Lent. Default is False (for Sundays after Pentecost).
        
        Returns:
            date: The date of the Sunday of the given week.
        """
        if prelent:
            return getSunday(date(self.year - 1, 12, 31)) + timedelta(weeks = week)
        else:
            return getSunday(date(self.year, 3, 27)) + timedelta(weeks = week)
    def bound(self) -> int:
        """
        This method calculates the bound of the given year
        Args:
            week (int): The week number to calculate the bound for.
        Returns:
            int: The bound of the given week.
        """
        day = (self.easter - date(self.year, 3, 1)).days + 1
        isleap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
        prelent = 4 + (day - (17 if isleap else 18)) // 7 # Week number before Lent
        postpentecost = 6 + (day - 20) // 7 # Week number after Pentecost
        return prelent, postpentecost
    @property
    def max_week(self) -> int:
        """
        This property calculates the maximum week number of the Ordinary Time before Ash Wednesday.
        Returns:
            int: The maximum week number of the Ordinary Time before Ash Wednesday.
        """
        return self.bound()[0]
    @property
    def week_after_pentecost(self) -> int:
        """
        This property calculates the week number of the Sunday after Pentecost.
        Returns:
            int: The week number of the Sunday after Pentecost.
        """
        return self.bound()[1]
    @property
    def ChristtheKing(self) -> date:
        """
        This property calculates the date of Christ the King. Christ the King is the last Sunday of the liturgical year, commemorating the kingship of Jesus Christ. This is also the 34th Sunday of the Ordinary Time (and Sunday nearest to 23 November).
        
        Gospel Readings:
        - A: Matthew 25:31-46 (#160) - The Last Judgment
        - B: John 18:33b-37 (#161) - Jesus before Pilate
        - C: Luke 23:35-43 (#162) - The Crucified King
        
        Returns:
            date: The date of Christ the King.
        """
        return self.sunday(34)
        
if __name__ == "__main__":
    # Testing program, testing all the dates of the Ordinary Time for any proleptic Gregorian calendar year.
    year = 2025
    for week in range(1, OrdinaryTime(year).max_week + 1):
        print(f"Sunday {week} of Ordinary Time: {OrdinaryTime(year).sunday(week, True)}")
    for week in range(OrdinaryTime(year).week_after_pentecost, 35): # There are maximum nominal 34 weeks of Ordinary Time.
        print(f"Sunday {week} of Ordinary Time: {OrdinaryTime(year).sunday(week)}")