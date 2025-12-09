"""
A Python module to calculate the dates of the Advent season for any given year as well as Christmastide. Works for proleptic Gregorian calendar due to the use of the datetime module (which supports proleptic Gregorian calendar).

This is made by a Vietnamese Catholic Christian developer, Thomas Mai Lê Bảo Khang, born in 2002, a student of Ho Chi Minh City University of Industry and Trade, Vietnam. He was baptized in the Catholic Church on August 12, 2022.

This is made for the purpose of calculating the dates of the Advent and Christmastide for any given year, and is not intended for any other purpose. The module is dedicated to Saint Carlo Acutis, and all saints whose feast days are celebrated on Advent or Christmastide (e.g. Saint Francis Xavier (3 December), Immaculate Conception (8 December, the patroness of Ho Chi Minh City), Our Lady of Guadalupe (12 December), etc.).

Originally written on Black Friday, 28 November 2025, 34th Friday of Ordinary Time, the penultimate day of the liturgical year before the beginning of Advent.
"""

from datetime import date, timedelta

def getSunday(date):
    """
    This function calculates the Sunday following or coinciding with a given date.
    
    Args:
        date (date): The date to calculate the Sunday following or coinciding with.
    
    Returns:
        date: The Sunday following or coinciding with the given date.
    """
    return date + timedelta(days = 6 - date.weekday()) 
    # Add the number of days to the date to get the Sunday following or coinciding with the given date. If the date is a Sunday, then the function returns the date itself.

