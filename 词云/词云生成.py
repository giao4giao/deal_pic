import jieba,wordcloud
import numpy as np
from PIL import Image


def all_np(arr):
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result

def merge_dict(x,y):
    for k,v in x.items():
                if k in y.keys():
                    y[k] += v
                else:
                    y[k] = v
    return y


py_mask = np.array(Image.open('car_.png'))
#print(py_mask)
#exit()
with open('2.txt',encoding='utf_8')as f:
		data=[i.replace('\n','').replace(' ','') for i in f if i.replace('\n','').replace(' ','')!='']

l=[]
for txt in data:
	ls=[]
	for ch in '!"！？”“#$%&()*+,-./:;<=>?@[\]^_‘{|}~，。、 ：《》' :
		if ch in txt:
			ls.append(ch)
	for i in ls:
		txt=txt.replace(i, " ")
	l.append(txt)
#print(l[0:18])
data=[i.replace(' ','') for i in l if i.replace(' ','')!='']

print(len(data))
ls=[]
if len(data)>5000:
	n,l=1,[]
	for i in data:
		if n==5000:
			ls.append(l)
			n,l=1,[]
		else:
			l.append(i)
		n+=1
else:
	ls=(data,)
world,n,list='',1,[]
for data in ls:
	print(n)
	data=' '.join(data)
	txt=jieba.lcut(data)
	print('finish')
	list+=txt
	#world+=('  '.join(txt)+' ')
	n+=1
world=world.replace('新一章','')
#world=world.replace('的','').replace('和','').replace('而','')

dict=all_np(txt)
del txt[:]
print('and')
'''
#建立颜色数组，可更改颜色
color_list=['#FF7F00','#FF7F00','#ff00ff','#00ffff','#ffff00']
#调用
from #matplotlib import colors
colormap=colors.ListedColormap(color_list)
'''
#with open('a.txt','w')as f:
#	f.write(str(dict))
w=wordcloud.WordCloud(background_color='white',
#mode="RGB",
mask=py_mask,
#colormap=colormap,
font_path='1.ttf',width=2000,
height=1000,max_words=1000000,
max_font_size=30,
min_font_size=1,
relative_scaling=1,
scale=100,#repeat=True,
)
#print(world)


#w.generate(world)
#w.fit_words(world)
w.generate_from_frequencies(dict)
w.to_file('a.png')


