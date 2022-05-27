# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import re
import random
import time


class Loader:
    dataPath = './lfw image data/'

    train_labels = {}

    validation_labels = {}

    test_labels = {}

    # 所需正则表达式  r"([A-Za-z_]*)_[0-9]*.jpg"gm

    def LoadData(self):
        # 从.txt导入标签
        # print("Start loading labels...")
        male_label = open('./male_names.txt', 'r')
        female_label = open('./female_names.txt', 'r')
        male_list = male_label.read().splitlines()
        female_list = female_label.read().splitlines()

        # 导入图片数组并标记，打乱放入字典；键为标签_编号，值为图像数组
        # print("Start loading pictures...")
        size = len(male_list) + len(female_list)
        ex = re.compile("([A-Za-z_-]*)_[0-9]*.jpg")
        i_male = 1
        i_female = 1
        for i in range(size):
            time.sleep(0.00001)
            flag = random.randint(0, 1)
            if flag == 0 and len(male_list) > 0:
                male_imgname = male_list.pop(random.randint(0, len(male_list)-1))
                tmplist = ex.findall(male_imgname)# 正则表达式获取图片所在文件夹名
                dir_name = tmplist[0]
                picPath = self.dataPath + dir_name + '/' + male_imgname  # 获取图片路径
                image = self.loadPicArray(picPath)
                key = "male_" + str(i_male)
                self.train_labels[key] = image
                i_male += 1
                # time.sleep(0.0001)
            elif flag == 1 and len(female_list) > 0:
                female_imgname = female_list.pop(random.randint(0, len(female_list) - 1))
                tmplist = ex.findall(female_imgname)# 正则表达式获取图片所在文件夹名
                dir_name = tmplist[0]
                picPath = self.dataPath + dir_name + '/' + female_imgname  # 获取图片路径
                image = self.loadPicArray(picPath)
                key = "female_" + str(i_female)
                self.train_labels[key] = image
                i_female += 1
                # time.sleep(0.0001)

        # 划分数据集
        # print("\nStart dividing dataset...")
        train_size = int(size * 0.40)
        validation_size = int(size * 0.10)
        test_size = size - train_size - validation_size
        for i in range(test_size):
            key_value = self.train_labels.popitem()
            tmp_dict = {}
            tmp_dict[key_value[0]] = key_value[1]
            self.test_labels.update(tmp_dict)
        for j in range(validation_size):
            key_value = self.train_labels.popitem()
            tmp_dict = {}
            tmp_dict[key_value[0]] = key_value[1]
            self.validation_labels.update(tmp_dict)

    # 读取图片数据并灰度化，得到图片对应的像素值的数组，均一化到0-1
    def loadPicArray(self, picFilePath):
        Img = Image.open(picFilePath)
        ImgGray = Img.convert('L')
        SmallImgGray = ImgGray.resize((100, 100))
        picArray = np.array(SmallImgGray).flatten() / 255.0
        return picArray

    def getTrainData(self):
        return self.train_labels

    def getValidationData(self):
        return self.validation_labels

    def getTestData(self):
        return self.test_labels
