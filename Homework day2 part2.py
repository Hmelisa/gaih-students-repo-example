#!/usr/bin/env python
# coding: utf-8

# In[1]:


n= int(input("Please enter a single digit integer."))
while not 0<n<10:
    n= int(input("Please enter a single digit integer."))


# In[2]:


print(n)


# In[3]:


even=[i for i in range(0,n+1) if i % 2 == 0]


# In[4]:


print(even)


# In[ ]:




