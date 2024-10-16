#!/usr/bin/env python
# coding: utf-8

# In[52]:


#DATA PREPROCESSING AND DATA CLEANING 


# In[1]:


#Read my dataset into the Jupyter Notebook
import pandas as pd
df=("user_behavior_dataset.csv")
read=pd.read_csv(df)
read


# In[3]:


#Display the first 11 rows from index 0
read.head(11)


# In[7]:


#Display the last 10 rows
read.tail(10)


# In[19]:


#display the total number of rows and columns in the dataset
read.shape


# In[15]:


#The columns in the dataset described
read.columns


# In[21]:


#Check for datatypes in the columns of the dataset
read.dtypes


# In[23]:


#General overview of the dataset
read.info()


# In[25]:


#Check for duplicates in the rows and columns
read.duplicated()


# In[27]:


#Sum of the duplicates found
read.duplicated(). sum()


# In[29]:


#Summary statistics for quantitative data
read.describe()


# In[37]:


read.isnull().sum()


# In[41]:


#Once completeness has been achieved uniqueness is automatically proven


# In[48]:


import pandas as pd

#the dataframe
dataset=("user_behavior_dataset.csv")
read=pd.read_csv(dataset)

#Identify numerical columns
numeric_read=read.select_dtypes(include='number')

#Calculate Q1 and Q3 and IQR
Q1=numeric_read.quantile(0.25)
Q3=numeric_read.quantile(0.75)
IQR=Q3-Q1

#Define outlier bounds
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

#Create a mask for outliers (Use logical conditions to identify rows that contain outliers in any numerical column)
outlier_mask=~((numeric_read<lower_bound)|(numeric_read>upper_bound)).any(axis=1) #axis=1 confirms that we are working on rows

#Filter the Dataframe to remove outliers,keeping non-numerical columns
read_no_outliers=read[outlier_mask]

#Display the results
print("Original Dataframe:")
print(read)
print("\nDataFrame without outliers:")
print(read_no_outliers)


# In[50]:


#Outliers have not been found hence dataframe mantains its original shape of 700 rowsx 11columns

