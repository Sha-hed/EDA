#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib
matplotlib.rcParams['figure.figsize'] =  (12, 6)


# In[2]:


df = pd.read_csv('zomato.csv', encoding='latin-1')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[8]:


df.shape


# In[9]:


cc = pd.read_excel('Country-Code.xlsx')
cc.head()


# In[10]:


cc.columns


# In[11]:


ff = pd.merge(df,cc,on='Country Code',how='left')
ff.head()


# In[12]:


ff.dtypes


# In[13]:


ff.Country


# In[14]:


ff.Country
ff.Country.value_counts()
cnames = ff.Country.value_counts().index
cvalues= ff.Country.value_counts().values


# In[15]:


## Pie Chart

plt.pie(cvalues[:3],labels=cnames[:3],autopct="%1.2f%%")
plt.show()


# In[16]:


ratings = ff.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[17]:


ratings 


# In[18]:


## We use hue for coloring our barplot 
# we cant get accurate color all the time, alternatively we can use palette and suggest 
# our own color : palette = ['white','blue','Green']
sns.barplot(data=ratings, x="Aggregate rating", y="Rating Count",hue="Rating color",palette=["white","red","orange","yellow","green","green"])


# In[28]:


sns.countplot(data=ratings, x='Rating color', palette=["blue","red","orange","yellow","green","green"])


# In[54]:


## Find the countries name that has given 0 rating 
ff[ff['Aggregate rating'] == 0].groupby('Country').size().reset_index().rename(columns={0:'Count'})


# In[77]:


## Find out which corrency is used by which country
ff.groupby(['Country','Currency']).size().reset_index()


# In[78]:


## Which Country Has Online Delivery Option 
ff.groupby(['Country','Has Online delivery']).size().reset_index()


# In[86]:


ff[ff['Has Online delivery'] == 'Yes'].Country.value_counts()


# In[87]:


ff.groupby(['Has Online delivery','Country']).size().reset_index()


# In[101]:


pie_city=ff.City.value_counts().values
pie_city
pie_names=ff.City.value_counts().index
pie_names


# In[108]:


plt.pie(x=pie_city[:5],labels=pie_names[:5], autopct="%1.2f")
plt.show()


# In[121]:


## Find the top ten cussinse
ff.Cuisines.value_counts().head(10).reset_index()
