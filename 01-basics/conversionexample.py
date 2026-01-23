"""Functions that convert metric and imperial units."""

def cel2fah(c):
    """Converts from celsius to fahrenheit."""
    return 9/5 * c + 32

def fah2cel(f):
    """Converts from fahrenheit to celsius."""
    return 5/9 * (f - 32)

def km2mi(km):
    """Converts from kilometers to miles."""
    return km / 1.60934

def mi2km(mi):
    """Converts from miles to kilometers."""
    return mi * 1.60934

if __name__ == "__main__":

    for c in range(0, 21, 5):
        f = round(cel2fah(c))
        print(f"{c} C is {f} F")

    print()
    for f in range(20, 41, 5):
        c = round(fah2cel(f))
        print(f"{f} F is {c} C")

    print()
    for km in range(1, 6):
        mi = round(km2mi(km), 1)
        print(f"{km} km is {mi} mi")

    print()
    for mi in range(5, 10):
        km = round(mi2km(mi), 1)
        print(f"{mi} mi is {km} km")
