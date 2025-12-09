"""
A Python module to calculate the dates of the Lent and Eastertide for any given year. Works for proleptic Gregorian calendar due to the use of the `datetime` module (which supports proleptic Gregorian calendar). For years before 1583, Easter is calculated using the historical Julian Paschalion rules and the resulting date is converted to and expressed in the proleptic Gregorian calendar.

This is made by a Vietnamese Catholic Christian developer, Thomas Mai Lê Bảo Khang, born in 2002, a student of Ho Chi Minh City University of Industry and Trade, Vietnam. He was baptized in the Catholic Church on August 12, 2022.

This is made for the purpose of calculating the dates of the Lent and Eastertide for any given year, and is not intended for any other purpose. The module is dedicated to Saint Carlo Acutis, and all saints whose feast days are celebrated on Lent and Eastertide (e.g. Saint Joseph (19 March), the Annunciation of the Virgin Mary (25 March), St Mark (25 April), St Joseph the Worker (1 May), Ss Philip and James the Less (3 May), etc).

Originally written on First Monday of Advent, 1 December 2025, the second day of Liturgical Year 2026, when the first window of the 24-window Advent calendar is opened after the first candle of 5-candle Advent wreath is lit (30 November 2025 was the first day of Advent and the First Sunday of Advent of lectionary year A).
"""

from datetime import date, timedelta # import date and timedelta from datetime module to convert to Gregorian calendar to be compatible with the Gregorian calendar.
from easter import easterdate # import easter and easterdate from easter.py module to calculate the date of Easter.

