# EASTER COMPUTUS
Comparison of Easter Computus calculations

## Classical Julian Computus
### Catholic Julian Computus
```python
def Julian(year):
    g = year % 19 + 1 # Golden Number
    e = 11 * (g - 1) % 30 # Dionysian Epact (Age of the moon as of 22 March)
    # Simpler epact formula: 11 * (y % 19) % 30
    pfm = 36 - e if e < 16 else 66 - e # Paschal Full Moon
    # If Dionysian epact in Golden Number year = 0 (as of March 22) then Gregorian Lillian epact is 8 (as of January 1)
    dow = (year + year // 4 + pfm) % 7 # Day of the week of PFM
    # With 0 is Sunday, 1 is Monday, etc.
    march = pfm + 7 - dow
    april = pfm - 24 - dow
    if march >= 31: return (april, 4)
    else: return (march, 3)
```
### Julian Typikon Computus
```python
def Typikon(year):
    l = (year + 16) % 19 + 1 # Lunar Cycle
    s = (year + 19) % 28 + 1 # Solar Cycle
    f = (11 * lunar + 3) % 30 # The Foundation (Age of the Moon as of March 1), i.e. the Lilianized Julian Epact
    if l > 16: f = (f + 1) % 30 # Saltus Lunae correction
    # Simple Foundation formula: f = 11 * (y % 19 + 1) % 30
    pfm = 47 - f if f < 27 else 77 - f
    c = (s + s // 4 - 1) % 7 + 1 # Concurrent (dow of March 24)
    m = 4 - c if c < 4 else 11 - c # First Sunday of March
    dow = (pfm - m) % 7
    march = pfm + 7 - dow
    april = pfm - 24 - dow
    if march >= 31: return (april, 4)
    else: return (march, 3)
```

## Classical Gregorian Computus
### Clavian Computus (1581, from Christopher Clavius)
```python
def Clavian(year):
    g = year % 19 + 1
    f = 11 * g % 30 # Foundation
    k = year // 100 # Century
    s = 3 * (k - 15) // 4 # Solar Correction
    l = 8 * (k - 14) // 25 # Lunar Correction
    e = (f - s + l) % 30 # Lilian epact (Age of the moon as of January 1)
    if e == 24 or (e == 25 and g > 11): e += 1 # Edge case coz of epact 25 so that Easter cannot be 26 April
    pfm = 44 - f if f < 24 else 74 - f
    d = k - k // 4 - 2 # Gregorian-Julian day difference
    dow = (year + year // 4 - d + pfm) % 7
    march = pfm + 7 - dow
    april = pfm - 24 - dow
    if march >= 31: return (april, 4)
    else: return (march, 3)
```
### Bradleyan Computus (by James Bradley, from Book of Common Prayer)
```python
def Bradley(year):
    
```