#!/usr/bin/env python
# coding: utf-8

# In[2]:


kımon= [1, 2, 3, 4, 5, 6]


# In[3]:


for i in range(0, 3):
    kımon.append(kımon[0])
    kımon.pop(0)


# In[4]:


print(kımon)

