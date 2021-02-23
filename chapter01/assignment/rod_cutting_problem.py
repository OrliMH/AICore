#!/usr/bin/env python
# coding: utf-8

# In[86]:


#rod cutting problem
'''
given rod of len n and the price of rod of len i, 
i from 1 to n, calculate the maximum price after
cutting or without cutting the rod

dp:
n=0:cutRod(n)=0
n!=0:cutRod(n)=max(p(i)+cutRod(n-i)),i from 1 to n


'''


# In[82]:



import numpy as np
def userinput():
    
    n=int(input('input len of rob: '))
    
    p=np.zeros(n+1)
    
    for i in range(n):        
        p[i+1]=int(input(f'input the price of len {i+1}: '))
   
        
    return n,p


             


# In[83]:


def cutRod(x,p):
  
    if x==0:
        return 0
    
    m=0
    for i in range(1,x+1):
        m=max(m,p[i]+cutRod(x-i,p))
    return m
        


# In[84]:


if __name__ == "__main__":
    n,p = userinput()    
    print(cutRod(n,p))
    

