#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv(r"C:\Users\Surbhi\Desktop\weatherHistory.csv")


# In[5]:


data


# In[6]:


data.head()


# In[9]:


data.index


# In[10]:


data.shape


# In[11]:


data.columns


# In[12]:


data.dtypes


# In[16]:


data["Humidity"].unique()


# In[17]:


data["Daily Summary"].nunique


# In[18]:


data.count()


# In[ ]:


#all the unique 'Precip Type' in the data#

data.nunique()


# In[23]:


data.nunique()


# In[34]:


data["Precip Type"].nunique()


# In[ ]:


#number of times when Weather is clear#


# In[36]:


data.head()


# In[45]:


data["Summary"].value_counts()


# In[ ]:


#number of times wind speed was 9.7727#


# In[51]:


data.head()


# In[49]:


data[data["Wind Speed"]] == 9.7727


# In[53]:


data[data["Wind Speed (km/h)"] == 9.7727]


# In[ ]:


#find all the null values#


# In[54]:


data.isnull()


# In[55]:


data.isnull().sum()


# In[56]:


data.notnull()


# In[ ]:


#rename Summary to Status#


# In[57]:


data.rename(columns = {'Summary' : 'Status'})


# In[58]:


data.head()


# In[59]:


data.rename(columns = {'Summary' : 'Status'}, inplace =True)


# In[60]:


data.head()


# In[ ]:


#mean visibility#


# In[71]:


data['Visibility (km)'].mean()


# In[ ]:


#standard deviation of pressure#


# In[72]:


data['Pressure (millibars)'].std()


# In[ ]:


#variance of ' humidity'#


# In[73]:


data['Humidity'].var()


# In[ ]:


#when snow was recorded#


# In[77]:


data['Precip Type'].value_counts()


# In[ ]:


#when wind speed is above 30#


# In[78]:


data.head()


# In[83]:


#mean vale of each column against each Daily Summary#


# In[81]:


data.head(3)


# In[84]:


data.groupby('Daily Summary').mean()


# In[ ]:


#minimum and maximum values of each coloumn against each daily summary value#


# In[85]:


data.groupby('Daily Summary').min()


# In[89]:


data.groupby('Status').max()


# In[ ]:


#Weather is rain untill morning   OR Visibility is above 10#


# In[92]:


data[(data['Daily Summary']=='Rain untill morning') | (data['Visibility (km)'] > 10)]


# In[ ]:




