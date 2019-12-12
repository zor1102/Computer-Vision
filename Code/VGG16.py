"""Đây là code sử dụng mô hình VGG16 để lấy đặc trưng của ảnh và lưu ra file
    Bộ data sử dụng là Caltech101, mọi người có thể sử dụng bộ data khác, cách tổ chức thư mục tương tự như nhau
"""
import os
import numpy as np
from PIL import Image
from keras.models import Model
from keras.layers import Input
from keras.applications.vgg16 import VGG16

vgg16_model = VGG16(include_top = True, weights = 'imagenet', input_shape = (224,224,3))
last = vgg16_model.layers[-2].output
features = Model(vgg16_model.input, last)

source_dir = os.getcwd()
data_dir = source_dir + "/101_ObjectCategories"
feature_dir = source_dir + "/feature"
list_data = os.listdir(data_dir)

for file_name in list_data:
    if file_name == "BACKGROUND_Google":
        # Bỏ lớp BACKGROUND_Google
        continue

    dir_of_this_file = data_dir + "/" + file_name
    list_images = os.listdir(data_dir + "/" + file_name)
    feature_dir_of_this_file = feature_dir + "/" + file_name
    os.mkdir(feature_dir_of_this_file)
    
    for image_name in list_images:
        dir_of_this_image = dir_of_this_file + "/" + image_name
        image = Image.open(str(dir_of_this_image)).resize((224, 224))
        x_train = np.array(image) * (1. / 255)
        if(x_train.shape == (224, 224)):
            #Nếu ảnh là ảnh xám thì bỏ qua
            continue
        x_train = np.expand_dims(x_train, axis = 0)
        feature_vec = features.predict(x_train)
        np.save(feature_dir_of_this_file + "/" + image_name, feature_vec)
