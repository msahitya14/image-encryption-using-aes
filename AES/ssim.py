from skimage import measure
from skimage import metrics
import cv2
import sewar
from sewar.full_ref import uqi

# 2. Construct the argument parse and parse the arguments


# 3. Load the two input images
imageA = cv2.imread("parrot.jpg")
imageB = cv2.imread("decryptedImage.png")

# 4. Convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 5. Compute the Structural Similarity Index (SSIM) between the two
#    images, ensuring that the difference image is returned
uqi1 = uqi(imageA, imageB)
(score, diff) = metrics.structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

# 6. You can print only the score if you want
print("SSIM: {}".format(score))
print("UQI: {}".format(uqi1))
