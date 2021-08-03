import time
#import img2txt
import os
import json
from PIL import Image

def load_file(fpath):  # fpath是具体的文件 ，作用：#str to list
    assert os.path.exists(fpath)  # assert() raise-if-not
    with open(fpath, 'r') as fid:
        lines = fid.readlines()
    records = [json.loads(line.strip('\n')) for line in lines]  # str to list
    return records


def img2txt(odgtpath, respath):
    records = load_file(odgtpath)  # 提取odgt文件数据
    record_list = len(records)  # 获得record的长度，循环遍历所有数据。
    print(os.getcwd())
    # os.mkdir(os.getcwd() + respath)
    with open(respath, 'w') as txt:
        for i in range(record_list):
            file_name = records[i]['ID'] + '.jpg'
            file_name = str("/Image/" + file_name)
            txt.write(file_name + '\n')


def tonormlabel(odgtpath, storepath):
    records = load_file(odgtpath)           #records = img2txt.load_file(odgtpath)
    record_list = len(records)
    print(record_list)
    categories = {}
    # txt = open(respath, 'w')
    for i in range(record_list):
        txt_name = storepath + records[i]['ID'] + '.txt'
        file_name = records[i]['ID'] + '.jpg'
        #print(i)
        im = Image.open("./Image/" + file_name)
        height = im.size[1]
        width = im.size[0]
        file = open(txt_name, 'w')
        gt_box = records[i]['gtboxes']
        gt_box_len = len(gt_box)  # 每一个字典gtboxes里，也有好几个记录，分别提取记录。
        for j in range(gt_box_len):
            category = gt_box[j]['tag']
            if category not in categories:  # 该类型不在categories，就添加上去
                new_id = len(categories) + 1  # ID递增
                categories[category] = new_id
            category_id = categories[category]  # 重新获取它的类别ID
            fbox = gt_box[j]['fbox']  # 获得全身框
#            norm_x = fbox[0] / width 
#            norm_y = fbox[1] / height
            norm_w = fbox[2] / width
            norm_h = fbox[3] / height
            norm_x = fbox[0] / width + 0.5 * norm_w
            norm_y = fbox[1] / height + 0.5 * norm_h

            '''
            norm_x = 0 if norm_x <= 0 else norm_x
            norm_x = 1 if norm_x >= 1 else norm_x
            norm_y = 0 if norm_y <= 0 else norm_y
            norm_y = 1 if norm_y >= 1 else norm_y
            norm_w = 0 if norm_w <= 0 else norm_w
            norm_w = 1 if norm_w >= 1 else norm_w
            norm_h = 0 if norm_h <= 0 else norm_h
            norm_h = 1 if norm_h >= 1 else norm_h
            '''
            blank = ' '
            if j == gt_box_len-1:
                file.write(str(category_id - 1) + blank + '{:.6f}'.format(norm_x) + blank + '{:.6f}'.format(norm_y) + blank
                           + '{:.6f}'.format(norm_w) + blank + '{:.6f}'.format(norm_h))
            else:
                file.write(str(category_id - 1) + blank + '{:.6f}'.format(norm_x) + blank + '{:.6f}'.format(norm_y) + blank
                           + '{:.6f}'.format(norm_w) + blank + '{:.6f}'.format(norm_h) + '\n')




if __name__ == '__main__':
    odgtpath = "./annotation_val.odgt"           #"/datasets/crowdhuman/annotation_train.odgt" 
    respath = "./annotation_name.txt"  #"/datasets/crowdhuman/train_name.txt"
    storepath = "./annotation/"                    #"/datasets/crowdhuman/labels/train_all/Image/"
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 格式化输出时间
    start = time.time()
    tonormlabel(odgtpath, storepath)
    end = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('已完成轉換，共耗時{:.5f}s'.format(end - start))