class Lent:
    """
    This class calculates the dates of the Lent season for a given year.
    Lent is the season of penance in which we must fast and abstain, also intense prayer too, it is sadder and longer than Advent. It is the season of preparation for the Resurrection of Jesus Christ, the Lord.
    Alleluia is banned all throughout Lent, including the Sundays of Lent and feasts and solemnities of Lent. The only exception is the Easter Vigil, the last day of Lent where Alleluia is sung.
    Every Sunday of Lent is how we journey by the Cross of Jesus Christ. And all Lent season is the catechumens' last challenge before their baptism on Easter Vigil.
    Note: 
    - All days of the Lent and Eastertide are weekday-locked (as Easter cannot be any day of the week other than Sunday and neither can Ash Wednesday other than Wednesday), the only the `timedelta` function is used to calculate the dates of the days of the Lent and Eastertide.
    - The Lent season is always 40 days, from Ash Wednesday to Holy Saturday, discounting the Sundays of Lent.
    - If counting from Ash Wednesday to Maundy Thursday inclusive (per current Roman Missal since 1970), then Lent is 44 days (counting Sundays).
    - Unlike Advent, the Lent cannot have 5-candle Advent Wreath nor Advent calendar, but the Lenten calendar (which is always reusable since Advent date ranges (hence the separate Advent Candles in Advent Wreath (Sunday) and Advent calendar (December 1-24)) varies but Lent date ranges is always the same). Instead, Lent is the intense time for the spiritual journey of the faithful to follow the way of the Cross of Jesus Christ.
    - Instead of the Advent Candles, Lent has the cross and violet stoles on it as well as fish to remind us of the suffering way of the Cross of Jesus Christ and to live His Passion.
    - While Advent does allow saints to be celebrated on Advent weekdays, Lent does not allow any saints falling in Lent (e.g. St Patrick (17 March)) to be celebrated on Lent weekdays (but only commemorated instead, except for the Chair of St Peter (22 February), St Joesph (19 March), the Annunciation of the Virgin Mary (25 March), etc).
    - While Advent does allow organs to be played solo without the accompaniment of the choir and must not exceed Christmastide; except on Laetare Sunday, Solemnities and Feasts in Lent, Lent does not allow organs to be played solo without the accompaniment of the choir but should not exceed Eastertide. On permitted days in Lent, it can be played without the accompaniment of the choir but SHOULD NOT exceed Eastertide. (Coz the General Instruction of the Roman Missal (GIRM) doesn't explicitly say that on permitted days in Lent, it must not exceed Eastertide).
    - While Advent does allow flowers in the altar decorations but minimal and not to exceed Christmastide, Lent does not allow flowers in the altar decorations except on Laetare Sunday, Solemnities and Feasts in Lent, and Eastertide. On the permitted days in Lent, it can be used but SHOULD NOT exceed Eastertide. (Coz the General Instruction of the Roman Missal (GIRM) doesn't explicitly say that on permitted days in Lent, it must not exceed Eastertide).
    - While Advent does allow Te Deum on Advent Sundays (despite the omission of Gloria, except on Solemnities and Feasts on Advent when both Te Deum and Gloria are allowed), Lenten Sundays do not allow Te Deum in addition to ommission of Gloria, it should be substituted with Lenten Prayer of Saint Ephrem the Deacon (because the General Instruction of Liturgy of the Hours doesn't explicitly say what to say instead of Te Deum on Lenten Sundays). The only days on Lent when both Te Deum and Gloria are allowed is the Solemnities and Feasts in Lent.
    - On Fridays in Lent as well as Ash Wednesday, if you turn 14, you must abstain from meat, so you can only eat vegan food, as well as seafood, eggs and dairy products.
    - Also on Ash Wednesday and Good Friday, if you turn 18, you must fast by eating a full meal and 2/3 of another meal, as well as abstain from meat, snacks and desserts, so you can only eat vegan food, as well as seafood, eggs and dairy products. You needn't fast if you turn 60.
    """
    def __init__(self, year, calendar = True):
        """
        This method initializes the Lent class.
        
        Args:
            year (int): The year to calculate the Lent dates for. Note that the input year is for liturgical year, since the liturgical year always starts on the first Sunday of Lent of the previous calendar year.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar, but Julian Easter if before 1583).
        """
        self.year = year # The input year is for liturgical year.
        self.easter = easterdate(year, calendar) # Calculate the date of Easter for the given year.
    @property
    def AshWednesday(self) -> date:
        """
        This property calculates the date of Ash Wednesday. Ash Wednesday is the first day of Lent. It is a day of fasting and abstinence.
        It is the first day Alleluia is banned, so the day before that, all Alleluias must be burned along with the ashes of the previous year's Palm Sunday's palms. The ashes are later distributed to the faithful in the form of ashes on the foreheads.
        If falling on a Solemnity or any lower rank of any feast day, Ash Wednesday takes precedence over the feast day and coinciding solemnity must be transferred to the following day.
        
        Gospel Reading (#219): Matthew 6:1-6, 16-18 - Fasting and Almsgiving
        
        Returns:
            date: The date of Ash Wednesday.
        """
        return self.easter - timedelta(days = 46) # Ash Wednesday is 46 days before Easter.
    @property
    def FirstSunday(self) -> date:
        """
        This property calculates the date of the First Sunday of Lent. It is also known as Invocabit Sunday. It is the Sunday after Ash Wednesday. The Sunday Mass may be preceded with the Litany of the Saints. The catechumens is now egilible for their Election on the First Sunday of Lent. After this Sunday, there will be Ember Days on Wednesday, Friday and Saturday.
        
        The Gospel reading is about the Temptation of Our Lord Jesus Christ by the Devil in the Desert:
        - A: Matthew 4:1-11 (#22)
        - B: Mark 1:12-15 (#23) - Note: Markan narrative is so brief so the focus changes to call to repentance.
        - C: Luke 4:1-13 (#24)
        
        Returns:
            date: The date of the First Sunday of Lent.
        """
        return self.easter - timedelta(days = 42) # The First Sunday of Lent is 42 days before Easter.
    @property
    def SecondSunday(self) -> date:
        """
        This property calculates the date of the Second Sunday of Lent. It is also known as Reminiscere Sunday.
        The Gospel reading is about the Transfiguration of the Lord Jesus Christ which is the same one read later on the Feast of the Transfiguration of the Lord Jesus Christ on August 6 later in the year (which always overrides the 18th Sunday of Ordinary Time due to being a Feast of the Lord Jesus Christ, but with different Gospel reading changes per Gospel Writer per year).
        - A: Matthew 17:1-9 (#25)
        - B: Mark 9:2-10 (#26)
        - C: Luke 9:28b-36 (#27)
        
        Returns:
            date: The date of the Second Sunday of Lent.
        """
        return self.easter - timedelta(days = 35) # The Second Sunday of Lent is 35 days before Easter.
    @property
    def ThirdSunday(self) -> date:
        """
        This property calculates the date of the Third Sunday of Lent. It is also known as Oculi Sunday.
        If there are catechumens, then this Sunday is the First Scrutiny with reading of John 4:5-42. Else, the Gospel readings of the 3rd to 5th Sunday of Lent diverge per lectionary year.
        In Year A, and other years when there are catechumens, the Gospel trilogy for 3-5th Sunday of Lent is "Baptism Stories": John 4:5-42 -> John 9:1-41 -> John 11:1-45
        In Year B, the Gospel trilogy for 3-5th Sunday of Lent is "Signs of the Cross": John 2:13-25 -> John 3:14-21 -> John 12:20-33
        In Year C, the Gospel trilogy for 3-5th Sunday of Lent is "Stories of Repentance": Luke 13:1-9 -> Luke 15:1-3, 11-32 -> John 8:1-11
        
        Gospel Reading:
        - A (Baptism): John 4:5-42 (#28) - The Samaritan Woman at the Well
        - B (Signs): John 2:13-25 (#29) - The Cleansing of the Temple
        - C (Repentance): Luke 13:1-9 (#30) - Repent or Die!
        
        Returns:
            date: The date of the Third Sunday of Lent.
        """
        return self.easter - timedelta(days = 28) # The Third Sunday of Lent is 28 days before Easter.
    @property
    def FourthSunday(self) -> date:
        """
        This property calculates the date of the Fourth Sunday of Lent. It is also known as Laetare Sunday. 
        This is the only Sunday of Lent where floral altar decorations, which is forbidden in the rest of Lent (outside of Solemnities and Feasts and solemnities of Lent, while in Advent, floral altar decorations are minimal and not to exceed Christmastide), are allowed (but not to exceed Eastertide). Rose vestments are worn on this Sunday.
        Also on this Sunday, organs are played solo without the accompaniment of the choir (which in the rest of Lent, the organ must be played with the accompaniment of the choir, but in Advent, organs are played lest exceeding Christmastide) but should not exceed Eastertide.
        If there are catechumens, then this Sunday is the Second Scrutiny with reading of John 9:1-41. Else, the Gospel reading diverges per lectionary year.
        
        Gospel Reading:
        - A (Baptism): John 9:1-41 (#28) - The Blind Man
        - B (Signs): John 3:14-21 (#29) - Midnight Talk with Nicodemus
        - C (Repentance): Luke 15:1-3, 11-32 (#30) - The Prodigal Son
        
        Note:
        - This Sunday is also known as Mothering Sunday, the Mother's Day in United Kingdom, hence the 'Alleluia-less' Mother's Day to differ from US Mother's Day (the 2nd Sunday of May, which Vietnam also observes, the 'Alleluiaful' Mother's Day, always falling during Eastertide).
        
        Returns:
            date: The date of the Fourth Sunday of Lent.
        """
        return self.easter - timedelta(days = 21) # The Fourth Sunday of Lent is 21 days before Easter.
    @property
    def FifthSunday(self) -> date:
        """
        This property calculates the date of the Fifth Sunday of Lent. It is also known as Passion Sunday, or Judica Sunday. This is the Sunday before Palm Sunday. The crosses and statues are veiled in violet veils for the last 2 weeks of Lent.
        If there are catechumens, then this Sunday is the Third Scrutiny with reading of John 11:1-45. Else, the Gospel reading diverges per lectionary year.
        
        Gospel Reading:
        - A (Baptism): John 11:1-45 (#31) - The Resurrection of Lazarus
        - B (Signs): John 12:20-33 (#32) - The Time is Near
        - C (Repentance): John 8:1-11 (#33) - The Woman Caught in Adultery
        
        Returns:
            date: The date of the Fifth Sunday of Lent.
        """
        return self.easter - timedelta(days = 14) # The Fifth Sunday of Lent is 14 days before Easter.
    @property
    def PalmSunday(self) -> date:
        """
        This property calculates the date of Palm Sunday. Palm Sunday is the first day of Lent. It is the Sunday before Easter. Red vestments are worn on this Sunday.
        
        On this Sunday as well as suceeding 2 Sundays, Easter and Divine Mercy, and weekdays between, all other saints (including Mary) are all omitted. Should Annunciation fall during the 15 consecutive days between Palm Sunday and Divine Mercy, then the feast of the Annunciation is celebrated on the day after Divine Mercy with Angelus traded for Regina Caeli. (e.g 2024 Annunciation Day was 8 April due to 25 March was Holy Monday). Should St Joseph fall during the 15 consecutive days between Palm Sunday and Divine Mercy, then the feast of St Joseph is celebrated on the day before Palm Sunday (e.g. 2008 St Joseph Day was 15 March due to 19 March was Spy Wednesday).
        
        At the beginning of this Mass, the palms are blessed and distributed to the faithful. This is the only day of the year on which 2 different Gospel Readings are read in the same Mass. The first Gospel reading is about the Triumphal Entry of Jesus Christ into Jerusalem (#37):
        - A: Matthew 21:1-11
        - B: Mark 11:1-10 or John 12:12-16
        - C: Luke 19:28-40
        
        But upon finishing the first Gospel reading and procession of Palms, the focus of the Mass changes to the Passion of the Lord Jesus Christ. 
        
        The Passion Reading is like Gospel Reading, but with 3 concurrent readers (one in middle acts as Jesus, another to his left acts as other people and another to Jesus-acting person's right acts as the Evangelist, i.e. the one who writes the Gospel). The beginning: no "The Lord be with you" but it starts directly with the Evangelist-actor saying "The Passion of our Lord Jesus Christ according to (Matthew, Mark, Luke)" without the crossing the book nor the response: "Glory to Thee, O Lord!". After the Passion Reading, the readers don't kiss the book after saying: "The Gospel of the Lord".
        
        The Passion Reading according to Synoptic Gospel Writers (#38):
        - A: Matthew 26:14 - 27:66
        - B: Mark 14:1 - 15:47
        - C: Luke 22:14 - 23:56
        
        Returns:
            date: The date of Palm Sunday.
        """
        return self.easter - timedelta(days = 7) # Palm Sunday is 7 days before Easter.
    @property
    def MaundyThursday(self) -> date:
        """
        This property calculates the date of Maundy Thursday. Maundy Thursday is the day before Good Friday. White vestments are worn on this day.
        
        In the morning, the cathedrals celebrate the Chrism Mass, recalling the institution of the sacrament of Holy Orders. The bishop blesses two oil barrels, one for the catechumens (OC) and one for the infirm (OI). Then he and his clergy renew their ordination vows and the bishop consecrates the third oil barrel, the chrism (SC, the sacred oil) for the rest of the year.
        Gospel Reading (#260): Luke 4:16-21 - Christ in the Synagogue
        
        The Triduum begins in the evening of Maundy Thursday with the Mass of the Last Supper (also known as the Mass of the Lord's Supper), where Jesus Christ institutes the sacrament of the Eucharist. And the tabernacle must be empty before the Mass of the Last Supper.
        Before the institution, He washes the feet of the Apostles (as it is indicated in the Gospel reading). The bell stop ringing after the Gloria (where bells run off for the last time before the Gloria of Easter Vigil), so in the Eucharistic Prayer, it is replaced by the clappers, semantra and crotaluses instead. After the Gospel, the priest washes feet for 12 randomly-chosen faithful from the congregation.
        After the Mass, the faithful process to the altar of repose (where the Blessed Sacrament must be in a sealed tabernacle and not monstrance) to spend the night in prayer and fasting, with the candles extinguished and altar stripped bare.
        Gospel Reading (#39): John 13:1-15 - The Washing of the Feet
        
        Returns:
            date: The date of Maundy Thursday.
        """
        return self.easter - timedelta(days = 3) # Maundy Thursday is 3 days before Easter.
    @property
    def GoodFriday(self) -> date:
        """
        This property calculates the date of Good Friday. Good Friday is the day after Maundy Thursday. Red vestments are worn on this day.
        
        On this day, the Lamb of God sacrificed for the sins of the world. As a result, it is the day of fasting and abstinence.
        
        The Mass is prohibited on this day and on Holy Saturday proper, instead, there are special Good Friday Liturgy. 
        In the beginning of the Liturgy, the priest and all congregation all prostrate themselves on the floor in front of the altar.
        Then the liturgy of the Word -> then the Ten Good Friday Intercessions: for the Church, for the Pope, for Church members, for catechumen who will be baptized on Easter Vigil the next night, for Christian unity, for the Jews, for non-Christians, for atheists, for the goverment officials and for all the suffering people!
        Then the Cross used for adoration is unveiled and adored -> Holy Communion from the Reserved Sacrament (from the altar of repose). After the communion, the Blessed Sacrament is transferred to a secret place.
        After the Liturgy, which must end without music, the altar is stripped bare and all remaining veiled crosses are unveiled.
        
        Gospel Reading (#40): John 18:1 - 19:42 - The Passion of Our Lord Jesus Christ According to John
        
        Returns:
            date: The date of Good Friday.
        """
        return self.easter - timedelta(days = 2) # Good Friday is 2 days before Easter.
    @property
    def HolySaturday(self) -> date:
        """
        This property calculates the date of Holy Saturday. Holy Saturday is the day after Good Friday and the day before Easter Sunday.
        
        On this day proper, the only permitted liturgy is the Liturgy of the Hours. And only available sacrament is the Viaticum (for the dying), Confession and Anointing of the Sick.
        Also on this day, the Church waits in silence reflecting the death of the Lord Jesus Christ and mourning of His death and burial. Also, on this day, all remaining veiled statues are being unveiled for Easter Vigil (as they MUST be unveiled before Easter Vigil).
        According to 1988 Vatican directive, Holy Saturday and Lent must end at nightfall of the day before Easter Sunday, so scheduling Easter Vigil Mass on usual Saturday anticipatory Mass is prohibited, instead, on this time, the Vespers of Holy Saturday is celebrated instead. Fasting is recommended to prepare for Eastertide.
        Gospel Reading: NO READING.
        
        Note: 
            Holy Saturday is the Apodosis (Leavetaking) of Lent, Apodosis of Angelus, the Saddest Apodosis (Leavetaking).
        
        Returns:
            date: The date of Holy Saturday.
        """
        return self.easter - timedelta(days = 1) # Holy Saturday is the day before Easter.
    
