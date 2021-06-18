
# PythonMargick包可以到Unofficial Windows Binaries for Python Extension Packages下载
'''
import PythonMagick

img = PythonMagick.Image('car.png')
# 这里要设置一下尺寸，不然会报ico尺寸异常错误
img.sample('128x128')
img.write('main.ico')
'''
import os

import PIL.Image as Image

# img=Image.open("car.png")
# img.resize((128,128),Image.ANTIALIAS).save("main.ico")

l=[]
for a, b, c in os.walk('.'):
	if b == []:
		l += [i for i in c if os.path.splitext(i)[-1] in ('.png', '.jpg')]



for i in l:
	img=Image.open(i)
	img=img.resize((168,168),Image.ANTIALIAS)
	print(img)
	img.save(os.path.splitext(i)[0]+'.ico')
	# os.remove(i)