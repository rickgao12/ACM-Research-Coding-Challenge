#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


# In[2]:


data=pd.read_csv(r"C:\Users\rick\Desktop\VSCode\ACM-Research-Coding-Challenge\ClusterPlot.csv")


# In[3]:


plt.scatter(data["V1"], data["V2"])


# In[4]:


km = KMeans(n_clusters=3)


# In[5]:


y_pred = km.fit_predict(data[['V1','V2']])
y_pred


# In[6]:


data['cluster'] = y_pred


# In[7]:


data1 = data[data.cluster == 0]
data2 = data[data.cluster == 1]
data3 = data[data.cluster == 2]

plt.scatter(data1.V1, data1['V2'], color='green')
plt.scatter(data2.V1, data2['V2'], color='red')
plt.scatter(data3.V1, data3['V2'], color='black')

plt.xlabel('V1')
plt.ylabel('V2')


# In[8]:


possible_k = range(1,10)
sum_of_squares = []
for k in possible_k:
    km = KMeans(n_clusters=k)
    km.fit(data[['V1','V2']])
    sum_of_squares.append(km.inertia_)


# In[10]:


sum_of_squares


# In[11]:


plt.plot(possible_k, sum_of_squares)


# In[ ]:




