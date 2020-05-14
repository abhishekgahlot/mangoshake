import pathlib
import IPython.display as display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = pathlib.Path('./positions')

image_count = len(list(data_dir.glob('*/*.png')))

CLASS_NAMES = np.array([item.name for item in data_dir.glob('*') if item.name != ".DS_Store"])

print(image_count, CLASS_NAMES)