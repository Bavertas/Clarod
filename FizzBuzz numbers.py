#!/usr/bin/env python
# coding: utf-8

# In[10]:


say = int(input("Lutfen Bir Sayi Giriniz :"))

if say%15 == 0 :
    print("FizBuzz")
elif say%5 == 0:
    print("Buzz")
elif say%3 == 0:
    print("Fizz")
else:
    print(say)


# In[ ]:




