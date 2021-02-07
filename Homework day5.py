#!/usr/bin/env python
# coding: utf-8

# In[79]:


class Animals():
    
    def __init__(self, name, habitat, nutrition, respiratory):
        self.name = name
        self.habitat = habitat
        self.nutrition = nutrition
        self.respiratory = respiratory
        
    def info(self):
        print(self.name, "lives in", self.habitat, ", is a", self.nutrition, ", breathes through it's", self.respiratory)


# In[80]:


class dogs(Animals):
    def __init__(self, name, habitat, nutrition, respiratory, breed, age):
        super().__init__(name,habitat, nutrition, respiratory)
        self.breed = breed
        self.age = age
    def doginfo(self):
        print(self.name, "is a", self.age, "years old", self.breed, "and lives in", self.habitat)


# In[87]:


class cats(Animals):
    def __init__(self, name, habitat, nutrition, respiratory, breed, weight):
        super().__init__(name,habitat, nutrition, respiratory)
        self.breed = breed
        self.weight = weight
    def catinfo(self):
        print(self.name, "is a",self.weight,"kg", self.breed, "cat","and lives in", self.habitat)
        


# In[88]:


shark = Animals("shark", "seas", "carnivore", "gills")
shark.info()
elephant = Animals("elephant", "Africa", "herbivore", "lungs")
elephant.info()


# In[89]:


venus=dogs("Venus","my house","carnivore","lungs","terrier",4)
venus.doginfo()


# In[90]:


uzay=cats("Uzay","garden","carnivore","lungs","Van",5)
uzay.catinfo()


# In[ ]:




