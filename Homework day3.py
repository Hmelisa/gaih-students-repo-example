#!/usr/bin/env python
# coding: utf-8

# In[ ]:


un1= "Melisa"
p1= 123456
un2=str(input("Please enter your username."))
p2=int(input("Please enter your password."))


# In[ ]:


n=1
while n >0 :
    if un1==un2 and p1==p2:
        print("logged in")
        break
    elif un1!=un2 and p1==p2:
        print("wrong username")
        un2=str(input("Please enter your username."))
    elif un1==un2 and p1!=p2:
        print("wrong password")
        p2=int(input("Please enter your password."))
    else:
        print("wrong username and password")
        un2=str(input("Please enter your username."))
        p2=int(input("Please enter your password."))

        


# # extra part

# In[ ]:


info= {un1 : "Melisa", p1 : 123456}
login= {un2: str(input(("Please enter your username."))), p2: int(input("Please enter your password."))}
while n>0:
    if info[un1] == login[un2] and info[p1] == login[p2]:
        print("logged in")
        break
    elif info[un1] != login[un2] and info[p1] == login[p2]:
        print("wrong username")
        login[un2] =str(input("Please enter your username."))
    elif info[un1] == login[un2] and info[p1] != login[p2]:
        print("wrong password")
        login[p2] =int(input("Please enter your password."))
    else:
        print("wrong username and password")
        login[un2]=str(input("Please enter your username."))
        login[p2]=int(input("Please enter your password."))


# In[ ]:




