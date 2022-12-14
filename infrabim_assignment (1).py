# -*- coding: utf-8 -*-
"""InfraBIM Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HKWVhvKMXR4o74dq41Q-bZ4ek9OlV0ec

Reg. No:2041

Name:Ramakrishna Cheekoti

Date:10/10/2022
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("/content/Enrollments_28092022.csv")

data

"""1.Identifying Variables and their types"""

#for quantitative it gives numerical data type
#for qualitative it gives descriptive datatypr
data.info()

"""2.Size of Data"""

#No.of Rows and coloumns of data in form(rows,coloumns)
data.shape

rows=len(data)
columns=len(data.axes)
print(rows)
print(columns)

"""3.Histogram of different sections"""

#Histogram of Degree column in data
data.DEGREE.hist()

# Histogram of Intermediate coulum in data
data.INTERMEDIATE.hist()

#Histogram of SSC column in data
data.SSC.hist()

#Count of differnt internships present in data
nc=data['INTERNSHIP'].value_counts()
nc

dataFrame = pd.DataFrame({
   "INTERNSHIPS": ['Data Science','Cloud Computing Services','Mean Stack Web Development'],"REPRTITIONS": [156,90,51]
})

#4.Piechart for given data
plt.pie(dataFrame["REPRTITIONS"], labels = dataFrame["INTERNSHIPS"],autopct="%1.2f%%")
plt.show()

"""Mean,Mode,Median of Degree,Intermediate,SSC columns is shown below"""

dmd=data.DEGREE.mean()
dmd

did=data.INTERMEDIATE.mean()
did

data.SSC.mean()

data.DEGREE.mode()

data.INTERMEDIATE.mode()

data.SSC.mode()

data.DEGREE.median()

data.INTERMEDIATE.median()

data.SSC.median()

"""In the following cells we can see Minimum,Maximum,Standard Deviation,Coefficient of varience,range."""

data.describe()

ds=data.DEGREE.std()
ds

cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
cv(data.DEGREE)

cv(data.INTERMEDIATE)

cv(data.SSC)

rd=(data.DEGREE.max()-data.DEGREE.min())
rd

ri=(data.INTERMEDIATE.max()-data.INTERMEDIATE.min())
ri

rs=(data.SSC.max()-data.SSC.min())
rs

"""The following are th Standard scores of different sections of data"""

import scipy.stats as stats

print("Standard scores of DEGREE:")
print(stats.zscore(data['DEGREE']))

print("Standard scores of INTERMEDIATE:")
print(stats.zscore(data['INTERMEDIATE']))

print("Standard scores of SSC:")
print(stats.zscore(data['SSC']))

"""The following are BOX plots of different sections

9.Box plot and Outliers
"""

plt.boxplot(data['DEGREE'])
plt.show

plt.boxplot(data['INTERMEDIATE'])
plt.show

plt.boxplot(data['SSC'])
plt.show

"""The following is outlier function that helps in finding outliers of data of different sections"""

#Outlier Function
def outlier(a):
  q1=np.quantile(a,0.25)
  q3=np.quantile(a,0.75)
  iqr=q3-q1
  upper_bound=q3+(1.5*iqr)
  lower_bound=q1-(1.5*iqr)
  print("Inter-Quartile Range:",iqr)
  outliers=a[(a<=lower_bound)|(a>=upper_bound)]
  print("the following are outliers in box plot:\n{}".format(outliers))

outlier(data['DEGREE'])

outlier(data['INTERMEDIATE'])

outlier(data['SSC'])

"""The values of different sections that are Greater than 90% percentile are Given below:

10.No.of students with 90% percentile marks
"""

def fun(c):
  q9=np.quantile(c,0.9)
  li=c[c==q9]
  print("No.of students with 90% percentile:",li.count())

fun(data['DEGREE'])

fun(data['INTERMEDIATE'])

fun(data['SSC'])

