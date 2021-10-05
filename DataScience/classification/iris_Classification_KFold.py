#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pymysql
import numpy as np

def classification_performance_eval(y,y_predict):
    tp, tn, fp, fn = 0,0,0,0
    
    for y,yp in zip(y,y_predict):
        if y == 1 and yp == 1:
            tp += 1
        elif y == 1 and yp == -1:
            fn += 1
        elif y == -1 and yp == -1:
            tn += 1
        else :
            fp += 1
    
    accuracy = (tp+tn) / (tp+tn+fp+fn)
    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    f1_score = (2*precision*recall) / (precision+recall)
    
    return accuracy , precision, recall, f1_score

conn = pymysql.connect(host='localhost',user='root',password='tkdals!0715',database='classification')
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from iris"
curs.execute(sql)

data = curs.fetchall()

curs.close()
conn.close()

# feature Array
X = [ (t['sepal_length'] ,t['sepal_width'],t['petal_length'],t['petal_width']) for t in data ]
X = np.array(X)

# label Array (feature에 대응하는)
y = [ 1 if t['variety'] == 'Versicolor' else -1 for t in data ]
y = np.array(y)

from sklearn.model_selection import KFold
from sklearn import tree

acc = []
pre = []
rec = []
f1 = []

kf = KFold(n_splits=5,random_state=42,shuffle=True)

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # decision tree 사용 - 컴퓨터가 학습을 통해 case에 대한 조건문들을 스스로 구성
    dtree = tree.DecisionTreeClassifier()
    dtree_model = dtree.fit(X_train,y_train) # training function <- 해당 함수 return으로 dtree_model이 만들어진다.
    
    y_predict = dtree_model.predict(X_test) # fit으로 만들어진 모델을 test by X_test

    accuracy,prediction,recall,f1_score =classification_performance_eval(y_test,y_predict)
    
    acc.append(accuracy)
    pre.append(prediction)
    rec.append(recall)
    f1.append(f1_score)

import statistics

print("acc",statistics.mean(acc))
print("pre",statistics.mean(pre))
print("rec",statistics.mean(rec))
print("f1",statistics.mean(f1))


# In[ ]:




