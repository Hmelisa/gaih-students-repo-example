#!/usr/bin/env python
# coding: utf-8

# In[16]:


class employees():
    def __init__(self, name, age, language):
        self.name=name
        self.age=age
        self.language=language


# In[17]:


class managers():
    def __init__(self, name, age, language):
        self.name=name
        self.age=age
        self.language=language


# In[18]:


emp1=employees("Melisa", 27, "Italian")
emp2=employees("Can", 32, "Spanish" )
emp3=employees("Batuhan", 29, "English")
emp4=employees("Ayşe", 36, "English")
emp5=employees("Mevlüt", 37, "Russian")
man1=managers("Halime", 45, "French")
man2=managers("Bayram", 48, "Spanish")


# In[19]:


Languages={emp1.language, emp2.language, emp3.language, emp4.language, emp5.language ,man1.language, man2.language}  


# In[20]:


print(Languages)