class Advent:
    """
    This class calculates the dates of the Advent season for a given year.
    Advent is the season of preparation for the nativity of Jesus Christ, the Lord, it is the 'bootcamp' of the liturgical year.
    Every Sunday of Advent is a preparation for the coming of Jesus Christ, the Lord, and the end of the world. As such, it is a time of joy, hope, and anticipation.
    Every Sunday in Advent, we light one candle in 5-candle Advent wreath, and every day from 1 to 24 December we also open a door in 24-door Advent calendar.
    """
    def __init__(self, year):
        """
        This method initializes the Advent class.
        
        Args:
            year (int): The year to calculate the Advent dates for. Note that the input year is for liturgical year, since the liturgical year always starts on the first Sunday of Advent of the previous calendar year.
        """
        self.year = year 
        # The input year is the input year for liturgical year, since the liturgical year always starts on the first Sunday of Advent of the previous calendar year.
        # e.g. if the input year is 2025, then the liturgical year starts on the first Sunday of Advent of 2024.
    @property
    def firstSunday(self) -> date:
        """
        This property calculates the first Sunday of Advent. This is the 4th Sunday before Christmas. This Sunday is the Liturgical New Year, its Gospel reading is about the Second Coming of Jesus (Matthew 24:37-44; Mark 13:32-37; Luke 21:25-28, 33-36). The color of the vestments for this Sunday as well as all of Advent is violet. Please note: lectionary year C is the liturgical year which is evenly divisible by 3, the next year is year A, and the year after that is year B (which is the year before year C), so Synoptic Gospel writers switch places every Advent. Note: upon taking place of the previous Synoptic Gospel Writer, the Gospel reading of the liturgical year according to Synoptic Gospel Writer of the year is not started from the beginning, but from the near end of his Gospel.
        
        Gospel Reading:
        - A: Matthew 24:37-44 (#1) - Be Vigilant! Second Coming Incoming Soon in an Unknown Time!
        - B: Mark 13:32-37 (#2) - Awake! The End Is Near!
        - C: Luke 21:25-28, 33-36 (#3) - Jesus Is Coming Soon!
        
        Returns:
            date: The first Sunday of Advent.
        """
        return getSunday(date(self.year - 1, 11, 27)) 
        # The first Sunday of Advent is the Sunday following the 26th of November of the previous year.
    @property
    def secondSunday(self) -> date:
        """
        This property calculates the second Sunday of Advent. This is the 3rd Sunday before Christmas. Should the feast of Immaculate Conception conflicts with this Sunday, then this Sunday takes precedence so that the feast of Immaculate Conception is celebrated on the following day. The Gospel reading is about John the Baptist's proclamation of the coming of the Messiah. The color of the vestments for this Sunday is violet.
        
        Gospel Reading:
        - A: Matthew 3:1-12 (#4) - John the Baptist's Proclamation of the Coming of the Messiah
        - B: Mark 1:1-8 (#5) - The Prologue of the Gospel of Mark
        - C: Luke 3:1-6 (#6) - John the Baptist's Ministry
        
        Returns:
            date: The second Sunday of Advent.
        """
        return getSunday(date(self.year - 1, 12, 4))
        # The second Sunday of Advent is the Sunday following the 4th of December of the previous year.
    @property
    def thirdSunday(self) -> date:
        """
        This property calculates the third Sunday of Advent. This is the 2nd Sunday before Christmas. This Sunday is also known as Gaudete Sunday, hence the use of rose vestments. After this Sunday, there will be Ember Days on Wednesday, Friday and Saturday. Should it falls in 17 December, then O Sapientia is sung on this day.
        
        Gospel Reading:
        - A: Matthew 11:2-11 (#7) - Jesus on John the Baptist
        - B: John 1:6-8, 19-28 (#8) - John the Baptist's Testimony in the Gospel of John
        - C: Luke 3:10-18 (#9) - How to Share with John the Baptist
        
        Returns:
            date: The third Sunday of Advent.
        """
        return getSunday(date(self.year - 1, 12, 11))
        # The third Sunday of Advent is the Sunday following the 11th of December of the previous year.    
    @property
    def fourthSunday(self) -> date:
        """
        This property calculates the fourth Sunday of Advent. This is the last Sunday before Christmas. This Sunday is also known as Rorate Sunday, and it always corresponds to any of O Antiphons. Should it falls in 24 December, then there is no O Antiphons sung on this day, due to the Sunday must end before the First Vespers of Christmas Day.
        
        Gospel Reading:
        - A: Matthew 1:18-24 (#10) - Joseph and Mary's Engagement
        - B: Luke 1:26-38 (#11) - The Annunciation of the Virgin Mary
        - C: Luke 1:39-45 (#12) - The Visitation of the Virgin Mary
        
        Corresponding O Antiphons:
        - 18 December: O Adonai
        - 19 December: O Radix
        - 20 December: O Clavis
        - 21 December: O Oriens
        - 22 December: O Rex
        - 23 December: O Emmanuel
        - 24 December: Christmas Eve (NO O ANTIPHONS)
        
        ----------------------
        
        LITURGICAL NOTE: RULES FOR THE LATE ADVENT ALLELUIA (DEC 17-24)
        ===============================================================
        
        The selection of the Alleluia Verse (Gospel Acclamation) during the "O Antiphon"
        days (Dec 17-24) follows a specific hierarchy of precedence. The Lectionary for Mass
        uses a slightly different sequence than the Liturgy of the Hours (Vespers).

        1. SUNDAY PRECEDENCE (The "Trump Card")
        ---------------------------------------
        If a date between Dec 17-24 falls on a Sunday, the Sunday Liturgy takes precedence.
        The specific fixed-date "O Antiphon" verse is suppressed in favor of the Sunday Proper.

        * Scenario A: Third Sunday of Advent falls on Dec 17
        - Verse: "The Spirit of the Lord is upon Me, because He has anointed Me..." (Is 61:1)
        - Context: Matches the Gaudete Sunday readings.

        * Scenario B: Fourth Sunday of Advent (Falls between Dec 18-24)
        - Year A (Matthew Cycle): 
            "The virgin shall conceive, and bear a son, and they shall name Him Emmanuel." (Mt 1:23)
        - Year B & C (Mark/Luke Cycle): 
            "Behold, I am the handmaid of the Lord. May it be done to me according to Your word." (Lk 1:38)

        2. WEEKDAY LECTIONARY SEQUENCE (If not Sunday)
        ----------------------------------------------
        If the day is a weekday, the Alleluia verse follows the fixed Roman Lectionary sequence.
        NOTE: This differs from the Vespers sequence. 'O Emmanuel' is moved earlier, and 'O Rex'
        is repeated to accommodate the Morning Mass of Dec 24.

        - Dec 17: O Sapientia (Wisdom)
        - Dec 18: O Adonai (Lord/Leader)
        - Dec 19: O Radix (Root of Jesse)
        - Dec 20: O Clavis (Key of David)
        - Dec 21: O Emmanuel (God With Us) (* Note: Moved here from the traditional Dec 23 spot to highlight the Incarnation.)
        - Dec 22: O Rex (King of Nations)
        - Dec 23: O Rex (King of Nations) (* Note: The title is repeated to fill the gap left by moving Emmanuel.)
        - Dec 24: O Oriens (Radiant Dawn / Morning Star)
          (* Note: Moved to the Morning Mass of Christmas Eve. This aligns with the Gospel of the day (the Benedictus), 
          which prophecies the "Dawn from on high" (Oriens ex alto).)
        
        Returns:
            date: The fourth Sunday of Advent.
        """
        return getSunday(date(self.year - 1, 12, 18))
        # The fourth Sunday of Advent is the Sunday following the 18th of December of the previous year.
    @property
    def ImmaculateConception(self) -> date:
        """
        This property calculates the date of the Immaculate Conception. This feast is celebrated on the 8th of December.
        
        Gospel Reading: Luke 1:26-38 (#689) - The Annunciation of the Virgin Mary
        
        Returns:
            date: The date of the Immaculate Conception. Should it falls on a Sunday, then the feast is celebrated on the following day. 
        """
        return date(self.year-1, 12, 8) if date(self.year-1, 12, 8).weekday() != 6 else date(self.year-1, 12, 9)
        # The Immaculate Conception is celebrated on the 8th of December. Should it falls on a Sunday (weekday = 6), viz. the 2nd Sunday of Advent, then the feast is celebrated on the following day.
    
