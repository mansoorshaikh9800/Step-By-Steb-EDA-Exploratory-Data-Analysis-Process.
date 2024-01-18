#!/usr/bin/env python
# coding: utf-8

# # 1: Import Python Libraries

# In[1]:


# 'Pandas' is used for data manipulation and analysis
import pandas as pd

# 'Numpy' is used for mathematical operations on large, multi-dimensional arrays and matrices
import numpy as np

# 'Matplotlib' is a data visualization library for 2D and 3D plots, built on numpy
import matplotlib.pyplot as plt

# 'Seaborn' is based on matplotlib; used for plotting statistical graphics
import seaborn as sns

#to ignore warnings
import warnings
warnings.filterwarnings('ignore')


# # 2.Importing and Reading Dataset

# In[2]:


data = pd.read_csv("C:\\Users\\admin\\Desktop\\used_cars_data.csv")


# In[3]:


# # showing the first 5 rows of the dataset:
data.head()


# In[4]:


# # showing the last 5 rows of the dataset:
data.tail()


# In[5]:


# Checking the info of the data:
data.info()


# # 3.Missing Value

# In[6]:


# use isnull().sum() to check for missing values 
data.isnull().sum()


# In[7]:


data.nunique()


# In[8]:


(data.isnull().sum()/(len(data)))*100


# # 4: Data Reduction

# In[9]:


# Remove S.No. column from data
data = data.drop(['S.No.'], axis = 1)
data.info()


# # 5.Feature Engineering

# In[10]:


from datetime import date
date.today().year
data['Car_Age']=date.today().year-data['Year']
data.head()


# In[11]:


data['Brand'] = data.Name.str.split().str.get(0)
data['Model'] = data.Name.str.split().str.get(1) + data.Name.str.split().str.get(2)
data[['Name','Brand','Model']]


# # 6: Data Cleaning/Wrangling

# In[12]:


print(data.Brand.unique())
print(data.Brand.nunique())


# In[13]:


searchfor = ['Isuzu','ISUZU','Mini','Land']
data[data.Brand.str.contains('|'.join(searchfor))].head(5)


# In[14]:


data['Brand'].replace({"ISUZU":"Isuzu","Mini":"Mini cooper","Land":"Land Rover"}, inplace=True)


# # 7: EDA Exploratory Data Analysis

# # Statistics Summary

# In[15]:


data.describe()


# In[16]:


data.describe().T


# In[ ]:


data


# In[ ]:




