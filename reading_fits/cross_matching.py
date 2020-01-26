# Write your crossmatch function here.
import numpy as np

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


def import_super():
    cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
    res = []
    for i in range(len(cat)):
        row = (i + 1, cat[i][0], cat[i][1])
        res.append(row)
    return res


def angular_dist(ra1, dec1, ra2, dec2):
    # Convert to radians
    r1 = np.radians(ra1)
    d1 = np.radians(dec1)
    r2 = np.radians(ra2)
    d2 = np.radians(dec2)

    deltar = np.abs(r1 - r2)
    deltad = np.abs(d1 - d2)
    angle = 2 * np.arcsin(np.sqrt(np.sin(deltad / 2) ** 2
                                  + np.cos(d1) * np.cos(d2) * np.sin(deltar / 2) ** 2))

    # Convert back to degrees
    return np.degrees(angle)


def crossmatch(cat1, cat2, max_radius):
    matches = []
    no_matches = []
    for id1, ra1, dec1 in cat1:
        closest_dist = np.inf
        closest_id2 = None
        for id2, ra2, dec2 in cat2:
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < closest_dist:
                closest_id2 = id2
                closest_dist = dist

        # Ignore match if it's outside the maximum radius
        if closest_dist > max_radius:
            no_matches.append(id1)
        else:
            matches.append((id1, closest_id2, closest_dist))

    return matches, no_matches


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    bss_cat = import_bss()
    super_cat = import_super()

    # First example in the question
    max_dist = 40 / 3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(no_matches))

    # Second example in the question
    max_dist = 5 / 3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(no_matches))
