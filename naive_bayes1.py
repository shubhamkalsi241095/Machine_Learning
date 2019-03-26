# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 02:00:16 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 00:59:21 2019

@author: user
"""
import numpy
import pandas
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder


malware_dataset = pandas.read_csv("C:/Users/user/Downloads/Final_Project.csv")
df = malware_dataset.iloc[1:,1:]


for column in df.columns:
    if df[column].dtype == type(object):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

X = malware_dataset.iloc[1:,1:1060]
y = malware_dataset.iloc[1:,1060:]

from sklearn.preprocessing import StandardScaler
standardizer = StandardScaler()
X_std = standardizer.fit_transform(X)

from sklearn.model_selection import train_test_split
### type your code here ###
X_train,X_test,y_train,y_test = train_test_split(X_std,y,test_size =0.30,random_state = 5)

model = GaussianNB()
model.fit(X_train, y_train)

y_test_pred = model.predict(X_test)
print(metrics.accuracy_score(y_test,y_test_pred))

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_test_pred,labels=[0,1])
print(pandas.DataFrame(confusion_matrix(y_test,y_test_pred,labels=[0,1]),index = ['true 0','true1'],columns=['pred0','pred1']))

print(metrics.classification_report(y_test, y_test_pred))

from sklearn.model_selection import cross_val_score
for i in range(1,10):
    model2=GaussianNB(priors=None)
    model3 = model2.fit(X_train,y_train)
    scores = cross_val_score(estimator=model3,X=X_train,y=y_train,cv=5)
    print(i,':',numpy.average(scores))
