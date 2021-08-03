import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
 
sets = []
classes = ['without_mask', 'with_mask', 'mask_weared_incorrect']  ##修改为自己的类别
 
#原样保留。size为图片大小
# 将ROI的坐标转换为yolo需要的坐标
# size是图片的w和h
# box里保存的是ROI的坐标（x，y的最大值和最小值）
# 返回值为ROI中心点相对于图片大小的比例坐标，和ROI的w、h相对于图片大小的比例
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(image_add):
    #image_add进来的是带地址的.jpg
    image_add = os.path.split(image_add)[1]        #截取文件名带后缀
    image_add = image_add[0:image_add.find('.',1)] #删除后缀，现在只有文件名没有后缀
    #现在传进来的只有图片名没有后缀
   
    in_file = open("/Users/meg/desktop/Mask_Detection/dataset/mask_xml/annotations/" + image_add + '.xml')        #修改为你自己的输入目录
    #out_file = open('/Users/meg/desktop/archive/labels/%s.txt'%(image_add), 'w')  #修改为你自己的输出目录
    with open('/Users/meg/desktop/Mask_Detection/dataset/mask_xml/labels/%s.txt'%(image_add), 'w') as out_file:
        tree=ET.parse(in_file)
        root = tree.getroot()
        
        if root.find('size'):
            size = root.find('size')
            w = int(size.find('width').text)    #偶尔xml标记出错，width或height设置为0了
            h = int(size.find('height').text)   #需要标记出来，便于单独处理
            if w==0:
                print("出错！ width或height为0:  "+image_add)
                os.remove("/Users/meg/desktop/Mask_Detection/dataset/mask_xml/images/"+image_add+".jpg")
                os.remove("/Users/meg/desktop/Mask_Detection/dataset/mask_xml/annotations/" + image_add + '.xml')
                return
            #在一个XML中每个Object的迭代
            for obj in root.iter('object'):
                #iter()方法可以递归遍历元素/树的所有子元素
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                #如果训练标签中的品种不在程序预定品种，或者difficult = 1，跳过此object
                if cls not in classes or int(difficult)==1:
                    continue
                #cls_id 只等于1
                print('qq')
                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                #b是每个Object中，一个bndbox上下左右像素的元组
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                bb = convert((w,h), b)
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        else:
            print("出错！xml缺少size:  "+image_add)      #偶尔xml缺少size，需要标记出来，便于单独处理
            os.remove("/Users/meg/desktop/Mask_Detection/dataset/mask_xml/images/"+image_add+".jpg")
            os.remove("/Users/meg/desktop/Mask_Detection/dataset/mask_xml/annotations/"+image_add+".xml")
 
 
#image_adds = open("/archive/annotations/lst.txt")        #修改为你自己的训练数据集目录



image_adds = os.listdir("/Users/meg/desktop/Mask_Detection/dataset/mask_xml/images")
for image_add in image_adds:
    if image_add == '.DS_Store':
        continue
    #image_add = image_add.strip()
    #print (image_add)
    convert_annotation(image_add)


