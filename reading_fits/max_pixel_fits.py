# Write your load_fits function here.
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


def load_fits(fits_file):
    hdu_list = fits.open(fits_file)
    hdu = hdu_list[0].data
    max_ind = np.unravel_index(np.argmax(hdu, axis=None), hdu.shape)
    return max_ind


if __name__ == '__main__':
    # Run your `load_fits` function with examples:
    bright = load_fits('image1.fits')
    print(bright)

    # You can also confirm your result visually:
    hdu_list = fits.open('image1.fits')
    data = hdu_list[0].data

    # Plot the 2D image data
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()


