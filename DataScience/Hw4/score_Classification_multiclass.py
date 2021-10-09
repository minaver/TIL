#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pymysql
import numpy as np

# 5-1 성능 평가 함수
def classification_performance_eval(y,y_predict,target):
    tp, tn, fp, fn = 0,0,0,0
    if target == 'A':
        target_num = 2
    elif target == 'B':
        target_num = 1
    else:
        target_num = 0
    
    for y,yp in zip(y,y_predict):
        if y == target_num and yp == target_num:
            tp += 1
        elif y == target_num and yp != target_num:
            fn += 1
        elif y != target_num and yp != target_num:
            tn += 1
        else :
            fp += 1
    
    accuracy = (tp+tn) / (tp+tn+fp+fn)
    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    f1_score = (2*precision*recall) / (precision+recall)
    
    return accuracy , precision, recall, f1_score
# /5-1

conn = pymysql.connect(host='localhost',user='root',password='tkdals!0715',database='classification')
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from score"
curs.execute(sql)

data = curs.fetchall()

curs.close()
conn.close()

# 1. X(사용할 특징 데이터)와 y(결과 데이터) 초기화
X = [(t['homework'],t['discussion'],t['final']) for t in data]
X = np.array(X)

y = list()
for t in data:
    if t['grade'] == 'A':
         y.append(2)
    elif t['grade'] == 'B':
         y.append(1)
    else:
         y.append(0)
 
y = np.array(y)

# [Split 사용]
# 2. X와 y 각각에 대한 train, test data 추출 by split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,shuffle=True,random_state=42)

# 3. SVM를 사용하여 학습 진행 (using X_train,y_train)
from sklearn import svm

svc_model = svm.SVC(kernel = 'rbf', gamma = 0.05, C=0.6)
svc_model.fit(X_train,y_train)

# 4. SVC model predict(predict 함수에 X_test data를 사용하여 y_predict를 도출)
y_predict_svc = svc_model.predict(X_test)

target = 'A'
# 5. SVC 도출한 y_predict와 y_test를 비교하여 성능 평가
acc,pre,rec,f1 =classification_performance_eval(y_test,y_predict_svc,target)

print("[\"Grade A\" SVC & train_test_split 성능 평가]")
print("accuracy : ",acc)
print("precision : ",pre)
print("recall : ",rec)
print("f1-score : ",f1)

target = 'B'
# 5. SVC 도출한 y_predict와 y_test를 비교하여 성능 평가
acc,pre,rec,f1 =classification_performance_eval(y_test,y_predict_svc,target)

print("[\"Grade B\" SVC & train_test_split 성능 평가]")
print("accuracy : ",acc)
print("precision : ",pre)
print("recall : ",rec)
print("f1-score : ",f1)

target = 'C'
# 5. SVC 도출한 y_predict와 y_test를 비교하여 성능 평가
acc,pre,rec,f1 =classification_performance_eval(y_test,y_predict_svc,target)

print("[\"Grade C\" SVC & train_test_split 성능 평가]")
print("accuracy : ",acc)
print("precision : ",pre)
print("recall : ",rec)
print("f1-score : ",f1)


# In[ ]:




