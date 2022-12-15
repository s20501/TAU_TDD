def roman(n: int):
    if n < 1:
        return ""
    if n >= 1000:
        return "M" + roman(n - 1000)
    if n >= 900:
        return "CM" + roman(n - 900)
    if n >= 500:
        return "D" + roman(n - 500)
    if n >= 400:
        return "CD" + roman(n - 400)
    if n >= 100:
        return "C" + roman(n - 100)
    if n >= 90:
        return "XC" + roman(n - 90)
    if n >= 50:
        return "L" + roman(n - 50)
    if n >= 40:
        return "XL" + roman(n - 40)
    if n >= 10:
        return "X" + roman(n - 10)
    if n >= 9:
        return "IX" + roman(n - 9)
    if n >= 5:
        return "V" + roman(n - 5)
    if n >= 4:
        return "IV" + roman(n - 4)
    if n >= 1:
        return "I" + roman(n - 1)
