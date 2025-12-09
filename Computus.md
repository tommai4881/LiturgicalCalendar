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
    if march > 31: return (april, 4)
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
    if march > 31: return (april, 4)
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
    if march > 31: return (april, 4)
    else: return (march, 3)
```
### Bradleyan Computus (by James Bradley, from Calendar (New Style) Act 1750 and Book of Common Prayer)
```python
def Bradley(year):
    g = year % 19 + 1
    k = year // 100
    s = k - 16 - (k - 16) // 4
    l = 8 * (k - 14) // 25
    c = s - l # Cypher
    p = (3 - 11 * g + c) % 30 if year > 1582 else (26 - 11 * g) % 30 # Paschal full moon
    if p == 29 or (p == 28 and g > 11): p -= 1 # Edge case
    d = (year + year // 4 - k + k // 4) % 7 if year > 1582 else (year + year // 4 + 5) % 7 # DOW of January 1
    march = p + 22 + (4 - d - p) % 7
    april = p - 9 + (4 - d - p) % 7
    if march > 31: return (april, 4)
    else: return (march, 3)    
```

## Modern Easter Algorithms
### Gaussian Computus (by Carl Friedrich Gauss 1800, 1816):
```python
def Easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (8 * k + 13) // 25
    q = k // 4
    m = (15 + k - p - q) % 30 if year > 1582 else 15 # Lunar constant
    n = (4 + k - q) % 30 if year > 1582 else 6 # Solar constant
    d = (19 * a + m) % 30 # Epact
    if d == 29 or (d == 28 and a > 10): d -= 1 # Edge case
    e = (2 * a + 4 * b + 6 * d + e) % 7 # Days till Easter
    march = d + e + 22
    april = d - e - 9
    if march > 31: return (april, 4)
    else: return (march, 3)
```
### Carterian Computus (from Royal Greenwich Obversatory, 1996, expanded to include Julian and Gregorian dates)
```python
def Carter(y):
    a = y % 19
    k = y // 100
    s = k - k // 4 - 12 # Solar correction
    m = 8 * (k - 14) // 25 # Lunar correction
    b = 202 + s - m - 11 * a if y > 1582 else 225 - 11 * a
    d = b % 30 + 21 # PFM
    # Simpler: d = (19 * a + 22 + s - m) % 30 + 21 (eliminating b)
    if d == 50 or (d == 49 and a > 10): d -= 1 # Edge case
    e = (y + y // 4 - d - 10 - s) % 7 if y > 1582 else (y + y // 4) % 7
    march = d + 7 - e
    april = d - 24 - e
    if march > 31: return (april, 4)
    else: return (march, 3)
```
### Knuthian Computus (by Donald Knuth)
```python
def Knuth(y):
    golden = y % 19 + 1
    e_1582 = (11 * golden - 10) % 30
    k = y // 100 + 1
    sol = (3 * k) // 4 - 12
    lun = (8 * k + 5) // 25 - 5
    epact = (e_1582 + l - s) % 30 if y > 1582 else (e_1582 + 7) % 30
    if epact == 24 or (epact == 25 and golden > 11): epact += 1 # Edge case
    pfm = 44 - f if f < 24 else 74 - f
    fsd = (10 + sol - (5 * year) // 4) % 7 if y > 1582 else ((-5 * year) // 4) % 7 # First Sunday of March
    dow = (pfm + 7 - fsd) % 7
    march = pfm + 7 - dow
    april = pfm - 24 - dow
    if march > 31: return (april, 4)
    else: return (march, 3)
```
### Oudinian Gregorian Computus (by JM Oudin (1940))
```python
def Oudin(m):
    # m stands for a year
    a = m % 19
    c = m // 100
    k = (c - 17) // 25
    r = (c - c // 4 - (c - k) // 3 + 19 * a + 15) % 30
    if r == 29 or (r == 28 and a > 10): r -= 1
    j = (m + m // 4 + r + 2 - c + c // 4) % 7
    march = 28 + r - j
    april = r - j - 3
    if march > 31: return (april, 4)
    else: return (march, 3)
```
    