class Eastertide:
    """
    This class calculates the dates of the Eastertide for a given year.
    Eastertide is the 50 days from Easter Sunday to Pentecost Sunday. It is the time of joy and celebration of the Resurrection of the Lord Jesus Christ.
    Also, not only Alleluia is allowed, but also expanded throughout the Eastertide, hence Alleluia overloads on Eastertide.
    On Eastertide, instead of Angelus, we will pray the Regina Coeli instead. Also on Eastertide, according to the Percepts of the Church, you must take communion at least once in Eastertide annually.
    Note:
    - Also like `Lent` class, all the dates of the Eastertide are weekday-locked (as Easter cannot be any day of the week other than Sunday and neither can Ascension Thursday other than Thursday), the only the `timedelta` function is used to calculate the dates of the days of the Eastertide.
    - While Lent forbids Alleluia in all of Lent including its solemnities and feasts (EXCEPT the Easter Vigil), Eastertide allows Alleluia in all of Eastertide including its solemnities and feasts, but not only does it return but also is expanded throughout the Eastertide (appended after every liturgical antiphon, e.g. introits, communions, psalmody antiphons, etc), hence Alleluia overloads on Eastertide.
    - White vestments are worn on Eastertide. On Eastertide Masses, Matins Lauds and Vespers, the Easter Candle is lit.It is placed in the center of the altar.
    """
    def __init__(self, year, calendar = True, ascensionThursday = False):
        """
        This method initializes the Eastertide class.
        
        Args:
            year (int): The year to calculate the Eastertide dates for. Note that the input year is for liturgical year, since the liturgical year always starts on the first Sunday of Lent of the previous calendar year.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar, but Julian Easter if before 1583).
            ascensionThursday (bool): Whether to include Ascension Thursday in the Eastertide. Ascension is Thursday (`True`) in Northeast USA, North Vietnam, France, England, etc; but Sunday (`False`) in most of the rest of the world. Default is False, since the developer lives in South Vietnam, where Ascension is celebrated on Sunday.
        """
        self.year = year # The input year is for liturgical year.
        self.easter = easterdate(year, calendar) # Calculate the date of Easter for the given year.
        self.ascensionThursday = ascensionThursday # Whether to include Ascension Thursday in the Eastertide.
    @property
    def EasterVigil(self) -> date:
        """
        This property calculates the date of Easter Vigil. Easter Vigil is the vigil of Easter Sunday. It is the last night of Lent and the only day of Lent where Alleluia is allowed. Yellow vestments are worn on this day as well as the next day and all the days of Easter Octave.
        
        According to 1988 Vatican directive, Easter Vigil must start at nightfall of Holy Saturday and end at dawn of Easter Sunday, so scheduling Easter Vigil Mass on usual Saturday anticipatory Mass is prohibited, instead, on this time, the Vespers of Holy Saturday is celebrated instead. The nightfall of Holy Saturday is the 'havdalah of Lenten fast' (the apodosis (leavetaking) of Lent).
        
        On the day of Holy Saturday proper, the old Easter Candle of the previous year is removed from baptismal font (the resting place of the Easter Candle after Pentecost Sunday) and discarded with all the decorations removed and carved away as well as its five incense sticks. It is replaced with the new un-blessed Easter Candle without any incense sticks (most Easter candles are pre-carved in Lent).
        
        After the sunset, on the last moments of Holy Saturday proper, the rest of the statues veiled on 5th Sunday of Lent are unveiled for Easter Vigil (as they MUST be unveiled before Easter Vigil). Altars previously stripped bare may be clothed again with the altar linens as well as flowers (previously banned in Lent) are allowed again (these altar decorations MAY be delayed until later in Gloria of Easter Vigil instead as it is practiced in most parishes).
        
        Consisting of 4 parts:
        - Liturgy of Light: The Church is darkened in the beginning of the Mass, then the priest lights the Paschal Candle and the other candles, then the priest recites the Exsultet.
        - Liturgy of Word: Read at least 2 Old Testament readings in addition to mandatory Exodus 14:15-15:1; after the last Old Testament reading, the Gloria is sung and all bell ran off excessively in joy (plus, organ overloads on Eastertide from Gloria of Easter Vigil)! Then Romans 6:3-11 and finally the Gospel reading on Empty Tomb.
        - Liturgy of Baptism: If there are catechumens, the priest baptizes the catechumens who will be baptized on this night. Nevertheless, all the congregation must renew their baptismal promises.
        - Liturgy of Eucharist: The priest celebrates the Mass of the Resurrection of the Lord Jesus Christ, that's why Easter Vigil CANNOT be a Saturday anticipatory Mass, instead, it is the First Mass of Easter Day. The Blessed Sacrament consecrated on Maundy Thursday returns to tabernacle with newly-consecrated one consecrated on Easter Vigil. If you attend Easter Vigil, you finish the speedrun since Easter Vigil is the earliest time you must fulfill the Easter duty (as Eastertide starts on Easter Vigil, which cannot be the last minutes of Holy Saturday).
        
        Gospel Reading - The Resurrection of the Lord Jesus Christ according to Synoptic Gospel Writers (#41):
        - A: Matthew 28:1-10
        - B: Mark 16:1-8
        - C: Luke 24:1-12
        
        ===============================
        THE EXSULTET
        ===============================
        
        Exult, let them exult, the hosts of heaven,
        exult, let Angel ministers of God exult,
        let the trumpet of salvation
        sound aloud our mighty King's triumph!

        Be glad, let earth be glad, as glory floods her,
        ablaze with light from her eternal King,
        let all corners of the earth be glad,
        knowing an end to gloom and darkness.

        Rejoice, let Mother Church also rejoice,
        arrayed with the lightning of His glory,
        let this holy building shake with joy,
        filled with the mighty voices of the peoples.

        (Therefore, dearest friends,
        standing in the awesome glory of this holy light,
        invoke with me, I ask you,
        the mercy of God almighty,
        that He, who has been pleased to number me,
        though unworthy, among the Levites,
        may pour into me His light unshadowed,
        that I may sing this candle's perfect praises).

        (Deacon: The Lord be with you.
        People: And with your spirit.)
        Deacon: Lift up your hearts.
        People: We lift them up to the Lord.
        Deacon: Let us give thanks to the Lord our God.
        People: It is right and just.

        It is truly right and just,
        with ardent love of mind and heart
        and with devoted service of our voice,
        to acclaim our God invisible, the almighty Father,
        and Jesus Christ, our Lord, His Son, His Only Begotten.

        Who for our sake paid Adam's debt to the eternal Father,
        and, pouring out His own dear Blood,
        wiped clean the record of our ancient sinfulness.

        These, then, are the feasts of Passover,
        in which is slain the Lamb, the one true Lamb,
        whose Blood anoints the doorposts of believers.

        This is the night,
        when once You led our forebears, Israel's children,
        from slavery in Egypt
        and made them pass dry-shod through the Red Sea.

        This is the night
        that with a pillar of fire
        banished the darkness of sin.

        This is the night
        that even now throughout the world,
        sets Christian believers apart from worldly vices
        and from the gloom of sin,
        leading them to grace
        and joining them to His holy ones.

        This is the night
        when Christ broke the prison-bars of death
        and rose victorious from the underworld.

        Our birth would have been no gain,
        had we not been redeemed.
        O wonder of Your humble care for us!
        O love, O charity beyond all telling,
        to ransom a slave You gave away Your Son!

        O truly necessary sin of Adam,
        destroyed completely by the Death of Christ!

        O happy fault
        that earned for us so great, so glorious a Redeemer!

        O truly blessed night,
        worthy alone to know the time and hour
        when Christ rose from the underworld!

        This is the night
        of which it is written:
        The night shall be as bright as day,
        dazzling is the night for me, and full of gladness.

        The sanctifying power of this night
        dispels wickedness, washes faults away,
        restores innocence to the fallen, and joy to mourners,
        drives out hatred, fosters concord, and brings down the mighty.

        On this, Your night of grace, O holy Father,
        accept this candle, a solemn offering,
        the work of bees and of Your servants' hands,
        an evening sacrifice of praise,
        this gift from Your most holy Church.

        But now we know the praises of this pillar,
        which glowing fire ignites for God's honor,
        a fire into many flames divided,
        yet never dimmed by sharing of its light,
        for it is fed by melting wax,
        drawn out by mother bees
        to build a torch so precious.

        O truly blessed night,
        when things of heaven are wed to those of earth,
        and divine to the human.

        Therefore, O Lord,
        we pray You that this candle,
        hallowed to the honour of Your name,
        may persevere undimmed,
        to overcome the darkness of this night.
        Receive it as a pleasing fragrance,
        and let it mingle with the lights of heaven.
        May this flame be found still burning
        by the Morning Star:
        the one Morning Star who never sets,
        Christ Your Son,
        who, coming back from death's domain,
        has shed His peaceful light on humanity,
        and lives and reigns for ever and ever. Amen.
        
        Returns:
            date: The date of Easter Vigil.
        """
        return self.easter - timedelta(days = 1) # Easter Vigil is the day before Easter.

    @property
    def EasterSunday(self) -> date:
        """
        This property calculates the date of Easter Sunday. Easter Sunday is the first day of Eastertide. It is the day of joy and celebration of the Resurrection of the Lord Jesus Christ, who "is risen from the dead, trampling down death by death, and upon those in the tombs bestowing life" (Orthodox Paschal Troparion). This is the first day the Regina Coeli prayer is prayed.
        It is the last day of the Paschal Triduum (aka the Easter Triduum) and the First Day of Eastertide. 
        
        Despite having one de jure Vespers on Easter Day evening, its de jure vespers (which ends the Holy Week and The Triduum) is the de facto Second Vespers of Easter Day (as the de facto First Vespers of Easter is de jure the Vespers of Holy Saturday, the sad vespers which precedes the Easter Vigil). 
        The sad First Vespers of Easter (aka the Vespers of Holy Saturday) is the only canonical equivalent to the Saturday anticipatory Mass due to the Vatican directive that Easter Vigil must start at nightfall of Holy Saturday.
        On Easter Sunday, it is the only Sunday in which the weekly Sunday Papal Angelus-Regina Coeli speech is omitted. The first Papal Regina Coeli speech of the year will be delivered on the next day, Easter Monday. Instead, on Easter Day, the Pope will give Urbi et Orbi blessing (he also gives it on Christmas Day later in the calendar year). The last Angelus speech before Easter is on Palm Sunday, the next Angelus speech after that is on Trinity Sunday.
        
        Note:
            In addition of Alleluia overload (because of Eastertide requirements), the sequence hymn is Victimae Paschali.
            If in the afternoon, read: Luke 24:13-35 (Road to Emmaus)
        
        Gospel Reading (#42): John 20:1-9 - The Resurrection of the Lord Jesus Christ According to John
        
        Returns:
            date: The date of Easter Sunday.
        """
        return self.easter # Easter Sunday is the first day of Eastertide.
    @property
    def secondSunday(self) -> date:
        """
        This property calculates the date of the second Sunday of Eastertide. It is the Sunday after Easter Sunday. This Sunday is also known as Quasimodo Sunday and Low Sunday. Also it is the Divine Mercy Sunday, which is the principal feast day of the Divine Mercy devotion which the developer is a devotee of since he was in Gia Định Special School (a school for the disabled, owned by the Catholic Church in Vietnam, where the developer was a student from 2007 to 2012).
        
        Before the Divine Mercy Sunday, the Church prays the Novena of the Divine Mercy starting from Good Friday and ending on Easter Saturday (the Saturday after Easter Sunday, not to be confused with Holy Saturday, the second day of the novena). (The novena may be prayed in any day outside prescribed days of the novena, i.e. outside the days between Good Friday and Easter Saturday, inclusive, coz all novenae can be prayed in any day in addition to the novenae with has no prescribed days [eg. Novena of Our Mother of Perpetual Help, Novena to St Jude, etc].)
        
        Gospel Reading (##43-45): John 20:19-31 - The Appearance of the Risen Lord Jesus Christ to the Disciples
        (Note, although the Gospel reading is the same every year, the preceding readings [i.e. the Acts (since Eastertide forbids OT readings) and epistle] is different per lectionary year.)
        
        Returns:
            date: The date of the second Sunday of Eastertide.
        """
        return self.easter + timedelta(days = 7) # The second Sunday of Eastertide is the Sunday after Easter Sunday.
    @property
    def thirdSunday(self) -> date:
        """
        This property calculates the date of the third Sunday of Eastertide. This Sunday is also known as Jubilate Sunday. The Gospel Reading is about post-resurrectional appearances of Jesus.
        
        Gospel Reading:
        - A: Luke 24:13-35 (#46) - Road to Emmaus
        - B: Luke 24:35-48 (#47) - The Appearance of the Risen Lord Jesus Christ to the Disciples
        - C: John 21:1-19 (#48) - Fishing with the Risen Lord
        
        Returns:
            date: The date of the third Sunday of Eastertide.
        """
        return self.easter + timedelta(days = 14) # The third Sunday of Eastertide is 14 days after Easter Sunday.
    
    @property
    def fourthSunday(self) -> date:
        """
        This property calculates the date of the fourth Sunday of Eastertide. It is also known as Misericordia Sunday and Good Shepherd Sunday (hence being the World Day of Vocations). The Gospel Reading is sourced from John 10.
        
        Gospel Reading:
        - A: John 10:1-10 (#49) - Gate of Life
        - B: John 10:11-18 (#50) - Good Shepherd
        - C: John 10:27-30 (#51) - On Hanukkah: "I and Father Are One"
        
        Returns:
            date: The date of the fourth Sunday of Eastertide.
        """
        return self.easter + timedelta(days = 21) # The fourth Sunday of Eastertide is 21 days after Easter Sunday.
    
    @property
    def fifthSunday(self) -> date:
        """
        This property calculates the date of the fifth Sunday of Eastertide. It is also known as Cantate Sunday. The Gospel reading is excerpted from the Farewell Discourse (John 14-17) as well as the initial discourse in the Upper Room (John 13:31-38).
        
        Gospel Reading:
        - A: John 14:1-12 (#52) - The Promise of the Father
        - B: John 15:1-8 (#53) - The Vine and the Branches
        - C: John 13:31-33a, 34-35 (#54) - The New Commandment
        """
        return self.easter + timedelta(days = 28) # The fifth Sunday of Eastertide is 28 days after Easter Sunday.
    
    @property
    def sixthSunday(self) -> date:
        """
        This property calculates the date of the sixth Sunday of Eastertide. It is also known as Vocem Jucumditatis Sunday. The Gospel reading is sourced from the Farewell Discourse (John 14-17). 
        This Sunday is also known as Rogation Sunday, due to the 3 days following it are Rogation Days (Rogation Monday, Rogation Tuesday and Rogation Wednesday) in addition to Saint Mark's Day (25 April, the Great Rogation Day), where priests bless the crops.
        
        Gospel Reading:
        - A: John 14:15-21 (#55) - The Comforter Is Coming
        - B: John 15:9-17 (#56) - Love Each Other
        - C: John 14:23-29 (#57) - The Witnessing Comforter
        
        Note:
            In where Ascension is transferred to Sunday (`ascensionThursday` is `False`), the readings from the 7th Sunday of Eastertide (sourced from John 17) is sometimes read on this day instead.
        """
        return self.easter + timedelta(days = 35) # The sixth Sunday of Eastertide is 35 days after Easter Sunday.
    
    @property
    def Ascension(self) -> date:
        """
        This property calculates the date of Ascension Day, commemorating the Ascension of the Lord Jesus Christ into heaven.
        
        It is celebrated on the 40th day after Easter Sunday in France, England, Germany, Austria, Switzerland, Northeast USA, North Vietnam, etc; but Sunday in most of the rest of the world, including South Vietnam.
        
        Gospel Reading (#58):
        - A: Matthew 28:16-20 - The Great Commission
        - B: Mark 16:15-20 - The Great Commission
        - C: Luke 24:46-53 - The Ascension of the Lord
        """
        return self.easter + timedelta(days = 39 if self.ascensionThursday else 42) # Ascension Day is the 40th day after Easter Sunday if Ascension is celebrated on Thursday, otherwise it is the 43rd day after Easter Sunday.
    
    @property
    def seventhSunday(self) -> date:
        """
        This property calculates the date of the seventh Sunday of Eastertide. It is also known as Exaudi Sunday. The Gospel reading is sourced from the conclusion of the Farewell Discourse (John 14-17), Jesus' own High Priestly Prayer in John 17, which is probably said peradventure from Upper Room to Gethsemane (cf. John 14:31b), where the events of John 15-17 take place. 
        This Sunday is celebrated if and only if Ascension is celebrated on Thursday (`ascensionThursday` is `True`), otherwise it is not celebrated.
        This Sunday is also known as the World Communication Sunday regardless of whether Ascension is celebrated on Thursday or Sunday.
        
        Gospel Reading:
        - A: John 17:1-11a (#59) - Dad, Glorify Me!
        - B: John 17:11b-19 (#60) - Glorify Me in Them that They May Be One
        - C: John 17:20-26 (#61) - I'm in My Disciples
        
        Returns:
            date: The date of the seventh Sunday of Eastertide.
        """
        return self.easter + timedelta(days = 42) if self.ascensionThursday else None
        # The seventh Sunday of Eastertide is 42 days after Easter Sunday if Ascension is celebrated on Thursday, otherwise it is not celebrated (None is returned). 
    
    @property
    def pentecost(self) -> date:
        """
        This property calculates the date of Pentecost. Pentecost is the day of the descent of the Holy Spirit upon the Apostles and the Church. It is celebrated on the 50th day after Easter Sunday and the conclusion of Eastertide. Red vestments are worn on this day, as red is the color of the Holy Spirit.
        
        After Pentecost Sunday, the Church returns to Ordinary Time with the day following Pentecost is the Memorial of Mary, Mother of the Church. After Pentecost there are be Ember days on Wednesday, Friday and Saturday.
        
        Note:
            On some parishes, the Vigil of Pentecost is celebrated on the previous day, which is the day before Pentecost Sunday. But in most parishes else, the Mass of the Day of Pentecost is used on the evening before Pentecost Sunday.
            The sequence hymn is Veni Sancte Spiritus.
            After Pentecost Sunday, the Easter Candle is extinguished and placed in baptismal font.
            The Pentecost Sunday is the Apodosis (Leavetaking) of Regina Coeli, because Angelus returns the next day on the following day, Pentecost Monday, the Memorial of Mary, Mother of the Church and the resumption of the Ordinary Time.
        
        Gospel Reading:
        - Vigil: John 7:37-39 (#62) - The Promise for the Holy Spirit
        - Day: John 20:19-23 (#63) - Receive the Holy Spirit!
        - OPTIONAL Gospel for Year B: John 15:26-27; 16:12-15 - The Spirit of Truth
        - OPTIONAL Gospel for Year C: John 14:15-16, 23b-26 - Holy Spirit the Comforter
        
        Returns:
            date: The date of Pentecost.
        """
        return self.easter + timedelta(days = 49) # Pentecost is the 50th day after Easter Sunday.
    
