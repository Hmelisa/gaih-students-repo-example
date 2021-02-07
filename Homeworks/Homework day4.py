#!/usr/bin/env python
# coding: utf-8

# In[31]:


def prime(x):
    asal=0
    primenumbers=[]
    for i in range(2,x):
        for j in range(2,i):
            if i%j==0 :
                asal=1
        if asal==0:
            primenumbers.append(i)
        asal=0
    print("Prime numbers between 0 and", x, ":" , primenumbers)


# In[32]:


prime(100)

