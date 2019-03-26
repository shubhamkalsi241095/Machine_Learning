## Example 2

import pandas
from sklearn.preprocessing import LabelEncoder

malware_dataset = pandas.read_csv("C:/Users/user/Downloads/Final_Project.csv")
df = malware_dataset.iloc[1:,1:]

for column in df.columns:
    if df[column].dtype == type(object):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

X = malware_dataset.iloc[1:,1:1060]
y = malware_dataset.iloc[1:,1060:]


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_std = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_std,y,test_size=0.30,random_state=5)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(1),max_iter=1000)

model2 = mlp.fit(X_train,y_train.values.ravel())

y_test_pred = model2.predict(X_test)

from sklearn.metrics import accuracy_score
s=accuracy_score(y_test, y_test_pred)
print(s)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_test_pred,labels=[0,1])
print(pandas.DataFrame(confusion_matrix(y_test,y_test_pred,labels=[0,1]),index = ['true 0','true1'],columns=['pred0','pred1']))
