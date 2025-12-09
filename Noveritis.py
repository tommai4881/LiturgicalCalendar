"""
A python module to print the text of the Noveritis for any given year.
"""
from lent import Lent, Eastertide, SolemnitiesoftheLord
from advent import Advent

class Noveritis:
    """
    This class prints the text of the Noveritis for any given year.
    The Noveritis is the announcement of key feast days in a given calendar year.
    It is announced right after the Gospel of Epiphany Day (Matthew 2:1-12) by the deacon, after that, the homily is given as usual.
    It is also known as the Announcement of Easter and the Moveable Feasts.
    """
    def __init__(self, year, calendar = True, AscensionThursday = False, CorpusChristiThursday = False):
        """
        This method initializes the Noveritis class.
        
        Args:
            year (int): The year to print the Noveritis for.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar, but Julian Easter if before 1583).
            AscensionThursday (bool): Whether to include Ascension Thursday in the Noveritis. Default is False, since the developer lives in South Vietnam, where Ascension is celebrated on Sunday.
            CorpusChristiThursday (bool): Whether to include Corpus Christi Thursday in the Noveritis. Default is False, since the developer lives in South Vietnam, where Corpus Christi is celebrated on Sunday.
        """
        self.year = year
        self.calendar = calendar
        self.AscensionThursday = AscensionThursday
        self.CorpusChristiThursday = CorpusChristiThursday
    @property
    def Noveritis(self):
        """
        This property prints the text of the Noveritis for any given year.
        """
        ashwednesday = Lent(self.year, self.calendar).AshWednesday
        easter = Eastertide(self.year, self.calendar).EasterSunday
        ascension = Eastertide(self.year, self.calendar, self.AscensionThursday).Ascension
        pentecost = Eastertide(self.year, self.calendar).pentecost
        corpus = SolemnitiesoftheLord(self.year, self.calendar, corpusChristionThursday = self.CorpusChristiThursday).CorpusChristi
        advent = Advent(self.year + 1).firstSunday # The first Sunday of the next liturgical year is the first Sunday of Advent of this calendar year.
        # After the Gospel of Epiphany Day (Matthew 2:1-12) by the deacon, the Noveritis is announced by the same deacon, as follows:
        print(f"KNOW, dear brothers and sisters,")
        print(f"that, as we have rejoiced at the Nativity of our Lord Jesus Christ,")
        print(f"so by leave of God's mercy")
        print(f"we announce to you also the joy of His Resurrection,")
        print(f"who is our Savior.")
        print(f"- On {ashwednesday.strftime('%B %d')} will fall Ash Wednesday,") # Ash Wednesday is the first day of Lent, 46 days before Easter.
        print(f"and the beginning of the Season of Lent.")
        print(f"- On {easter.strftime('%B %d')} you will celebrate with joy Easter Day,") # Easter Sunday is the Sunday after the Paschal Full Moon.
        print(f"the Paschal feast of our Lord Jesus Christ.")
        print(f"- On {ascension.strftime('%B %d')} will be the Ascension of our Lord Jesus Christ.") # Ascension is the 40th or 43th day after Easter Sunday, dependent of boolean flag AscensionThursday.
        print(f"- On {pentecost.strftime('%B %d')}, the feast of Pentecost.") # Pentecost is the 50th day after Easter Sunday.
        print(f"- On {corpus.strftime('%B %d')}, the Feast of the Most Holy Body and Blood of Christ,") # Corpus Christi is 60 or 63 days after Easter Sunday, dependent of boolean flag CorpusChristiThursday.
        print(f"- On {advent.strftime('%B %d')}, the First Sunday of the Advent of our Lord Jesus Christ,") # Advent is the first Sunday of the next liturgical year. In this case the first Sunday of the next liturgical year is the first Sunday of Advent of this calendar year.
        print(f"to Whom is honor and glory forever and ever. Amen.")
        # After the Noveritis, the homily is given as usual.
        
if __name__ == "__main__":
    # Testing Noveritis text for any given year, Gregorian calendar, Ascension Thursday and Corpus Christi Thursday.
    year = 2024 # Any given calendar year
    gregorian = False # Gregorian boolean flag if the Gregorian computus (True) or Julian Paschalion (False) rules are used to calculate the date of Easter.
    ascension = True # Ascension boolean flag if Ascension is celebrated on Thursday (True) or Sunday (False).
    corpus = False # Corpus Christi boolean flag if Corpus Christi is celebrated on Thursday (True) or Sunday (False).
    Noveritis(year, gregorian, ascension, corpus).Noveritis