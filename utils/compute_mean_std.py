from glob import glob
from skimage import io
import numpy as np
from tqdm import tqdm

images = glob(r"C:\Users\Ramzan\Documents\Self Supervised Learning\dataset\flowers\*\*.jpg")
for i, im_name in enumerate(images):
    image = io.imread(im_name)
    image = image/255

    if i == 0:
        mean = np.mean(image, axis=(0, 1), keepdims=True)
        std_dev = np.std(image, axis=(0,1), keepdims=True)

        print(mean.shape)
        print(mean)
        print(std_dev)
        break

    else:
        mean = np.append(mean, np.mean(image, axis=(0,1), keepdims=True), axis=0)
        std_dev = np.append(std_dev, np.std(image, axis=(0, 1), keepdims=True), axis=0)

print(np.mean(mean, axis=(0,1)))
print(np.mean(std_dev, axis=(0,1)))
