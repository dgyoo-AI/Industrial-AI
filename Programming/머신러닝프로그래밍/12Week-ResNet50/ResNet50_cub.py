import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import os
import matplotlib.pyplot as plt

train_folder = "./CUB200/train"
test_folder = "./CUB200/test"

class_reduce = 0.1
no_class = int(len(os.listdir(train_folder))*class_reduce)
set_type = 4
data_set = [no_class, no_class/5, no_class/10, no_class/no_class]
multi_no = [1, 5, 10, 20]


def get_dataset(settype, dataset, class_no):    # 데이터 집합 필터링 함수
    if (class_no == dataset) and (settype == 0):
        breedset = 0
    else:
        if settype == 1:
            if (class_no >= (dataset * multi_no[settype])) and (class_no < (dataset * multi_no[settype]) + multi_no[settype]):
                breedset = 1
            else:
                breedset = -1
        elif settype == 2:
            if (class_no >= (dataset * multi_no[settype])) and (class_no < (dataset * multi_no[settype]) + multi_no[settype]):
                breedset = 2
            else:
                breedset = -1
        elif settype == 3:
            if (class_no > (dataset * multi_no[settype])) and (class_no < (dataset * multi_no[settype]) + multi_no[settype]):
                breedset = 3
            else:
                breedset = -1
        else:
            breedset = -1

    return breedset


def train_model(settype, dataset):
    x_train, y_train = [], []
    for i, class_name in enumerate(os.listdir(train_folder)):

        breedset = get_dataset(settype, dataset, i)

        if settype == breedset:
            for file_name in os.listdir(train_folder + '/' + class_name):
                img = image.load_img(train_folder + '/' + class_name + '/' + file_name, target_size=(224, 224))
                if len(img.getbands()) != 3:  # R,G,B 형식으로 구성된 Image 인지 확인
                    print("주의: 유효하지 않은 영상 발생", class_name, file_name)
                    continue
                x = image.img_to_array(img)  # 3D Numpy 배열로 변환.
                x = preprocess_input(x)  # ResNet50 에서 제공되는 전처리 함수
                x_train.append(x)
                y_train.append(i)
            print("Train Class Name : ", class_name)
    print("y_train count : ", len(y_train))

    x_test, y_test = [], []
    for i, class_name in enumerate(os.listdir(test_folder)):

        breedset = get_dataset(settype, dataset, i)

        if settype == breedset:
            for file_name in os.listdir(test_folder + '/' + class_name):
                img = image.load_img(test_folder + '/' + class_name + '/' + file_name, target_size=(224, 224))
                if len(img.getbands()) != 3:
                    print("주의: 유효하지 않은 영상 발생", class_name, file_name)
                    continue
                x = image.img_to_array(img)
                x = preprocess_input(x)
                x_test.append(x)
                y_test.append(i)
            print("Test Class Name :", class_name)
    print("y_test count :", len(y_train))

    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    x_test = np.asarray(x_test)
    y_test = np.asarray(y_test)
    y_train = tf.keras.utils.to_categorical(y_train, no_class)
    y_test = tf.keras.utils.to_categorical(y_test, no_class)

    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))  # 새로운 모델 생성
    cnn = Sequential()
    cnn.add(base_model)  # ResNet50 모델을 추가.
    cnn.add(Flatten())  # 마지막 층을 일렬로 펼침
    cnn.add(Dense(1024, activation='relu'))  # 1024 개의 노드를 가진 은닉층 추가
    cnn.add(Dense(no_class, activation='softmax'))  # 출력층 추가

    cnn.compile(loss='categorical_crossentropy', optimizer=Adam(0.00001), metrics=['accuracy'])
    hist = cnn.fit(x_train, y_train, batch_size=16, epochs=10, validation_data=(x_test, y_test), verbose=1)

    res = cnn.evaluate(x_test, y_test, verbose=0)
    print("정확률은", res[1] * 100)

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.plot(hist.history['accuracy'])
    plt.plot(hist.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='best')
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='best')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    for m in range(set_type):
        for k in range(int(data_set[m])):
            if m<1:
                train_model(m, k)



