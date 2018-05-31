import os



for i in range(1870 * 1 + 1, 1870 * 2 + 1):
    index = str(i).zfill(6)
    os.rename('camera4/period14_camera4/%d.png' % i, 'camera4/period14_camera4/%s.png' % index)   #重命名
print('ok')
#        print file.split('.')[-1]