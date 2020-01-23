# Write your mean_fits function here:
# Write your load_fits function here.
import numpy as np
from astropy.io import fits


def mean_fits(fits_files_list):
    fits_data = np.zeros((200, 200), dtype=np.int32)
    for fits_file in fits_files_list:
        hdu_list = fits.open(fits_file)
        fits_data = fits_data + hdu_list[0].data
    fits_data = fits_data / len(fits_files_list)
    return fits_data


if __name__ == '__main__':
    # Test your function with examples from the question
    data = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    print(data[100, 100])

    # You can also plot the result:
    import matplotlib.pyplot as plt

    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()