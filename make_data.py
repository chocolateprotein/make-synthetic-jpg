
import cv2
import math
import numpy as np
from PIL import Image
import os
from tqdm import tqdm

#만들 데이터를 입력
root = '/Users/test/Desktop/다양한 형태의 한글 문자 OCR/Training/원천/008' 
files = os.listdir(root)
os.chdir(root)
backgrnd_img = '/Users/test/synthetic/낙서2.png'
for foregrnd_img in tqdm(files) :
    if '.jpg' not in foregrnd_img:
        continue
    backgrnd_img = '/Users/test/synthetic/낙서2.png'

    def convertTransparent(path):
        img = Image.open(path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                                newData.append((255, 255, 255, 0))
            else:
                if item[0] > 255:
                                newData.append((0, 0, 0, 255))
                else:
                    newData.append(item)
        img.putdata(newData)

        return img

    #앞으로 넣을 글씨사진 입력(numpy로 받은후에 나중에 합쳐짐)
    fore_img = np.array(convertTransparent(foregrnd_img))
    fore_height, fore_width, fore_channels = fore_img.shape

    #배경 사진 입력
    backgrnd_img = cv2.imread(backgrnd_img)
    backgrnd_height, backgrnd_width, backgrnd_channels = backgrnd_img.shape

    fore_img = cv2.resize(fore_img,(3000,3000))
    backgrnd_img = cv2.resize(backgrnd_img,(3000,3000))
    # 이미지 리사이징 백그라운드와 


    if fore_channels < 4:
        fore_img = cv2.cvtColor(fore_img, cv2.COLOR_BGR2BGRA)

    # check if backgrnd_img as same channels as foregrnd_img
    if backgrnd_channels < 4:
        backgrnd_img = cv2.cvtColor(backgrnd_img, cv2.COLOR_BGR2BGRA)


            #사이즈 체크
            #print(fore_img.shape)
            #print(backgrnd_img.shape)


    # set the x-y off-set 말만 번지르르하지 이건 그냥 x,y축을 맞추는것이다!
        y1 = 0
        y2 = fore_img.shape[0] 
        x1 = 0
        x2 = fore_img.shape[1]
        alpha_fore_img = fore_img[:, :, 3] / 255.0 
        alpha_l =  1.0 - alpha_fore_img


    # create RGBA image  위에 값 설정에 따라서 위치가 바뀐다, 실행해봤다. 
    for c in range(0, 3):
        backgrnd_img[y1:y2, x1:x2, c] = (alpha_fore_img * fore_img[:, :, c] + alpha_l * backgrnd_img[y1:y2, x1:x2, c])
                    

    # save the image
    fResult = foregrnd_img
    # print(fResult)

    cv2.imwrite(fResult, backgrnd_img)
    