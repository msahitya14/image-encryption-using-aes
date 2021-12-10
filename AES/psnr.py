
from math import log10, sqrt
import cv2
import numpy as np


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def main():
    original = cv2.imread("parrot.jpg")
    compressed = cv2.imread("decryptedImage.png", 1)
    value = PSNR(original, compressed)
    print(f"PSNR value is {value} dB")


if __name__ == "__main__":
    main()
