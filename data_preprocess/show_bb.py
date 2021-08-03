from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

#####################################################################

# 建立資料夾中的檔案清單
def make_list(inputfile):
	allFileList = os.listdir(inputfile)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	return(allFileList)

# 輸出單一張圖片的 bounding_box
def show_single_bb(imagename, imagefile='./', labelfile='./', outputfile='./', bbsize=2):
	label_List = make_list(labelfile)
	labelname = labelfile+imagename[:imagename.find('.')]+'.txt'
	if imagename[:imagename.find('.')]+'.txt' in label_List:
		with open(labelname, 'r') as f:
			img = cv2.imread(imagefile+imagename)
			picture_width = float(img.shape[1])
			picture_high = float(img.shape[0])

			for line in f:
				(_class, x, y, w, h) = line.split(' ')
				_class = float(_class)
				x = float(x)
				y = float(y)
				w = float(w)
				h = float(h)
				boxx_center = x * picture_width
				boxy_center = y * picture_high
				xmin = int(boxx_center - 0.5 * w * picture_width)
				ymin = int(boxy_center - 0.5 * h * picture_high)
				xmax = int(boxx_center + 0.5 * w * picture_width)
				ymax = int(boxy_center + 0.5 * h * picture_high)

				if _class == 0:
					img = cv2.rectangle(img, (xmin,ymin), (xmax,ymax), (0,0,255), bbsize)
				elif _class == 1:
					img = cv2.rectangle(img, (xmin,ymin), (xmax,ymax), (0,255,0), bbsize)
				elif _class == 2:
					img = cv2.rectangle(img, (xmin,ymin), (xmax,ymax), (255,0,0), bbsize)
				else:
					img = cv2.rectangle(img, (xmin,ymin), (xmax,ymax), (125,125,125), bbsize)

			cv2.imwrite(outputfile+'bb_'+imagename[:imagename.find('.')]+'.jpg', img)
			print('bb完成')

# 輸出資料夾內所有圖片的 bounding_box
def show_mount_image_bb(imagefile, labelfile, outputfile, bbsize=2):
	os.mkdir(outputfile[:-1])
	for image in make_list(imagefile):
		show_single_bb(image, imagefile, labelfile, outputfile, bbsize)

#####################################################################

'''
show_single_bb(
	'268_105.jpg',
	'../dataset/plate/images/valid/',
	'../dataset/plate/labels/valid/')
'''
show_mount_image_bb(
	imagefile = '../dataset/mask_plate/images_bi/',
	labelfile = '../dataset/mask_plate/labels_bi/',
	outputfile = '../dataset/mask_plate/test/'
	)








