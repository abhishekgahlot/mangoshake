import os
from PIL import Image

basewidth = 300

for i in os.listdir('./positions'):
	for j in os.listdir('./positions/' + i):
		try:
			img = Image.open('./positions/' + i +'/' + j)
			wpercent = (basewidth/float(img.size[0]))
			hsize = int((float(img.size[1])*float(wpercent)))
			img = img.resize((basewidth,hsize), Image.ANTIALIAS)
			img.save('./scaled/' + i +'/' + j) 
		except: pass