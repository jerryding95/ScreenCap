#-- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab
from PIL import Image, ImageDraw
import time
import numpy as np
# prepare to change to emWave window and full screen
start = time.time()
waittime=1
print('Change to emWave window and full screen in '+str(waittime)+' sec.')
for i in range(waittime):
	while time.time()<start+i+1:
		pass
	if i<waittime-1:
		print('You have '+str(waittime-1-i)+' sec left.')
	else:
		print('Screencapting!')
####################################################

for i in range(1):
	# im = ImageGrab.grab(bbox=(0, 40, 1125, 500))
	im = ImageGrab.grab(bbox=(17, 0, 38, 22))	# The apple sign!
	# im = ImageGrab.grab(bbox=(0,0,2,2))
	rawdata = list(im.getdata())
	pdata = [rawdata[42*i:42*i+42] for i in range(len(rawdata)//42)]
	print(pdata)
	print(len(rawdata))
	newim=Image.new(mode='RGB',size=(42,44))
	newim.putdata(rawdata)
	newim.show()
	# p=im.getpixel((100,100))
	# print(p)
# 	# grab fullscreen, taking average 1.8s
	
	
# 	#im.show()
# 	# save image file
# 	# im.save('screenshot'+str(i)+'.png')
# 	# print(list(im.getdata()))
# 	# print(len(list(im.getdata())))
# 	# print(im.histogram())
# 	# show image in a window
# 	#im.show()