#!/usr/bin/env python
# coding: utf-8

# # Пример доктестов

# In[2]:


from typing import List
import doctest


# In[3]:


def is_positive(n: float) -> bool:
    """Check if number is positive
    
    >>> is_positive(-2)
    False
    >>> is_positive(-0.1)
    False
    >>> is_positive(0)
    True
    >>> is_positive(0.1)
    True
    
    """
    return n >= 0


# In[4]:


def filter_only_positive(numbers: List[float]) -> List[float]:
    """Return a list with positive numbers only
    
    
    >>> filter_only_positive([])
    []
    >>> filter_only_positive([1, 2, 3])
    [1, 2, 3]
    """
    return list(filter(is_positive, numbers))


# In[5]:


ex1 = []
filter_only_positive(ex1)


# In[6]:


ex2 = [1, 2, 3]
filter_only_positive(ex2)


# In[7]:


ex3 = [-2, -1, 0, 1, 2]
filter_only_positive(ex3)


# In[8]:


ex4 = [-10, 3, -5, 17]
filter_only_positive(ex4)


# In[9]:


doctest.testmod(verbose=False)


# In[9]:




