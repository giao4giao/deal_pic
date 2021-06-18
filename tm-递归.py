from  PIL import Image
import os

def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((2,2))
    for h in range(H):
        for l in range(L):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 ==color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot,(0,0,0,0))
    return img 
 
   
'''
img=Image.open('1.png')
img=transparent_back(img)
img.save('round2.png')
'''

def transparent_back2(img):
    img=img.convert('RGBA')
    sp=img.size
    width=sp[0]
    height=sp[1]
    print(sp)
    for yh in range(height):
        for xw in range(width):
            dot=(xw,yh)
            color_d=img.getpixel(dot)
            if(color_d[3]==0):
                color_d=(255,255,255,255)
                img.putpixel(dot,color_d)
    img.show()
    return img


l=[]
for a,b,c in os.walk('.'):
	#print(a,b,c)
	if b==[]:		
		l+=[os.path.join(a,i) for i in c if os.path.splitext(i)[-1] in ('.png','.jpg')]
#print(l)
num=len(l)
print(num)
n=0
for i in l:
	n+=1
	print('正在进行',i,n,'共',num)
	img=Image.open(i)
	img=transparent_back(img)
	img.save(i)
	









