import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data

data = pd.read_csv('C:/Users/ALLA/Desktop/data analysis projectes/data students.csv')
print(data)
print('___________________________________')


#data cleaning

print(data.isnull().sum())
print('___________________________________')

print(data.info())
print('___________________________________')

print(data.describe())
print('___________________________________')

print(data.duplicated())
print('___________________________________')



#data exploration

print(data['math score'].groupby(data['gender']).max())
print('___________________________________')

print(data['reading score'].groupby(data['race/ethnicity']).agg(['min','max','mean','sum','count']))
print('___________________________________')

print(data['writing score'].groupby(data['lunch']).count())
print('___________________________________')

print(data['math score'].groupby(data['race/ethnicity']).max())
print('___________________________________')

print(data['math score'].groupby(data['parental level of education']).agg(['min','max','mean','sum','count']))
print('___________________________________')

print(data['reading score'].groupby(data['test preparation course']).mean())
print('___________________________________')

print(data['writing score'].groupby(data['lunch']).agg(['min','max','mean','sum','count']))
print('___________________________________')



# data visualization

plt.bar(data['gender'],data['math score'],color='r',edgecolor='black',width=0.3)
plt.show()

plt.bar(data['race/ethnicity'],data['reading score'],color='b',edgecolor='black',width=0.3)
plt.show()

plt.bar(data['lunch'],data['writing score'],color='y',edgecolor='black',width=0.3)
plt.show()

plt.bar(data['test preparation course'],data['total'],color='g',edgecolor='black',width=0.3)
plt.show()

plt.bar(data['parental level of education'],data['total'],color='#6495ED',edgecolor='black',width=0.3)
plt.show()

X = data['total'].groupby(data['race/ethnicity']).max()
plt.pie(X.values,labels=X.index,autopct ='%1.4f%%',shadow=True, startangle=90)
plt.show()

Y = data['total'].groupby(data['parental level of education']).max()
plt.pie(Y.values,labels=Y.index,autopct='%1.4f%%',shadow=True, startangle=90)
plt.show()


data['id'] = np.arange(0,1000)
plt.scatter(data['id'],data['total'])
plt.show()

plt.hist(data['total'])
plt.show()
























#Q1

t = 0
f = 0

for i in data['math score']:
    if i >=50:
        t+=1
    elif i <50:
        f+=1
print(t,'\t',f)
print('___________________________________')


a = 0
s = 0

for i in data ['reading score']:
    if i >=50:
        a+=1
    elif i <50 :
        s+=1
print(a,'\t',s)
print('___________________________________')


z = 0
x = 0

for i in data['writing score']:
    if i >=50:
        z+=1
    
    elif i <50 :
        x+=1
print(z,'\t',x)    
print('___________________________________')

#Q2

data['total']=data['math score'] + data['reading score'] + data['writing score']

w = 0
n = 0

for i in data['total']:
    if i >=150:
        w+=1
    elif i <150 :
        n+=1
print(w,'\t',n)
print('___________________________________')


#Q3

        
    
    
        
        


        
        
        
        
    
        
        
        
        
    
    
        
        
        
 
        
        
  
    
  









