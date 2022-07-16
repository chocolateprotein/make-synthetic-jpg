from tkinter import image_names
import cv2
import math
import numpy as np
from PIL import Image
import os
from tqdm import tqdm

#만들 데이터를 입력
#roots = ['/Users/test/synthetic/낙서1.jpg']
root = '/Users/test/synthetic/낙서1.jpg'
#for root in roots :
files = os.listdir(root)
new = os.path.join(files,root)
print(new)
for foregrnd_img in tqdm(new) :
    if '.jpg' not in foregrnd_img:
        continue
    
    image = cv2.imread(foregrnd_img)
    image = cv2.resize(image,(2480,3508))
    fResult = foregrnd_img
    cv2.imwrite(fResult ,image )