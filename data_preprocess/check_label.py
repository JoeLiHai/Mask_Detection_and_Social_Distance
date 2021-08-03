import os

# 建立allFileList，印出資料夾內有多少個檔案
def make_list(file):
	allFileList = os.listdir(file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	print('-'*40)
	print(f'檔案中共有{len(allFileList)}筆資料')
	print('-'*40)
	return(allFileList)

# 印出全部txt檔案的內容
def print_all():
	for document in allFileList:
		print(f'檔案名稱 ： {document}')
		with open(file + '/' + document) as d:
			for line in d:
				print(line, end='')
			print('-'*40)

# 輸入要查詢的label，印出資料夾中有多少個這種label
def count_label(label, allFileList):
	count = 0
	for document in allFileList:
		with open(file + '/' + document, 'r') as d:
			for line in d:
				if line[0] == str(label):
					count += 1
	print(f'標記為 {str(label)} 的 label 共有{count}個')
	count = 0


# 列出包含某個label的檔案
def check_label(label, minn):
	lst = []
	for document in allFileList:
		with open(file + '/' + document) as d:
			count = 0
			for line in d:
				if line[0] == str(label):
					count += 1
				elif line[0] != str(label):
					count -= 1
			if count >= minn:
				print(f'檔案名稱：{document}中，類別{label}的數量比其他多{count}個')
				lst.append(document)
	print(f'共有{len(lst)}個檔案內包含{label}')
# 輸入要檢查的valid資料夾路徑及名稱
file = '../dataset/mask_plate/labels/valid'

allFileList = make_list(file)
count_label(0, allFileList)
count_label(1, allFileList)
count_label(2, allFileList)
count_label(3, allFileList)
check_label(0, 0)