class SolemnitiesoftheLord:
    """
    This class calculates the dates of the Solemnities of the Lord after Pentecost Sunday for a given year, hence being dependent to the date of Easter.
    This calculates the 3 Solemnities of the Lord after Pentecost Sunday: Trinity Sunday, Corpus Christi and Sacred Heart. White vestments are worn on all 3 Solemnities.
    """
    def __init__(self, year, calendar = True, corpusChristionThursday = False):
        """
        This method initializes the Solemnities of the Lord class.
        
        Args:
            year (int): The year to calculate the Solemnities of the Lord for. Note that the input year is for liturgical year, since the liturgical year always starts on the first Sunday of Lent of the previous calendar year.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar, but Julian Easter if before 1583).
            corpusChristionThursday (bool): Corpus Christi is celebrated on Thursday after Trinity in Germany, Brazil, Australia, etc; but Sunday in most of the rest of the world, including USA, Vietnam, England, France, etc.
        """
        self.year = year # The input year is for liturgical year.
        self.easter = easterdate(year, calendar) # Calculate the date of Easter for the given year.
        self.corpusChristionThursday = corpusChristionThursday # Whether to include Corpus Christi in the Solemnities of the Lord.
        
    @property
    def Trinity(self) -> date:
        """
        This property calculates the date of Trinity Sunday. Trinity Sunday is the Sunday after Pentecost Sunday. It commemorates the mystery of the Most Holy Trinity: Father, Son and Holy Spirit.
        
        Note:
            On some parishes, the Athanasian Creed is read near the end of Lauds of Trinity Sunday (due to the 1960 pre-Vatican II rubric that the Athanasian Creed is the exclusive proper to Trinity Sunday).
            For the first time after Palm Sunday, the Papal Angelus speech is resumed after Eastertide pause.
        
        Gospel Readings:
        - A: John 3:16-18 (#164) - The Love of Triune God for the World
        - B: Matthew 28:16-20 (#165) - Baptize in Trinity's Name
        - C: John 16:12-15 (#166) - The Spirit of Truth
        """
        return self.easter + timedelta(days = 56) # Trinity Sunday is 56 days after Easter Sunday.
    
    @property
    def CorpusChristi(self) -> date:
        """
        This property calculates the date of Corpus Christi. Corpus Christi is the Sunday after Trinity Sunday. It commemorates the mystery of the Most Holy Body and Blood of Christ as well as the real presence of Christ in the Eucharist. 
        Unlike Maundy Thursday, which commemorates the institution of the Eucharist, and has Eucharistic adoration in altar of repose (where the Blessed Sacrament is reserved but not adored in monstrance), Corpus Christi commemorates the real presence of Christ in the Eucharist and hence Eucharistic adoration in monstrance as well as pomp and circumstance of Eucharistic processions.
        
        Note:
            Corpus Christi is celebrated on Thursday after Trinity in Germany, Brazil, Australia, etc; but Sunday after Trinity (i.e. the second Sunday after Pentecost Sunday) in most of the rest of the world, including USA, Vietnam, England, France, etc.
        
        Gospel Readings:
        - A: John 6:51-58 (#167) - The Bread of Life
        - B: Mark 14:12-16, 22-26 (#168) - The First Mass
        - C: Luke 9:11b-17 (#169) - The Eucharistic Meal with the 5000
        """
        return self.easter + timedelta(days = 60 if self.corpusChristionThursday else 63)
        # Corpus Christi is 60 days after Easter Sunday if Corpus Christi is celebrated on Thursday, otherwise it is 63 days after Easter Sunday. 
    
    @property
    def SacredHeart(self) -> date:
        """
        This property calculates the date of Sacred Heart. Sacred Heart is the Friday after the second Sunday after Pentecost Sunday. It commemorates the mystery of the Sacred Heart of Jesus Christ as well as His unconditional love for the world. This Friday is also the World Day of Sanctification of Priests.
        
        Gospel Readings:
        - A: Matthew 11:25-30 (#170) - The Heart of Gold
        - B: John 19:34-37 (#171) - The Pierced Heart
        - C: Luke 15:3-7 (#172) - The Searching Heart for the Lost Sheep
        """
        return self.easter + timedelta(days = 68) # Sacred Heart is 68 days after Easter Sunday.