class Christmastide:
    """
    This class calculates the dates of the Christmastide for a given year.
    This season is the season of celebration of the nativity of Jesus Christ as well as His Epiphany. Note that the Gregorian New Year always in the Christmastide.
    """
    def __init__(self, year, epiphany_on_jan6th = False):
        """
        This method initializes the Christmastide class.
        
        Args:
            year (int): The year to calculate the Christmastide dates for. Note that the input year is for liturgical year, since the liturgical year always starts on the first Sunday of Advent of the previous calendar year.
            epiphany_on_jan6th (bool): If True, then Epiphany is celebrated on the 6th of January, else it is celebrated on the Sunday after New Year's Day. Defaults to False since the developer lives in Vietnam, where Epiphany is celebrated on the Sunday after New Year's Day instead of the January 6.
        """
        self.year = year # The input year is for liturgical year, since the liturgical year always starts on the first Sunday of Advent of the previous calendar year.
        self.epiphany_on_jan6th = epiphany_on_jan6th # If True, then Epiphany is celebrated on the 6th of January, else it is celebrated on the Sunday after New Year's Day.
    @property
    def ChristmasDay(self) -> date:
        """
        This property calculates the date of Christmas Day. This is the 25th of December, the "Eight Kalends of January". This feast day marks the beginning of the Christmas season, commemorating the nativity of Jesus Christ (Luke 2:1-20). It is always a Holy Day of Obligation in the Roman Catholic Church worldwide.
        
        Despite using to be a public holiday in Vietnam and being a working day in Vietnam since reunification in 1975 (as it used to be a public holiday before 1975, especially in South Vietnam), it is a cultural holiday in Vietnam, and thus its cultural significance as well as its economic and commercial significance is never diminished.
        
        [Grammatical Note: 'Using to' is employed here as the gerundive form of the habitual past, applied for morphological consistency. The phrase 'Despite using to [bare infinitive verb]...' is grammatically equivalent to 'Despite having formerly [verb in past participle]...'. The developer acknowledges the heterodoxy of this construction, but posits it as an intentional 'thickening' of English grammar for artistic and precision purposes in addition to precedent of thickening English dictionaries.]
        
        ------------------
        
        **The Kalenda:**     
        ----------------
           
        THE Eighth Kalends of January:
        In the year 5199 since the world was created, when ages beyond number had run their course from the creation of the world, when God in the beginning created heaven and earth, and formed man in His own likeness;
        2957 years after the Flood, when century upon century had passed since the Almighty set His bow in the clouds after the Great Flood, as a sign of covenant and peace;
        2015 years since Abraham’s birth; 
        in the twenty-first century since Abraham, our father in faith, came out of Ur of the Chaldees;
        1510 years since the People of Israel were led by Moses in the Exodus from Egypt;
        1032 years since David was anointed king of Israel;
        in the 65th week of the prophecy of Daniel;
        in the 194th Olympiad; 
        in the year 752 since the founding of Rome; 
        and in the 42nd year of the rule of Caesar Octavian Augustus, the whole world being at peace,
        JESUS CHRIST, eternal God and Son of the eternal Father, desiring to consecrate the world by His most loving presence, was conceived by the Holy Spirit, and when nine months had passed since His conception, was born of the Virgin Mary in Bethlehem of Judah, and was made man: The Nativity of Our Lord Jesus Christ according to the flesh.
        
        Note: The Eighth Kalends of January means December 25.
        
        Gospel Reading:
        - Vigil: Matthew 1:1-25 (#13) - The Nativity of Jesus Christ according to Matthew
        - Night: Luke 2:1-14 (#14) - The Nativity of Jesus Christ according to Luke
        - Dawn: Luke 2:15-20 (#15) - The Adoration of the Shepherds
        - Day: John 1:1-18 (#16) - The Word Became Flesh
        
        Returns:
            date: The date of Christmas Day.
        """
        return date(self.year-1, 12, 25)
        # The Christmas Day is celebrated on the 25th of December.
    @property
    def holyFamily(self) -> date:
        """
        This property calculates the date of the Holy Family. This is the Sunday after Christmas Day.
        
        Gospel Reading (#17):
        - A: Matthew 2:13-15, 19-23 - The Flight into Egypt
        - B: Luke 2:22-40 - The Presentation of Jesus in the Temple
        - C: Luke 2:41-52 - The Finding in the Temple
        
        Returns:
            date: The date of the Holy Family. Should Christmas falls on a Sunday, then the feast is celebrated on Friday, December 30, since the Sunday after Christmas is January 1 of the next calendar year.
        """
        return getSunday(date(self.year-1, 12, 26)) if self.ChristmasDay.weekday() != 6 else date(self.year-1, 12, 30)
        # The Holy Family is celebrated on the Sunday after Christmas Day.
        # But if it falls on a Sunday, then the feast is celebrated on Friday, December 30, since the Sunday after Christmas is January 1 of the next calendar year.
    @property
    def NewYear(self) -> date:
        """
        This property calculates the date of New Year's Day. This is the 1st of January, and is also known as Solemnity of Mary, Mother of God.
        
        Being the first day of civil year, it is also known as the first day of the year. As we Vietnamese prefer Lunar New Year over Gregorian New Year, the President of Vietnam never gives New Year's Day speech on this day (he always leave it to the Lunar New Year speech at midnight of the first day of the Lunar New Year). But for Japan and the rest of the world, it is the sole New Year, in which Japan officially abandoned Lunar New Year in 1873 (January 1, Meiji 6), after December 31, 1872 (Meiji 5/12/2).
        
        So while Vietnam and the rest of East Asia prefer Lunar New Year over Gregorian New Year, the rest of the world (as well as Japan) prefers Gregorian New Year over Lunar New Year. Here, when Japan decorates its houses with Christmas lights and decorations, it also uniquely uses kadomatsu as a Christmas decoration in addition, which is a traditional Japanese decoration for the New Year, in addition to the traditional Christmas decorations, 12 grapes and a countdown to the New Year like in the rest of the world.
        
        Gospel Reading (#18): Luke 2:16-21 - The Shepherds' Visit to the Manger and the Circumcision of the Lord
        
        Returns:
            date: The date of New Year's Day.
        """
        return date(self.year, 1, 1)
        # The New Year's Day is celebrated on the 1st of January.
    @property
    def Epiphany(self) -> date:
        """
        This property calculates the date of Epiphany. This is the 6th of January in England, Wales, Germany, Italy, Spain, etc. But in the United States, Vietnam, France, Philippines, etc., it is celebrated on the Sunday after New Year's Day. This feast day commemorates the manifestation of Jesus Christ to the Gentiles, as the Magi from the East came to Bethlehem to worship Him.
        
        Gospel Reading (#20): Matthew 2:1-12 - The Adoration of the Magi
        
        Returns:
            date: The date of Epiphany.
        """
        return date(self.year, 1, 6) if self.epiphany_on_jan6th else getSunday(date(self.year, 1, 2))
    
    @property
    def SecondSundayAfterChristmas(self) -> date:
        """
        This property calculates the date of the Second Sunday after Christmas. This is the second Sunday after Christmas Day and is only celebrated IF Epiphany is January 6th and is neither a Friday, Saturday nor Sunday.
        
        Gospel Reading (#19): John 1:1-18 - The Word Became Flesh
        
        Returns:
            date: The date of the Second Sunday after Christmas.
        """
        return getSunday(date(self.year, 1, 2)) if (self.epiphany_on_jan6th and not self.Epiphany.weekday() in [4, 5, 6]) else None
    
    @property
    def BaptismOfTheLord(self) -> date:
        """
        This property calculates the date of the Baptism of the Lord. This is the Sunday after Epiphany, commemorating the Baptism of Jesus Christ in the Jordan River by John the Baptist.
        In where Epiphany is transferred to the Sunday after New Year's Day, then the Baptism of the Lord is celebrated on the Sunday after January 6, should it falls on January 7 and 8, the day after Epiphany Sunday.
        
        Gospel Reading (#21):
        - A: Matthew 3:13-17 - The Baptism of Jesus Christ: "That's My Son!"
        - B: Mark 1:7-11 - The Baptism of Jesus Christ: "That's My Son!"
        - C: Luke 3:15-16, 21-22 - The Baptism of Jesus Christ: "That's My Son!"
        
        Returns:
            date: The date of the Baptism of the Lord.
        """
        if self.epiphany_on_jan6th: return getSunday(date(self.year, 1, 7))
        # In case where Epiphany is transferred into Sunday after January 1:
        elif self.Epiphany == date(self.year, 1, 7): return date(self.year, 1, 8) # Baptism on Monday, Jan 8 if Epiphany Sunday falls on January 7
        elif self.Epiphany == date(self.year, 1, 8): return date(self.year, 1, 9) # Baptism on Monday, Jan 9 if Epiphany Sunday falls on January 8
        else: return self.Epiphany + timedelta(days = 7) # Baptism on Sunday 7 days after Epiphany Sunday
        
