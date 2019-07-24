# accuracy :  83.35%
import numpy as np 
import pandas as pd 
from sklearn.metrics import accuracy_score
from random import shuffle

temp_data= pd.read_csv('dataset.csv')
temp_data = temp_data.drop(columns=['Sunshine','Evaporation','Cloud3pm','Cloud9am','Location','RISK_MM','Date'],axis=1)
temp_data = temp_data.dropna(how='any')
#Lets deal with the categorical cloumns now
# simply change yes/no to 1/0 for RainToday and RainTomorrow
temp_data['RainToday'].replace({'No': 0, 'Yes': 1},inplace = True)
temp_data['RainTomorrow'].replace({'No': 0, 'Yes': 1},inplace = True)

#See unique values and convert them to int using pd.getDummies()
categorical_columns = ['WindGustDir', 'WindDir3pm', 'WindDir9am']
for col in categorical_columns:
    print(np.unique(temp_data[col]))
# transform the categorical columns
temp_data = pd.get_dummies(temp_data, columns=categorical_columns)
#pre-processing step
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
scaler.fit(temp_data)
temp_data = pd.DataFrame(scaler.transform(temp_data), index=temp_data.index, columns=temp_data.columns)
#feature selection
from sklearn.feature_selection import SelectKBest, chi2
X = temp_data.loc[:,temp_data.columns!='RainTomorrow']
Y = temp_data[['RainTomorrow']]
selector = SelectKBest(chi2, k=3)
selector.fit(X, Y)
X_new = selector.transform(X)
print(X.columns[selector.get_support(indices=True)]) #top 3 columns
temp_data = temp_data[['Humidity3pm','Rainfall','RainToday','RainTomorrow']]
X = temp_data[['RainToday','Humidity3pm']] # using two features
Y = temp_data[['RainTomorrow']]
#using decision tree algorithm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20)
print('the length of X_train is:',len(X_train))
dt_clf = DecisionTreeClassifier(random_state=0)
dt_clf.fit(X_train,Y_train)
Y_pred = dt_clf.predict(X_test)
accuracy = accuracy_score(Y_test,Y_pred)
print('Accuracy :',accuracy)

