

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/devz/data/messi5.jpg',0)

plt.imshow(img,cmap='gray', interpolation = 'bicubic')
plt.xticks([])
plt.xticks([])
plt.show()


