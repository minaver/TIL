#!/usr/bin/env python
# coding: utf-8

# In[75]:


import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import initializers

# y = 1 + 3*x1 + 5*(x2**2) + 10*(x3**3) + 20(x4**4) + 10

# Model 제작
def gen_sequential_model():
# kernel_initializer 의 weight 값이 지정을 안해주면 랜덤으로 들어가 운이 나쁘면 model이 제대로 학습이 안될 수 있다. seed를 42로 주어 항상 동일한 weight를 만들어 준다.
    model = Sequential([
            Input(4, name='input_layer'),
            Dense(16, activation='sigmoid', name='hidden_layer1', kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.05, seed=42)),
            Dense(16, activation='sigmoid', name='hidden_layer2', kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.05, seed=42)),
            Dense(1, activation='relu', name='output_layer', kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.05, seed=42))
            ])
            
    model.summary() # Param # : 전 layer의 input값 * (현 layer Node 수 + bias(1))
    
    # weight값을 각각 확인할 수 있다.
    # print(model.layers[0].get_weights())
    # print(model.layers[1].get_weights())
    
    # sgd = 확률적 경사 하강법 mse = meanSquaredError
    model.compile(optimizer='adam', loss='mse')

    return model

# y = 1 + 3*x1 + 5*(x2**2) + 10*(x3**3) + 20(x4**4) + 10

# Sample Data Set 생성
def gen_linear_regression_dateset(numofsamples=500, w1=3, w2=5, w3=10, w4=20, b=11):

    np.random.seed(42)
    X = np.random.rand(numofsamples, 4)
    
    Z = np.zeros((numofsamples,4))
    
    for i in range(numofsamples):
        Z[i,0] = X[i,0]
        Z[i,1] = (X[i,1])**3
        Z[i,2] = (X[i,2])**4
        Z[i,3] = (X[i,3])**5

    coef = np.array([w1, w2, w3, w4])
    bias = b

    y = np.matmul(Z, coef.transpose()) + bias

    # X=(numofsamples, 4), coef.transpose() = (4,1)
    
    return X, y

# 화면 상에서 loss 변화를 확인할 수 있는 함수 (loss 값이 잘 줄어드는지 확인/train과 test의 차이가 별로 없다면 오버피팅이 되지 않고 있음을 알 수 있다.)
def plot_loss_curve(history):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(15, 10))

    plt.plot(history.history['loss'][1:])
    plt.plot(history.history['val_loss'][1:])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.show()   

# Model에 예측하는 함수
def predict_new_sample(model, x, w1=3, w2=5, w3=10, w4=20, b=11):
    
 
    x = x.reshape(1,4)
    y_pred = model.predict(x)[0][0]
    
    y_actual = w1*x[0][0] + w2*(x[0][1]**2) + w3*(x[0][2]**3) + w4*(x[0][3]**4) + b
     
    print("y actual value = ", y_actual)
    print("y predicted value = ", y_pred)



model = gen_sequential_model()

# * 데이터 샘플 준비
# 데이터 샘플을 충분히 준비하지 않으면 좋은 결과를 얻을 수 없다.
X, y = gen_linear_regression_dateset(numofsamples=4000)

# # 모델 학습
# # epochs : 전체 데이터를 몇번 스캔하면서 학습할 것인가 // loss 그래프가 평평해지면 epochs를 더 늘려봤자 소용없다.
# # verbose : 실제 트레이닝 하는 각 과정의 loss값 표현 (2)
# # validation_split=0.3 : Training에 70% 를 쓰고 Validate에 나머지 30% 준다
history = model.fit(X, y, epochs=2000, verbose=2, validation_split=0.3)

# # loss 그래프 생성
plot_loss_curve(history)

# # loss 마지막 loss 각각 도출
print("train loss=", history.history['loss'][-1])
print("test loss=", history.history['val_loss'][-1])

# # 모델을 사용하여 예측
predict_new_sample(model, np.array([0.3, 0.9, 0.4 ,0.1]))



