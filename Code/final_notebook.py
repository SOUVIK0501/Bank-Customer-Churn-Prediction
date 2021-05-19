# -*- coding: utf-8 -*-
"""Final_notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xfP8TBhR1e3srQwXv1_wFUNv0r26nTBm

<div style="text-align:center"><span style="color:green; font-family:Georgia; font-size:2em;">FINAL NOTEBOOK FOR BANK DATA SET</span></div>

### Importing all the necessary library functions
"""

# Commented out IPython magic to ensure Python compatibility.
# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

"""### Imporing the data set"""

bank_df = pd.read_csv("C:/Users/91977/OneDrive/Python/PROJECT (BANK)/bank-full.csv")
bank_df

"""### delete the column 'month'"""

print("Before", bank_df.shape)

bank_df = bank_df.drop(['month'], axis=1)

"After", bank_df.shape

"""### Modifying the 'job' column"""

def job_pro(x):
    if x["job"] == "retired" or x['job'] == 'student':
        return "B"
    if x["job"] == "admin." or x['job'] == 'services':
        return "D"
    if x["job"] == "blue-collar" or x['job'] == 'management' or x['job'] == 'technician':
        return "C"
    return "A"

bank_df.apply(lambda x:job_pro(x), axis = 1)

bank_df["job_profile"] = bank_df.apply(lambda x:job_pro(x), axis = 1)

def jobB(x):
    if x["job_profile"] == "B":
        return 1
    return 0
bank_df["job_B"] = bank_df.apply(lambda x:jobB(x), axis = 1)

"""### dropping the columns 'job' and 'job_profile'"""

print("Before", bank_df.shape)
bank_df = bank_df.drop(['job','job_profile'], axis=1)
"After", bank_df.shape

"""### Standardising the columns 'balance' and 'duration'"""

X = bank_df[['balance','duration']]
std_scale = preprocessing.StandardScaler().fit(X)
X_std = std_scale.transform(X)
x_stds = pd.DataFrame(data = X_std)
bank_df = pd.concat([bank_df,x_stds],axis=1)
bank_df.rename(columns={0:"Balance",1:"Duration"},inplace=True)
bank_df = bank_df.drop(['balance','duration'],axis=1)
#X_std = std_scale.transform(X)

"""### Modifying all the remaining categorical columns to numerical"""

bank_df['marital'] = bank_df['marital'].map( {'married': 1, 'single': 0, 'divorced':2}).astype(int)

bank_df['education'].fillna(value=0)
bank_df['education'] = bank_df['education'].map( {'unknown':0, 'primary': 1, 'secondary': 2, 'tertiary': 3} ).astype(int)

bank_df['default'] = bank_df['default'].map( {'yes': 1, 'no': 0}).astype(int)

bank_df['housing'] = bank_df['housing'].map( {'yes': 1, 'no': 0}).astype(int)

bank_df['loan'] = bank_df['loan'].map( {'yes': 1, 'no': 0}).astype(int)

bank_df['contact'].fillna(value=0)
bank_df['contact'] = bank_df['contact'].map( {'unknown': 0, 'telephone': 1, 'cellular':2}).astype(int)

bank_df['poutcome'].fillna(value=0)
bank_df['poutcome'] = bank_df['poutcome'].map( {'unknown': 0, 'failure': 1, 'success': 2, 'other': 3}).astype(int)

bank_df['y'] = bank_df['y'].map( {'yes': 1, 'no': 0}).astype(int)

bank_df.head()

"""### Train_Test_split"""

X_train = bank_df.drop('y',axis=1)
Y_train = bank_df['y']

X_Train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.30, random_state=42)

"""### Random Forest model"""

random_forestTest = RandomForestClassifier(random_state=10)
random_forestTest.fit(X_Train, y_train)
Y_predTest = random_forestTest.predict(X_Train)
acc_random_forest = round(random_forestTest.score(X_Train, y_train) * 100, 2)
acc_random_forest_test = round(random_forestTest.score(X_test, y_test) * 100, 2)
print('Train_Score =',acc_random_forest)
print('Test_Score= ',acc_random_forest_test)

"""### Random Forest model on entire data set"""

random_forestTest.fit(X_train, Y_train)
Y_predTest = random_forestTest.predict(X_Train)
acc_random_forest = round(random_forestTest.score(X_train, Y_train) * 100, 2)
#acc_random_forest_test = round(random_forestTest.score(X_test, y_test) * 100, 2)
print('Train_Score =',acc_random_forest)
#print('Test_Score= ',acc_random_forest_test)

"""<div style="text-align:center"><span style="color:red; font-family:Georgia; font-size:2em;"> NEW DATA SET </span></div>

### Read the data set
"""

df=pd.read_csv("C:/Users/91977/OneDrive/Python/bank.csv")
df

"""### make a copy of the data frame 'df'"""

df_trans=df
df_trans

df_trans['job'].unique()

"""### Drop the column 'month'"""

print("Before", df_trans.shape)

df_trans = df_trans.drop(['month'], axis=1)

"After", df_trans.shape

df_trans.head()

"""### Modify the 'job' column"""

def job_pro(x):
    if x["job"] == "retired" or x['job'] == 'student':
        return "B"
    if x["job"] == "admin." or x['job'] == 'services':
        return "D"
    if x["job"] == "blue-collar" or x['job'] == 'management' or x['job'] == 'technician':
        return "C"
    return "A"

df_trans.apply(lambda x:job_pro(x), axis = 1)

df_trans["job_profile"] = df_trans.apply(lambda x:job_pro(x), axis = 1)

def jobB(x):
    if x["job_profile"] == "B":
        return 1
    return 0
df_trans["job_B"] = df_trans.apply(lambda x:jobB(x), axis = 1)

df_trans.head()

"""### Drop the columns 'job' and 'job_profile'"""

print("Before", df_trans.shape)
df_trans = df_trans.drop(['job','job_profile'], axis=1)
"After", df_trans.shape

df_trans.head()

"""### Change all other categorical columns into numerical columns"""

df_trans['marital'] = df_trans['marital'].map({'single': 0, 'married': 1, 'divorced': 3}).astype(int)
df_trans.head()

df_trans['education'] = df_trans['education'].map({'unknown':0, 'primary':1, 'secondary':2, 'tertiary':3}).astype(int)
df_trans.head()

df_trans['default'] = df_trans['default'].map({'no':0, 'yes':1}).astype(int)

df_trans['housing'] = df_trans['housing'].map({'no':0, 'yes':1}).astype(int)

df_trans['loan'] = df_trans['loan'].map({'no':0, 'yes':1}).astype(int)

df_trans['contact'] = df_trans['contact'].map({'unknown':0, 'telephone':1, 'cellular':2}).astype(int)

df_trans['poutcome'] = df_trans['poutcome'].map({'unknown':0, 'failure':1, 'success':2, 'other':3}).astype(int)

df_trans['y'] = df_trans['y'].map({'no':0, 'yes':1}).astype(int)

df_trans.head()

"""### Standardising the columns 'balance' and 'duration'"""

X = df_trans[['balance','duration']]
std_scale = preprocessing.StandardScaler().fit(X)
X_std = std_scale.transform(X)
x_stds = pd.DataFrame(data = X_std)
df_trans = pd.concat([df_trans,x_stds],axis=1)
df_trans.rename(columns={0:"Balance",1:"Duration"},inplace=True)
df_trans = df_trans.drop(['balance','duration'],axis=1)

df_trans.head()

"""### Train_Test_Split"""

X_train = df_trans.drop('y',axis=1)
Y_train = df_trans['y']

X_Train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.30, random_state=42)

"""### Random Forest model for the whole data set"""

random_forestTest = RandomForestClassifier(random_state=10)
random_forestTest.fit(X_train, Y_train)
Y_predTest = random_forestTest.predict(X_Train)
acc_random_forest = round(random_forestTest.score(X_train, Y_train) * 100, 2)
print('Train_Score =',acc_random_forest)

"""### Dropping the column 'y'"""

df_trans= df_trans.drop('y',axis=1)
df_trans.head()

"""### Prediction test """

Y_predTest = random_forestTest.predict(df_trans)

Y_predTest

"""#### Converting the numpy array into dataframe and rename the column"""

df2=pd.DataFrame(Y_predTest)
df2.rename(columns={0:"ypred"},inplace=True)
df2.head()

"""### Probability test"""

Y_probTest = random_forestTest.predict_proba(df_trans)
Y_probTest

"""#### Converting the numpy array into dataframe"""

df3=pd.DataFrame(Y_probTest)
df3.head()

"""#### Drop the column for 0 probability"""

df3=df3.drop(0,axis=1)
df3.head()

df3.head()

"""#### Rename the column for 1 probability"""

df3.rename(columns={1:"y=1_prob"},inplace=True)
df3.head()

"""### Concatinating the prediction test and probability test"""

df2=pd.concat([df2,df3],axis=1)

df2.head()

"""### Concatinating df2 with the main dataframe (i.e df)"""

df=pd.concat([df,df2],axis=1)
df.head()

"""## Save the main dataframe (i.e. df) as csv file"""

df.to_csv("modified_Bank.csv",index=False)

