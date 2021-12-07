import numpy as np
import os
import tkinter
import scipy
import scipy.io

current_path = os.getcwd()
new_path = "../images"
market_path = '/Market-1501_Attribute-master/gallery_market.mat'
print(new_path)

scipy.io.loadmat('gallery_market.mat')