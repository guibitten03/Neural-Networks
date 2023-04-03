
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import io


if __name__ == "__main__":
    lenna_img = io.imread('Lenna.png')
    lenna_gray = rgb2gray(lenna_img)

    peppers_img = io.imread('peppers.jpg')
    peppers_gray = rgb2gray(peppers_img)

    io.imsave("lenna_gray.png", lenna_gray)
    io.imsave("peppers_gray.png", peppers_gray)