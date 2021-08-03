import os

# 建立allFileList，印出資料夾內有多少個檔案
def make_list(input_file):
	allFileList = os.listdir(input_file)
	if '.DS_Store' in allFileList:
		allFileList.remove('.DS_Store')
	print('-'*40)
	print(f'檔案中共有{len(allFileList)}筆資料')
	print('-'*40)
	return(allFileList)

# 修改類別的index，要手動調整方程式內的類別
def transfer(input_file, output_file, allFileList):
	new = ''
	for document in allFileList:
		with open(input_file+'/'+document, 'r') as f:
			for line in f:
				if line[0] == '0':
					new_line = '2' + line[1:]
				'''
				elif line[0] == '1':
					new_line = '1' + line[1:]
				elif line[0] == '2':
					new_line = '1' + line[1:]
				'''
				new = new+new_line
				print('new=', new)
		with open(output_file+'/'+document, 'w') as f:
			f.write(new)
		new = ''
		#print('*********************************')
	print('finished')

def combine_labels(input_file, combine_file, output_file):

	allFileList_1 = os.listdir(input_file)
	if '.DS_Store' in allFileList_1:
		allFileList_1.remove('.DS_Store')
	set1 = set(allFileList_1)

	allFileList_2 = os.listdir(combine_file)
	if '.DS_Store' in allFileList_2:
		allFileList_2.remove('.DS_Store')
	set2 = set(allFileList_2)

	set3 = set1 & set2
	allFileList_3 = list(set3)

	new = ''
	for document in allFileList_3:
		with open(input_file+'/'+document, 'r') as f:
			for line in f:
				new = new+line

		with open(combine_file+'/'+document, 'r') as f:
			for line in f:
				new=new+line

		with open(output_file+'/'+document, 'w') as f:
			f.write(new)
		
		new=''
	print(f'總共有{len(allFileList_3)}筆資料')
	print('finished')


input_file = '../out_train'
combine_file = '../dataset/mask_plate/labels_01/train'
output_file = '../dataset/mask_plate/labels_012/train'

allFileList = make_list(input_file)
#transfer(input_file, output_file, allFileList)
combine_labels(input_file, combine_file, output_file)








