#!/usr/bin/env python
# coding: utf-8

import pymysql
import numpy as np

# 5-1 성능 평가 함수
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

y = [1 if t['grade'] == 'B' else -1 for t in data]
y = np.array(y)

# [Split 사용]
# 2. X와 y 각각에 대한 train, test data 추출 by split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)

# 3-1. SVM를 사용하여 학습 진행 (using X_train,y_train)
from sklearn import svm

svc_model = svm.SVC(kernel = 'rbf', gamma = 0.6, C=500)
svc_model.fit(X_train,y_train)

# 3-2. Logistic Regression을 사용하여 학습 진행
from sklearn.linear_model import LogisticRegression

logi_model = LogisticRegression(C=0.3,max_iter=100)

# scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_logi = scaler.fit_transform(X_train)
X_test_logi = scaler.transform(X_test)
#

logi_model.fit(X_train_logi,y_train)

# 4-1. SVC model predict(predict 함수에 X_test data를 사용하여 y_predict를 도출)
y_predict_svc = svc_model.predict(X_test)
print("y_test")
print(y_test)
print("y_predict")
print(y_predict_svc)

# 4-2. LogisticRegression model predict(predict 함수에 X_test data를 사용하여 y_predict를 도출)
y_predict_logi = logi_model.predict(X_test_logi)
print("y_test")
print(y_test)
print("y_predict")
print(y_predict_logi)

# 5-1. SVC 도출한 y_predict와 y_test를 비교하여 성능 평가
acc,pre,rec,f1 =classification_performance_eval(y_test,y_predict_svc)

print("[SVC 성능 평가]")
print("accuracy : ",acc)
print("precision : ",pre)
print("recall : ",rec)
print("f1-score : ",f1)

# 5-2. LogisiticRegression 도출한 y_predict와 y_test를 비교하여 성능 평가
acc,pre,rec,f1 =classification_performance_eval(y_test,y_predict_logi)

print("[LogisticRegression 성능 평가]")
print("accuracy : ",acc)
print("precision : ",pre)
print("recall : ",rec)
print("f1-score : ",f1)

# # [K-fold 사용]
# from sklearn.model_selection import KFold
# from sklearn import tree

# acc = []
# pre = []
# rec = []
# f1 = []

# # 2. K-fold attribute 설정
# kf = KFold(n_splits=5,random_state=42,shuffle=True)

# # 3. K-fold에서 추출한 train과 test index를 기준으로 X,y 각각의 train,test data를 설정해준다.
# # kf.split(X)는 n_splits만큼의 경우를 갖고있다.
# for train_index,test_index in kf.split(X):
#     X_train, X_test = X[train_index], X[test_index]
#     y_train, y_test = y[train_index], y[test_index]
    
#     # 4. Decision tree를 사용하여 학습 진행 (using X_train,y_train)
#     dtree = tree.DecisionTreeClassifier()
#     dtree_model = dtree.fit(X_train,y_train)
    
#     # 5. predict 함수에 X_test data를 사용하여 y_predict를 도출
#     y_predict = dtree_model.predict(X_test)
    
#     # 6. 도출한 y_predict와 y_test를 비교하여 성능 평가
#     accuracy,precision,recall,f1_score = classification_performance_eval(y_test,y_predict)
    
#     # 7. 각 성능 배열에 append하여 추가
#     acc.append(accuracy)
#     pre.append(precision)
#     rec.append(recall)
#     f1.append(f1_score)
    
# # 8. 각 성능의 평균값 구한다.
# import statistics
# print("[K-fold 성능 평가]")
# print("accuracy :",statistics.mean(acc))
# print("precision :",statistics.mean(pre))
# print("recall : ",statistics.mean(rec))
# print("f1-score : ",statistics.mean(f1))

