#!/usr/bin/env python
# coding: utf-8

# In[3]:


names = []
scores = [] 
age = []
result_f = open("results.txt") 
for line in result_f: 
    (name, score) = line.split() 
    scores.append(float(score)) 
result_f.close() 
scores.sort(reverse = True) 
print("The top scores were:") 
print(scores[0]) 
print(scores[1]) 
print(scores[2])


# In[ ]:




