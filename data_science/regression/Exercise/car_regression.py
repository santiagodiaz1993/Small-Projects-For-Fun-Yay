'''
Questions we want to answer:
   What is the price in the future?
Steps we need to take:
Lable the information [done]
Inspect information and get most important attributes
Drop none significant information

note: A good pactice is to fill values with the avrage of the column. 
This will need to be done where the values are ?'
'''''

import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math

df = pd.read_csv('imports-85.data')

''' Look for interaction between all factors against price '''
y = df['price'].replace('?', 0)
y = pd.to_numeric(y)
y = np.array(y)

for factor in df:
    colum_X = df[factor].sort_values(ascending=True)
    plt.title(factor + ' vs price')
    plt.xlabel(factor)
    plt.ylabel('price')
    plt.scatter(colum_X, y)
    plt.show()

''' Pick all factors that will be used to predict the car's price based on the interaction
from all of the factors'''

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

#plt.scatter(dfe, y)
plt.title('Price vs highway mpg')
plt.xlabel('Symboling')
plt.ylabel('Price')
plt.show()

example = X_practice 
example = np.array(example)
example_result = clf.predict(example)

