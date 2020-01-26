# Write your find_closest function here
import numpy as np


def angular_dist(r1, d1, r2, d2):
    r1 = np.radians(r1)
    d1 = np.radians(d1)
    r2 = np.radians(r2)
    d2 = np.radians(d2)
    x = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1 - r2) / 2) ** 2
    y = np.sin(np.abs(d1 - d2) / 2) ** 2
    result = 2 * np.arcsin(np.sqrt(x + y))
    return np.degrees(result)


def hms2dec(h, m, s):
    return 15 * (h + m / 60 + s / (3600))


def dms2dec(h, m, s):
    if h > 0:
        return (h + m / 60 + s / (3600))
    else:
        return -(-h + m / 60 + s / (3600))


def import_bss():
    cat = np.loadtxt('bss.dat', usecols=range(1, 7))
    res = []
    for i in range(len(cat)):
        hms = hms2dec(cat[i][0], cat[i][1], cat[i][2])
        dms = dms2dec(cat[i][3], cat[i][4], cat[i][5])
        row = (i + 1, hms, dms)
        res.append(row)
    return res


def find_closest(cat, ra, dec):
    dist = np.inf
    id = 0
    for (id1, ra1, dec1) in cat:
        ang_dist = angular_dist(ra1, dec1, ra, dec)
        if dist > ang_dist:
            id = id1
            dist = ang_dist
    return id, dist


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    cat = import_bss()

    # First example from the question
    print(find_closest(cat, 175.3, -32.5))

    # Second example in the question
    print(find_closest(cat, 32.2, 40.7))