class LentenEastertide_Holidays:
    """
    This class calculates the dates of the Lenten Eastertide Holidays for a given year.
    """
    def __init__(self, year, calendar = True):
        """
        This method initializes the Lenten Eastertide Holidays class.
        
        Args:
            year (int): The year to calculate the Lenten Eastertide Holidays for. Note that the input year is for liturgical year, since the liturgical year always starts on the first Sunday of Lent of the previous calendar year.
            calendar (bool): Whether to return the date in the Gregorian calendar. Default is True (Gregorian calendar, but Julian Easter if before 1583).
        """
        self.year = year # The input year is for liturgical year.
        self.easter = easterdate(year, calendar) # Calculate the date of Easter for the given year.
    @property
    def SaintJoseph(self) -> date:
        """
        This property calculates the date of Saint Joseph. Saint Joseph is the patron saint of the Church as well as Vietnam. He is the foster father of Jesus Christ. Although the Bible didn't record his words, his recorded acts makes him a model of a perfect husband and father.
        
        Note:
            - Unless 19 March falls on a Sunday or during Holy Week (including Palm Sunday), since 19 March is always before the earliest possible Easter (22 March), Saint Joseph's day is celebrated on 19 March.
            - If 19 March falls on a Sunday in Lent (except Palm Sunday), Saint Joseph's day is celebrated on the following day, 20 March.
            - But should 19 March fall on Holy Week and Palm Sunday, Saint Joseph's day is celebrated on the Saturday before Palm Sunday (e.g. 2008 Saint Joseph's Day was 15 March due to 19 March was Spy Wednesday).
            
        Gospel Reading (#543):
        - Matthew 1:16, 18-21 - How Joseph Became the Father of Jesus Christ
        - Luke 2:41-51 - Lost in the Temple
        
        Returns:
            date: The date of Saint Joseph.
        """
        joseph = date(self.year, 3, 19)
        if joseph.weekday() == 6: # Sunday in Lent (except Palm Sunday)
            return joseph + timedelta(days = 1)
        elif self.easter < date(self.year, 3, 27): 
            # Palm Sunday and Holy Week, Saint Joseph is celebrated on the Saturday before Palm Sunday (8 days before Easter)
            # If Easter is 22 March -> Saint Joseph is 14 March
            # If Easter is 23 March -> Saint Joseph is 15 March (worked example in 2008)
            # If Easter is 24 March -> Saint Joseph is 16 March
            # If Easter is 25 March -> Saint Joseph is 17 March
            # If Easter is 26 March -> Saint Joseph is 18 March
            return self.easter - timedelta(days = 8)
        else:
            return joseph
    @property
    def Annunciation(self) -> date:
        """
        This property calculates the date of the Annunciation. The Annunciation is the day the Virgin Mary was visited by the angel Gabriel and told she would conceive and bear a son, Jesus Christ.
        
        Gospel Reading (#545): Luke 1:26-38 - The Annunciation of the Virgin Mary
        
        Note:
            - Unless 25 March falls on a Sunday or during Holy Week (including Palm Sunday), since 25 March is always after the earliest possible Easter (22 March), the Annunciation is celebrated on 25 March.
            - If 25 March falls on a Sunday in Lent (except Palm Sunday), the Annunciation is celebrated on the following day, 26 March, the anniversary of Ho Chi Minh Communist Youth Union.
            - But should 25 March fall on Holy Week and Palm Sunday, the Annunciation is celebrated on the Monday after Divine Mercy Sunday, with Angelus traded for Regina Caeli (since we must not recite Angelus during Eastertide). (e.g. 2024 Annunciation was 8 April due to 25 March was Holy Monday)
        
        Returns:
            date: The date of the Annunciation.
        """
        annunciation = date(self.year, 3, 25)
        if annunciation.weekday() == 6: # Sunday in Lent (except Palm Sunday)
            return annunciation + timedelta(days = 1)
        elif self.easter < date(self.year, 4, 2):
            # Palm Sunday and Holy Week, the Annunciation is celebrated on the Monday after Divine Mercy Sunday (8 days after Easter)
            # If Easter is 22 March -> Annunciation is 30 March
            # If Easter is 23 March -> Annunciation is 31 March (worked example in 2008)
            # If Easter is 24 March -> Annunciation is 1 April
            # If Easter is 25 March -> Annunciation is 2 April
            # If Easter is 26 March -> Annunciation is 3 April
            # If Easter is 27 March -> Annunciation is 4 April (worked example in 2016)
            # If Easter is 28 March -> Annunciation is 5 April (worked example in 2026)
            # If Easter is 29 March -> Annunciation is 6 April
            # If Easter is 30 March -> Annunciation is 7 April
            # If Easter is 31 March -> Annunciation is 8 April (worked example in 2024)
            # If Easter is 1 April -> Annunciation is 9 April (latest possible Annunciation, worked example in 2018)
            return self.easter + timedelta(days = 8)
        else:
            return annunciation