if __name__ == "__main__":
    # Testing program, testing all the dates of the Advent and Christmastide for any proleptic Gregorian calendar year.
    year = 2025
    advent = Advent(year)
    christmastide = Christmastide(year)
    secondsunday = Christmastide(year, True).SecondSundayAfterChristmas
    nextadvent = Advent(year + 1) # Advent of this calendar year 
    nextchristmastide = Christmastide(year + 1) # Christmastide of this calendar year as well as the next calendar year
    print(f"Liturgical Year: {year}")
    print(f"First Sunday of Advent (First Violet Candle): {advent.firstSunday}")
    print(f"Second Sunday of Advent (Second Violet Candle): {advent.secondSunday}")
    print(f"Feast of the Immaculate Conception: {advent.ImmaculateConception}")
    print(f"Third Sunday of Advent (Rose Candle): {advent.thirdSunday}")
    print(f"Fourth Sunday of Advent (Third Violet Candle): {advent.fourthSunday}")
    print(f"Christmas Day (White Candle): {christmastide.ChristmasDay}")
    print(f"Holy Family: {christmastide.holyFamily}")
    print(f"New Year's Day AD {year}: {christmastide.NewYear}")
    print(f"Second Sunday after Christmas (in where Epiphany is January 6th): {secondsunday}")
    print(f"Epiphany: {christmastide.Epiphany}")
    print(f"Baptism of the Lord: {christmastide.BaptismOfTheLord}")
    print(f"First Sunday of Advent of this calendar year: {nextadvent.firstSunday}")
    print(f"Second Sunday of Advent of this calendar year: {nextadvent.secondSunday}")
    print(f"Feast of the Immaculate Conception of this calendar year: {nextadvent.ImmaculateConception}")
    print(f"Third Sunday of Advent of this calendar year: {nextadvent.thirdSunday}")
    print(f"Fourth Sunday of Advent of this calendar year: {nextadvent.fourthSunday}")
    print(f"Christmas Day of this calendar year: {nextchristmastide.ChristmasDay}")
    print(f"Holy Family of this calendar year: {nextchristmastide.holyFamily}")
    print(f"New Year's Day AD {year + 1}: {nextchristmastide.NewYear}")
    print(f"Epiphany of the next calendar year: {nextchristmastide.Epiphany}")
    print(f"Baptism of the Lord of the next calendar year: {nextchristmastide.BaptismOfTheLord}")