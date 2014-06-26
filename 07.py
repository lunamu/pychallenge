import os,sys
from PIL import Image

def average3(a,b,c):
	return (a+b+c)/3

pngfile = Image.open("07.png")
pix = pngfile.load()
lst = []
for i in range(0,609):
	lst.append(pix[i,5])
flst = []
origin = 0
for i in range(0, len(lst)):
	c = average3(lst[i][0], lst[i][1], lst[i][2]) 
	if(c != origin):
		flst.append(c)
		origin = c

f = open('07.out','w')
for i in range(0, len(flst)):
	f.write(str(flst[i])+'\n')
