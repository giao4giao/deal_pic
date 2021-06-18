import os

n=1
for i in os.listdir():
	if os.path.splitext(i)[-1] in ('.jpg','.png'):
		print(n)
		os.rename(i,str(n)+os.path.splitext(i)[-1])
		n+=1
