import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential      # keras.model 클래스로부터 Sequential 과 functionnal API 모델 제작 방식 제공
from tensorflow.keras.layers import Dense           # keras.layers 클래스로부터 Dense API 를 제공
from tensorflow.keras.optimizers import Adam        # keras.optimizers 클래스로부터 Adam 옵티마이저를 제공

# MNIST 를 읽어와서 신경망에 입력할 형태로 변환
(x_train, y_train), (x_test, y_test) = mnist.load_data()    # 읽어온 데이터는 28X28 크기의 2차원 텐서
x_train = x_train.reshape(60000,784)                        # reshape 함수를 이용해 1차원 텐서 모양 변환
x_test = x_test.reshape(10000,784)                          # reshape 함수를 이용해 1차원 텐서 모양 변환
x_train = x_train.astype(np.float32)/255.0                  # 정수를 실수형으로 바꾸고 [0,255] 범위를 [0,1] 범위로 정규화 (ndarray 로 변환)
x_test = x_test.astype(np.float32)/255.0                    # 정수를 실수형으로 바꾸고 [0,255] 범위를 [0,1] 범위로 정규화 (ndarray 로 변환)
y_train = tf.keras.utils.to_categorical(y_train,10)         # 레이블을 원핫 코드로 변환
y_test = tf.keras.utils.to_categorical(y_test,10)           # 레이블을 원핫 코드로 변환

# 신경망 구조 설계
n_input=784         # 입력층 노드 개수 설정
n_hidden=1024       # 은닉층 노드 개수 설정
n_output=10         # 출력층 노드 개수 설정

# 모델을 생성하고 두 층을 쌓는다.
mlp=Sequential()
# 은닉층을 추가, input_shpe 매개 변수는 units 이 이전 층에 해당한다는 사실을 프로그램이 알고 있으므로 생략
mlp.add(Dense(units=n_hidden,activation='tanh',input_shape=(n_input,),kernel_initializer='random_uniform', bias_initializer='zeros'))
# 출력층을 추가.
mlp.add(Dense(units=n_output,activation='tanh',kernel_initializer='random_uniform',bias_initializer='zeros'))

# 신경망 학습
mlp.compile(loss='mean_squared_error',optimizer=Adam(learning_rate=0.001),metrics=['accuracy'])
hist=mlp.fit(x_train,y_train,batch_size=128,epochs=30,validation_data=(x_test,y_test),verbose=2)

# 학습된 신경망으로 예측
res=mlp.evaluate(x_test,y_test,verbose=0)
print("정확률은", res[1]*100)

# 학습 곡선 시각화
import matplotlib.pyplot as plt

# 정확률 곡선
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='upper left')
plt.grid()
plt.show()

# 손실 함수 곡선
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='upper right')
plt.grid()
plt.show()