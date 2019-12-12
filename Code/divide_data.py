import os
import random
import math as m

def ConvertListToDic(lst): 
    res_dct = {lst[i]: 0 for i in range(0, len(lst), 1)} 
    return res_dct 

def ConvertDicToList(dic):
    dic_to_lst = []
    for key in dic:
        if dic[key] == 0:
            dic_to_lst.append(key)
    return dic_to_lst

def ProcessedList(lstA, lstB):
    dicA = ConvertListToDic(lstA)
    for item in lstB:
        if(dicA[item] == 0):
            dicA[item] = 1
    return ConvertDicToList(dicA)
    
def WriteData(file_name, lst_images, dir_target):
    file_data = open(dir_target, "w")
    for image_name in lst_images:
        image_dir = file_name + "/" + image_name
        file_data.write(image_dir + "\n")
    file_data.close()

def Processed(source_dir, data_dir):
    list_files = os.listdir(source_dir)
    for file_name in list_files:
        file_dir = source_dir + "/" + file_name
        list_images = os.listdir(file_dir)

        number_of_images = len(list_images)
        number_of_images_train = m.ceil(number_of_images / 2)
        number_of_images_val = m.ceil((number_of_images - number_of_images_train) / 2)
        number_of_images_test = number_of_images - number_of_images_train - number_of_images_val

        list_images_train = random.sample(list_images, number_of_images_train)
        list_images_val_and_test = ProcessedList(list_images, list_images_train)
        list_images_val = random.sample(list_images_val_and_test, number_of_images_val)
        list_images_test = ProcessedList(list_images_val_and_test, list_images_val)

        file_class_dir = data_dir + "/" + file_name
        if(os.path.exists(file_class_dir) == False):
            os.mkdir(file_class_dir)

        data_train_dir = file_class_dir + "/train.txt"
        data_val_dir = file_class_dir + "/val.txt"
        data_test_dir = file_class_dir + "/test.txt"

        WriteData(file_name, list_images_train, data_train_dir)
        WriteData(file_name, list_images_val, data_val_dir)
        WriteData(file_name, list_images_test, data_test_dir)

name_of_folder = "Tên thư mục chứa data"
source_dir = os.getcwd() + "/" + name_of_folder
data_dir = os.getcwd() + "/dataset/data1"

Processed(source_dir, data_dir)