import os
import cv2
import numpy as np


cropSize = 448
cropImg = []
cnt = 0
saveDir = ''
ch2eng = {'不导电':'defect1', '擦花':'defect2', '横条压凹':'defect3', '桔皮':'defect4', '漏底':'defect5', '碰伤':'defect6', '起坑':'defect7', '凸粉':'defect8', '涂层开裂':'defect9', '脏点':'defect10', '其他':'defect10'}
if os.path.exists('savedFileList_bak.txt'):
    os.remove('savedFileList_bak.txt')
if os.path.exists('savedFileList.txt'):
    os.rename('savedFileList.txt', 'savedFileList_bak.txt')
savedFileList = open('savedFileList.txt', 'w')
oneClick = 0
keyin = 0

def SaveImg():
    global oneClick
    global keyin
    if (oneClick == 0):
        if keyin&0xFF==89:
            cv2.imwrite(saveDir+'/'+'y_'+str(cnt)+'.jpg', cropImg)
            print('saved: '+ saveDir+'/'+'y_'+str(cnt)+'.jpg'+'\n')
            savedFileList.write('saved: '+ saveDir+'/'+'y_'+str(cnt)+'.jpg'+'\n')
            savedFileList.flush()
            oneClick = 1
        elif keyin&0xFF==78:
            cv2.imwrite(saveDir+'/'+'n_'+str(cnt)+'.jpg', cropImg)
            print('saved: '+ saveDir+'/'+'n_'+str(cnt)+'.jpg'+'\n')
            savedFileList.write('saved: '+ saveDir+'/'+'n_'+str(cnt)+'.jpg'+'\n')
            savedFileList.flush()
            oneClick = 1
        elif keyin&0xFF==66:
            cv2.imwrite(saveDir+'/'+'b_'+str(cnt)+'.jpg', cropImg)
            print('saved: '+ saveDir+'/'+'b_'+str(cnt)+'.jpg'+'\n')
            savedFileList.write('saved: '+ saveDir+'/'+'m_'+str(cnt)+'.jpg'+'\n')
            savedFileList.flush()
            oneClick = 1
        elif keyin&0xFF==68:
            cv2.imwrite(saveDir+'/'+'d_'+str(cnt)+'.jpg', cropImg)
            print('saved: '+ saveDir+'/'+'d_'+str(cnt)+'.jpg'+'\n')
            savedFileList.write('saved: '+ saveDir+'/'+'m_'+str(cnt)+'.jpg'+'\n')
            savedFileList.flush()
            oneClick = 1

cv2.namedWindow('cropImg', cv2.WINDOW_NORMAL)
cv2.namedWindow('row image', cv2.WINDOW_NORMAL)
#cv2.setMouseCallback('cropImg',SaveImg)

filelist = open('fileList.txt')
lines = filelist.readlines()
for idx in range(0, 1119):
    print("读到list行数： ", idx)
    savedFileList.write("读到list行数： "+str(idx)+' ')
    savedFileList.flush()
    print("总的图片计数： ", cnt+1)
    savedFileList.write("总的图片计数： "+str(cnt+1)+'\n')
    savedFileList.flush()
    imgPath = lines[idx].strip('\n')
    print(imgPath)
    pathSplit = imgPath.split('/')
    path_ = 'defect/'+ch2eng[pathSplit[1]]
    if not os.path.exists(path_):
        os.mkdir(path_)
    saveDir = path_
    img = cv2.imdecode(np.fromfile(imgPath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    rowImg = img.copy()
    num = 0
    for h in range(1920//cropSize):
        for w in range(2560//cropSize):
            cv2.rectangle(rowImg, (w*cropSize,h*cropSize), ((w+1)*cropSize,(h+1)*cropSize), (0,0,255), 10)
            cv2.imshow('row image', rowImg)
            cropImg = img[h*cropSize:(h+1)*cropSize,w*cropSize:(w+1)*cropSize,:]
            cropImg = cv2.resize(cropImg, (224,224))
            print('单张图片cropimg计数： ', num+1)
            savedFileList.write('单张图片cropimg计数： '+str(num+1)+' ')
            savedFileList.flush()
            while(1):
                cv2.imshow('cropImg',cropImg)
                keyin = cv2.waitKey(100)
                SaveImg()
                if oneClick == 1:
                    oneClick = 0
                    break
            cnt += 1
            num += 1
    for w in range(2560//cropSize):
        cv2.rectangle(rowImg, (w*cropSize,1920-1-cropSize), ((w+1)*cropSize,1920-1), (0,0,255), 10)
        cv2.imshow('row image', rowImg)
        cropImg = img[1920-1-cropSize:1920-1,w*cropSize:(w+1)*cropSize,:]
        cropImg = cv2.resize(cropImg, (224,224))
        print('单张图片cropimg计数： ', num+1)
        savedFileList.write('单张图片cropimg计数： '+str(num+1)+' ')
        savedFileList.flush()
        while(1):
            cv2.imshow('cropImg',cropImg)
            keyin = cv2.waitKey(100)
            SaveImg()
            if oneClick == 1:
                oneClick = 0
                break
        cnt += 1
        num += 1
    for h in range(1920//cropSize):
        cv2.rectangle(rowImg, (2560-1-cropSize,h*cropSize), (2560-1,(h+1)*cropSize), (0,0,255), 10)
        cv2.imshow('row image', rowImg)
        cropImg = img[h*cropSize:(h+1)*cropSize,2560-1-cropSize:2560-1,:]
        cropImg = cv2.resize(cropImg, (224,224))
        print('单张图片cropimg计数： ', num+1)
        savedFileList.write('单张图片cropimg计数： '+str(num+1)+' ')
        savedFileList.flush()
        while(1):
            cv2.imshow('cropImg',cropImg)
            keyin = cv2.waitKey(100)
            SaveImg()
            if oneClick == 1:
                oneClick = 0
                break
        cnt += 1
        num += 1
'''
    cv2.rectangle(rowImg, (2560-1-cropSize,1920-1-cropSize), (2560-1,1920-1), (0,0,255), 10)
    cv2.imshow('row image', rowImg)
    cropImg = img[1920-1-cropSize:1920-1,2560-1-cropSize:2560-1,:]
    cropImg = cv2.resize(cropImg, (224,224))
    print('单张图片cropimg计数： ', num+1)
    savedFileList.write('单张图片cropimg计数： '+str(num+1)+' ')
    savedFileList.flush()
    while(1):
        cv2.imshow('cropImg',cropImg)
        if cv2.waitKey(20)&0xFF==27:
            break
    cnt += 1
    num += 1
'''
        
cv2.destroyAllWindows()
savedFiileList.close()