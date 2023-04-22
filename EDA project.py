#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns                      
import matplotlib.pyplot as plt             
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


df = pd.read_csv("data.csv")


# In[3]:


df.head(5) 


# In[4]:


df.tail(5)   


# In[5]:


df.dtypes


# In[6]:


df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
df.head(5)


# In[7]:


df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
df.head(5)


# In[8]:


df.shape


# In[9]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)


# In[10]:


df.count()


# In[11]:


df = df.drop_duplicates()
df.head(5)


# In[12]:


df.count()


# In[13]:


df.isnull().sum()


# In[14]:


df = df.dropna()    
df.count()


# In[15]:


print(df.isnull().sum())


# In[17]:


sns.boxplot(x=df['Price'])


# In[18]:


sns.boxplot(x=df['HP'])


# In[19]:


sns.boxplot(x=df['Cylinders'])


# In[20]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[21]:


df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape


# In[22]:


df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');


# In[24]:


plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[25]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()


# Hence the above are some of the steps involved in Exploratory data analysis
