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
    
def WriteData(file_name, lst_images, file_data):
    for image_name in lst_images:
        image_dir = file_name + "/" + image_name
        file_data.write(image_dir + "\n")

def Processed(source_dir, data_dir):
    list_files = os.listdir(source_dir)
    data_train_dir = data_dir + "/train.txt"
    data_val_dir = data_dir + "/val.txt"
    data_test_dir = data_dir + "/test.txt"

    file_train = open(data_train_dir, "w")
    file_val = open(data_val_dir, "w")
    file_test = open(data_test_dir, "w")
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

        WriteData(file_name, list_images_train, file_train)
        WriteData(file_name, list_images_val, file_val)
        WriteData(file_name, list_images_test, file_test)

    file_train.close()
    file_val.close()
    file_test.close()

path = os.getcwd()
source_dir = path + "/Name Of Folder Data"

dataset_dir = path + "/dataset"
if(os.path.exists(dataset_dir) == False):
    os.mkdir(dataset_dir)

folder_data_in_dataset = dataset_dir + "/data1"
if(os.path.exists(folder_data_in_dataset) == False):
    os.mkdir(folder_data_in_dataset)

Processed(source_dir, folder_data_in_dataset)

source_dir = os.getcwd() + "/101_ObjectCategories"
data_dir = os.getcwd() + "/dataset/data1"

Processed(source_dir, data_dir)