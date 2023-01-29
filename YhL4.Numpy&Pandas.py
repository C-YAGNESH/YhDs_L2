#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([1,2,3])
arr


# In[11]:


list=[[1,2,3],[4,5,6]]
np.array(list)


# In[12]:


np.arange(12)


# In[13]:


np.random.rand(3,2)


# In[14]:


np.random.randn(3,2)


# In[15]:


sample_array=np.arange(20)


# In[16]:


sample_array.reshape(4,5)


# In[17]:


np.eye(6)


# In[24]:


np.eye(6),int


# In[25]:


sample_array.min()


# In[26]:


sample_array.max()


# In[27]:


sample_array.dtype()


# In[29]:


####Pandas


# In[30]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/Yhills_July12_Analytics/main/titanic-training-data.csv")


# In[33]:


df.head(10)


# In[34]:


df.shape


# In[35]:


df.tail(10)


# In[40]:


df.columns


# In[43]:


df.dtypes


# In[44]:


df.info()


# In[46]:


df.isnull().sum()


# In[47]:


df.describe()


# In[48]:


df.describe().T


# In[51]:


df.describe(include="all").T


# In[ ]:




