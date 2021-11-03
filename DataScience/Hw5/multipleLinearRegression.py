#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
import time

def load_dbscore_data():
    conn = pymysql.connect(host='localhost', user='root', password='tkdals!0715', db='LinearRegression')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = "select * from score"
    curs.execute(sql)
    
    data  = curs.fetchall()
    
    curs.close()
    conn.close()
    
    #X = [ (t['attendance'], t['homework'], t['midterm'] ) for t in data ]
    X1 = [ ( t['attendance'] ) for t in data ]
    X1 = np.array(X1)
    X2 = [ ( t['homework'] ) for t in data ]
    X2 = np.array(X2)
    X3 = [ ( t['final'] ) for t in data ]
    X3 = np.array(X3)
    
    y = [ (t['score']) for t in data]
    y = np.array(y)

    return X1,X2,X3,y

X1,X2,X3,y = load_dbscore_data()

'''
plt.scatter(X, y) 
plt.show()
'''

#y = w1x1 + w2x2 + w2x2 + c

from statsmodels.formula.api import ols

df = pd.read_excel('db_score.xlsx')

model = ols('score ~ attendance + homework + final',data = df)
ls = model.fit()

print(ls.summary())


#########

def gradient_descent_naive(X1,X2,X3,y):

    epochs = 100000
    min_grad = 0.0001
    learning_rate = 0.001
    
    w1 = 0.0
    w2 = 0.0
    w3 = 0.0
    c = 0.0
    
    n = len(y)
    
    c_grad = 0.0
    w1_grad = 0.0
    w2_grad = 0.0
    w3_grad = 0.0
    
    for epoch in range(epochs):
        
        for i in range(n):
            y_pred = w1 * X1[i] + w2 * X2[i] + w3 * X3[i] + c
            w1_grad += 2*(y_pred-y[i]) * X1[i]
            w2_grad += 2*(y_pred-y[i]) * X2[i]
            w3_grad += 2*(y_pred-y[i]) * X3[i]
            c_grad += 2*(y_pred - y[i])

        c_grad /= n
        w1_grad /= n
        w2_grad /= n
        w3_grad /= n
        
        w1 = w1 - learning_rate * w1_grad
        w2 = w2 - learning_rate * w2_grad
        w3 = w3 - learning_rate * w3_grad
        c = c - learning_rate * c_grad
        
        if ( epoch % 1000 == 0):
            print("epoch %d: w1_grad=%f, w2_grad=%f, w3_grad=%f, c_grad=%f, w1=%f, w2=%f, w3=%f, c=%f" 
                  %(epoch, w1_grad, w2_grad, w3_grad, c_grad, w1, w2 , w3, c) )   
        
        if ( abs(w1_grad) < min_grad and abs(w2_grad) < min_grad and abs(w3_grad) < min_grad 
                and abs(c_grad) < min_grad ):
            break
        
    return w1,w2,w3,c

start_time = time.time()
w1,w2,w3, c = gradient_descent_naive(X1,X2,X3,y)
end_time = time.time()

print("%f seconds" %(end_time - start_time))

print("\n\nFinal:")
print("gdn_w1=%f,gdn_w2=%f,gdn_w3=%f, gdn_c=%f" %(w1,w2,w3, c) )

######### 

def gradient_descent_vectorized(X1,X2,X3, y):
    epochs = 100000
    min_grad = 0.0001
    learning_rate = 0.001
    
    w1 = 0.0
    w2 = 0.0
    w3 = 0.0
    c = 0.0
    
    n = len(y)
    
    c_grad = 0.0
    w1_grad = 0.0
    w2_grad = 0.0
    w3_grad = 0.0

    for epoch in range(epochs):    
    
        y_pred = w1 * X1 + w2 * X2 + w3 * X3 + c
        w1_grad = (2*(y_pred - y)*X1).sum()/n
        w2_grad = (2*(y_pred - y)*X2).sum()/n
        w3_grad = (2*(y_pred - y)*X3).sum()/n
        c_grad = (2 * (y_pred - y)).sum()/n
        
        w1 = w1 - learning_rate * w1_grad
        w2 = w2 - learning_rate * w2_grad
        w3 = w3 - learning_rate * w3_grad
        c = c - learning_rate * c_grad        

        if ( epoch % 1000 == 0):
            print("epoch %d: w1_grad=%f, w2_grad=%f, w3_grad=%f, c_grad=%f, w1=%f, w2=%f, w3=%f, c=%f" 
                  %(epoch, w1_grad, w2_grad, w3_grad, c_grad, w1, w2 , w3, c) )   
        
        if ( abs(w1_grad) < min_grad and abs(w2_grad) < min_grad and abs(w3_grad) < min_grad 
                and abs(c_grad) < min_grad ):
            break

    return w1,w2,w3,c

start_time = time.time()
w1,w2,w3,c = gradient_descent_vectorized(X1,X2,X3, y)
end_time = time.time()

print("%f seconds" %(end_time - start_time))

print("\n\nFinal:")
print("gdv_w1=%f,gdv_w2=%f,gdv_w3=%f, gdv_c=%f" %(w1,w2,w3, c) )




# In[ ]:





# In[ ]:




