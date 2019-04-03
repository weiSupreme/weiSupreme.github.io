import os
import cv2
import random
import numpy as np
import math

colors = [[0, 0, 0]]
ratios = [1.0, 0.8, 0.6, 0.5, 0.4, 0.3, 0.25]
resize_heights = [320, 384, 448, 512]
coorddis = 90
chardis = 4


def FindCoord(img):
    y, x = (img < 254).nonzero()
    return x, y, min(x), min(y), max(x), max(y)


def Overlap(ylimits, y):
    if len(ylimits) > 0:
        for ylimit in ylimits:
            if y >= ylimit[0] and y <= ylimit[1]:
                return True
        return False
    else:
        return False


def Cover(ylimits, yy):
    if len(ylimits) > 0:
        for ylimit in ylimits:
            if yy[0] <= ylimit[0] and yy[1] >= ylimit[1]:
                return True
        return False
    else:
        return False


bgimgs = os.listdir('bg_img')
sps=random.sample(bgimgs,5000)
for iter in range(1):
    for bgimgn in sps:
        print(bgimgn)
        bgimg = cv2.imread('bg_img/' + bgimgn)
        txt = open('syn_img_label/' + bgimgn.split('.')[0] + '_'+str(iter)+'.txt', 'w')
        #txt=open('label.txt','w')

        h, w, _ = bgimg.shape
        resizeHeight = random.choice(resize_heights)
        meth = random.choice(range(4))
        bgimg = cv2.resize(
            bgimg, (int(resizeHeight / h * w), resizeHeight), interpolation=meth)

        h, w, _ = bgimg.shape
        ylimit = []
        for i in range(random.choice(range(1, 6))):
            topleftx = random.choice(range(int(w * 0.8)))
            toplefty = random.choice(range(int(h * 0.8)))
            if Overlap(ylimit, toplefty):
                continue
            startx = topleftx
            starty = toplefty

            maxCharH = 0
            for j in range(random.choice(range(3, 12))):
                fntdir = random.choice(os.listdir('Fnts'))
                fntimgn = random.choice(os.listdir('Fnts/' + fntdir))
                fntimg = cv2.imread('Fnts/' + fntdir + '/' + fntimgn, 0)
                h_, w_ = fntimg.shape
                meth = random.choice(range(4))
                ratio = random.choice(ratios)
                fntimg = cv2.resize(
                    fntimg, (int(ratio * w_), int(ratio * h_)), interpolation=meth)
                xs, ys, xmin, ymin, xmax, ymax = FindCoord(fntimg)

                color = random.choice(colors)
                charw = xmax - xmin
                charh = ymax - ymin
                diff='0'
                if charw<10 or charh<10:
                    diff='1'
                if startx + charw >= w or starty + charh >= h or Overlap(
                        ylimit, starty + charh) or Cover(ylimit,
                                                        [starty, starty + charh]):
                    continue
                if maxCharH < charh:
                    maxCharH = charh
                for k in range(len(xs)):
                    x, y = xs[k], ys[k]
                    transx = startx + x - xmin
                    transy = starty + y - ymin
                    bgimg[transy, transx, :] = bgimg[starty,startx,:]+80
                txt.write(
                    chr(int(fntdir)) + ' ' + str(transx - 2) + ' ' +
                    str(transy - 2) + ' ' + str(charw + 2) + ' ' + str(charh + 2) +
                    ' ' + diff + '\n')
                startx += charw + random.choice(range(chardis, 20))
            ylimit.append([starty, starty + maxCharH])
        txt.close()
        cv2.imwrite('syn_img/' + bgimgn.split('.')[0] + '_'+str(iter)+'.jpg',bgimg)
        #cv2.imshow('synimg', bgimg)
        #cv2.waitKey(0)
