
import cv2
import os


def resize_image(input_file, output_file):
	allFileList = os.listdir(input_file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	for picture in allFileList[0:300]:
		image = cv2.imread(input_file+picture)
		print(f'轉換前 ： {image.shape}')
		image = cv2.resize(image, (500, 400), interpolation=cv2.INTER_AREA)
		print(f'轉換後 ： {image.shape}')
		cv2.imwrite(output_file+picture, image)


def standarize_image(input_file, output_file):
	allFileList = os.listdir(input_file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	for picture in allFileList:
		image = cv2.imread(input_file+picture)
		print(f'轉換前 image[0, 0, :] = ： {image[0, 0, :]}')
		image = image / 255
		print(f'轉換後 image[0, 0, :] = ： {image[0, 0, :]}')
		cv2.imwrite(output_file+picture, image)	

# 高通濾波
def high_pass_filter(input_file, output_file):
	allFileList = os.listdir(input_file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	for picture in allFileList:
		image=cv2.imread(input_file+picture)
		x=cv2.Sobel(image,cv2.CV_16S,1,0)
		y=cv2.Sobel(image,cv2.CV_16S,0,1)
		absx=cv2.convertScaleAbs(x)
		absy=cv2.convertScaleAbs(y)
		dist=cv2.addWeighted(absx,0.5,absy,0.5,0)
		cv2.imwrite(output_file+picture, dist)

# 雙邊濾波
def bi_demo(input_file, output_file):
	allFileList = os.listdir(input_file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	for picture in allFileList:
		image=cv2.imread(input_file+picture)
		dst = cv2.bilateralFilter(image, 0, 100, 5)
		cv2.imwrite(output_file+picture, dst)

# 均值遷移
def shift_demo(input_file, output_file):
	allFileList = os.listdir(input_file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	for picture in allFileList:
		image=cv2.imread(input_file+picture)
		dst = cv2.pyrMeanShiftFiltering(image, 10, 50)
		cv2.imwrite(output_file+picture, dst)


input_file = '../dataset/mask_plate/images_origin/'
output_file = '../dataset/mask_plate/images_shift/'
os.mkdir(output_file[:-1])
shift_demo(input_file, output_file)





