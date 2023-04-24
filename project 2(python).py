#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd 
df = pd.read_csv(r"C:\Users\Surbhi\Desktop\8. Netflix Dataset.csv")


# In[6]:


df.head()


# In[12]:


df.tail()


# In[13]:


df.shape


# In[14]:


df.size


# In[15]:


df.columns


# In[16]:


df.dtypes


# In[17]:


df.info()


# In[18]:


df.shape


# In[19]:


#to find duplicates#
df[df.duplicated()]


# In[20]:


df.drop_duplicates(inplace= True)


# In[21]:


df[df.duplicated()]


# In[22]:


df.isnull()


# In[23]:


df.isnull().sum()


# In[24]:


#null values with visualization#
import seaborn as sns


# In[25]:


sns.heatmap(df.isnull())


# In[26]:


df.head()


# In[32]:


#information about particular show#
df.info()


# In[33]:


df.describe()


# In[34]:


#to find specific details of an element#
df[df['Title'].isin(['House of Cards'])]


# In[36]:


df[df['Title'].str.contains('13 Reasons Why')]


# In[39]:


df['Date_N']= pd.to_datetime(df['Release_Date'])


# In[41]:


df.head()


# In[42]:


#year in which highest number of movies and shows were released#
df['Date_N'].dt.year.value_counts()


# In[45]:


df['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[47]:


#categories#
df.head(2)


# In[49]:


df.groupby('Category').Category.count()


# In[51]:


sns.countplot(df['Category'])


# In[52]:


#movies in a prticular year#
df['Year']= df['Date_N'].dt.year


# In[53]:


df.head(1)


# In[56]:


df[(df['Category'] == 'Movie') & (df['Year']==2018)]


# In[60]:


#filtering shows on the basis of country along with titles#
df[(df['Category']=='TV Show') & (df['Country']=='India')]


# In[61]:


df[(df['Category']=='TV Show') & (df['Country']=='India')]['Title']


# In[64]:


#top 20 directors giving most numbers of movies #
df['Director'].value_counts()


# In[66]:


df['Director'].value_counts().head(20)


# In[71]:


#appliction of AND and OR operator#
df[(df['Category']=='Movie') & (df['Type']=='Comedies')]


# In[72]:


#category=movie and type is comedies or country is india#
df[(df['Category']=='Movie') & (df['Type']=='Comedies')| (df['Country']=='India')] 


# In[74]:


#in how many movie Jennifer Aniston Was casted#
df[(df['Category']=='Movie') & (df['Cast']=='Jennifer Aniston')]


# In[81]:


#in how many TV Show Anupam Kher Was casted#
df[(df['Category']=='Movie') & (df['Cast']== 'Hrithik Roshan')]


# In[82]:


#now removing null values to get above answer#
df1=df.dropna()


# In[83]:


df1[df1['Cast'].str.contains('Hrithik Roshan')]


# In[85]:


#types of ratings#
df.head()


# In[86]:


df['Rating'].nunique()


# In[89]:


df['Rating'].unique()


# In[93]:


#number of movies having PG-13 ratings in india#
df[(df['Category']=='Movie') & (df['Rating']=='PG-13') & (df['Country']=='India')]


# In[94]:


df[(df['Category']=='Movie') & (df['Rating']=='PG-13') & (df['Country']=='India') & (df['Year'] > 2018)]


# In[95]:


df.Duration.unique()


# In[96]:


#to change type#
df.Duration.dtype


# In[97]:


#make two new columns for numeric and string values#
df[['Minutes','Units']] = df['Duration'].str.split(' ', expand=True)


# In[98]:


df.head(2)


# In[99]:


df['Minutes'].max()


# In[100]:


df['Units'].max()


# In[102]:


#country with highest number of tv shows#
df_tvshows = df[df['Category']=='TV Show']


# In[103]:


df_tvshows.head()


# In[105]:


df_tvshows.Country.value_counts()


# In[108]:


#shorting by year ascending order#
df.sort_values(by= 'Year', ascending = True)


# In[ ]:




