# Write your function median_FITS here:
import numpy as np
from astropy.io import fits
import time
import sys


def median_fits(fits_files):
    fits_median_image = np.zeros((200, 200))
    median_arr = np.zeros(len(fits_files))
    fits_data = np.zeros((len(fits_files), 200, 200))
    l = 0;
    start = time.perf_counter()
    for fits_file in fits_files:
        hdu_list = fits.open(fits_file)
        fits_data[l] = hdu_list[0].data
        l = l + 1
    for i in range(200):
        for j in range(200):
            for k in range(len(fits_files)):
                median_arr[k] = fits_data[k][i][j]
            median_arr.sort()
            mid = len(median_arr) // 2
            median = (-0.5) * (len(median_arr) % 2 - 1) * (median_arr[mid - 1] - median_arr[mid]) + median_arr[mid]
            fits_median_image[i][j] = median
    eval_time = start = time.perf_counter() - start
    mem_size = sys.getsizeof(fits_data) / 1024
    return fits_median_image, eval_time, round(mem_size * 2) / 2


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with first example in the question.
    result = median_fits(['image0.fits', 'image1.fits'])
    print(result[0][100, 100], result[1], result[2])

    # Run your function with second example in the question.
    result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
    print(result[0][100, 100], result[1], result[2])