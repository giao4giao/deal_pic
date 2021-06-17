
# PythonMargick包可以到Unofficial Windows Binaries for Python Extension Packages下载
'''
import PythonMagick

img = PythonMagick.Image('car.png')
# 这里要设置一下尺寸，不然会报ico尺寸异常错误
img.sample('128x128')
img.write('main.ico')
'''

import PIL.Image as Image
 
# img=Image.open("car.png")
# img.resize((128,128),Image.ANTIALIAS).save("main.ico")
img=Image.open("a_.png")
img.resize((128,128),Image.ANTIALIAS).save("_a.ico")