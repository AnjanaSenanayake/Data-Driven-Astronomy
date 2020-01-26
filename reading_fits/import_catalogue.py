# Write your import_bss function here.
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


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Output of the import_bss and import_super functions
    bss_cat = import_bss()
    super_cat = import_super()
    print(bss_cat)
    print(super_cat)