def HolyFire(year):
    """
    This property calculates the date of Holy Fire Saturday. It is the day before Julian Easter where the miracle of the Holy Fire occurs in the Church of the Holy Sepulcher in Jerusalem.
    Note: For Catholic Christians, unless Gregorian and Julian Easters coincide (as it did on 19 April 2025), there cannot be a Holy Fire on Gregorian Holy Saturday due to being an Orthodox-exclusive liturgical practice (e.g: in 2024, Holy Saturday was 30 March, but it wasn't until 4 May did the Holy Fire occur 5 weeks later; in 2026, Holy Saturday will be 4 April, but it won't until 11 April will the Holy Fire occur the next week).
    Returns:
        date: The date of Holy Fire Saturday.
    """
    return easterdate(year, False) - timedelta(days = 1) 
    # Holy Fire Saturday is the day before Julian Easter.
    
if __name__ == "__main__": # Testing program, testing all the dates of the Lent, Eastertide, Solemnities of the Lord and Holy Fire Saturday for any proleptic Gregorian calendar year.
    year = 2024
    lent = Lent(year)
    eastertide = Eastertide(year)
    solemnitiesofthelord = SolemnitiesoftheLord(year)
    lentenEastertideHolidays = LentenEastertide_Holidays(year)
    seventhSunday = Eastertide(year, ascensionThursday = True).seventhSunday
    holyFire = HolyFire(year)
    print(f"Liturgical Year: {year}")
    print(f"Ash Wednesday: {lent.AshWednesday}")
    print(f"First Sunday of Lent: {lent.FirstSunday}")
    print(f"Second Sunday of Lent: {lent.SecondSunday}")
    print(f"Third Sunday of Lent: {lent.ThirdSunday}")
    print(f"Fourth Sunday of Lent: {lent.FourthSunday}")
    print(f"Fifth Sunday of Lent: {lent.FifthSunday}")
    print(f"Saint Joseph: {lentenEastertideHolidays.SaintJoseph}")
    print(f"Palm Sunday: {lent.PalmSunday}")
    print(f"Maundy Thursday: {lent.MaundyThursday}")
    print(f"Good Friday: {lent.GoodFriday}")
    print(f"Holy Saturday: Day of {lent.HolySaturday}")
    print(f"Easter Vigil: Night of {eastertide.EasterVigil}")
    print(f"Easter Sunday: {eastertide.EasterSunday}")
    print(f"Divine Mercy Sunday: {eastertide.secondSunday}")
    print(f"Annunciation: {lentenEastertideHolidays.Annunciation}")
    print(f"Third Sunday of Eastertide: {eastertide.thirdSunday}")
    print(f"Fourth Sunday of Eastertide: {eastertide.fourthSunday}")
    print(f"Fifth Sunday of Eastertide: {eastertide.fifthSunday}")
    print(f"Sixth Sunday of Eastertide: {eastertide.sixthSunday}")
    print(f"Ascension Day: {eastertide.Ascension}")
    print(f"Seventh Sunday of Eastertide: {seventhSunday}")
    print(f"Pentecost: {eastertide.pentecost}")
    print(f"Trinity Sunday: {solemnitiesofthelord.Trinity}")
    print(f"Corpus Christi: {solemnitiesofthelord.CorpusChristi}")
    print(f"Sacred Heart: {solemnitiesofthelord.SacredHeart}")
    print(f"--------------------------------")
    print(f"Holy Fire Saturday: {holyFire}")
    if (easterdate(year,False) - easterdate(year)).days // 7 != 0:
        print(f"Julian Easter: {easterdate(year, False)}") 
        print(f"({(easterdate(year,False) - easterdate(year)).days // 7} week{"s" if (easterdate(year,False) - easterdate(year)).days // 7 > 1 else ""} later)")
    else:
        print("Double Easter: Gregorian and Julian Easters coincide")