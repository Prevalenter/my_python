import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np
from scipy.ndimage import binary_fill_holes,label,generate_binary_structure,distance_transform_edt
from skimage.morphology import watershed
from skimage.measure import regionprops
from skimage.filters import  sobel
