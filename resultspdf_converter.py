#!/usr/bin/env python
# coding: utf-8

# ## importing all required packages

# In[1]:


import tabula
import numpy as np
import pandas as p


# ## converrting pdf file to csv

# In[2]:


tabula.convert_into(r"C:\Users\Admin\Downloads\Results for I B.Tech II semester (R19R16) RegularSupplementary Examinations DEC 2020.pdf", "result.csv", output_format="csv", pages='all')


# #### Reading CSV file

# In[4]:


result_csv=p.read_csv("result.csv")


# In[7]:


result_csv.columns


# ##### only getting sutdents of hallticket no of CSE students and Subjects of CSE students

# In[14]:


cs_ht=result_csv.loc[result_csv['Htno'].str.startswith("19F01A05")]
cs_ht=list(cs_ht['Htno'].unique())
cs_sub=result_csv[result_csv["Htno"]==cs_ht[0]]
cs_sub=list(cs_sub['Subname'])


# # creating an empty data frame with HTNO and cse subjects as columns

# In[18]:


final=p.DataFrame(columns=['HTNO',*cs_sub])


# In[19]:


final


# ## now adding data in empty data frame using for loop

# In[21]:


for i in cs_ht:
    grade=result_csv.loc[result_csv['Htno']==i]
    grade=list(grade['Grade'])
    data=[i,*grade]
    final.loc[len(final)]=data
    

# In[22]:


final


# In[36]:


final.to_excel("result.xlsx")


# #### using multiple queries from data frame

# In[35]:


final.loc[(final[cs_sub[0]]=='F') &( final[cs_sub[1]]=='F')]


# In[ ]:




