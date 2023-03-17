#!/usr/bin/env python
# coding: utf-8

# # a.Numbers

# In[1]:


1+1


# In[3]:


1*3


# In[4]:


1/2


# In[5]:


2**4


# In[6]:


4%2


# In[7]:


5%2


# In[8]:


(2+3) * (5+5)


# # b. variables assignment

# In[9]:


name_of_var=2


# In[10]:


x=2
y=3


# In[11]:


z=x+y


# In[12]:


z


# # Strings

# In[13]:


'single quotes'


# In[14]:


'double quotes'


# In[15]:


"wrap lot's a of other quotes"


# # Printing

# In[16]:


x= 'heelo'


# In[17]:


x


# In[18]:


print(x)


# In[19]:


num = 12
name = 'Sam'


# In[22]:


print('My name is: {one}, and my name is: {two}'.format(one=num, two=name))


# In[25]:


print('My name is : {}, and my name is: {}'.format(num,name))


# # Lists

# In[26]:


[1,2,3]


# In[27]:


['hi', 1, [1,2]]


# In[28]:


my_list = ['a','b','c']


# In[29]:


my_list.append('d')


# In[30]:


my_list


# In[31]:


my_list[0]


# In[32]:


my_list[1]


# In[33]:


my_list[1:]


# In[34]:


my_list[:1]


# In[35]:


my_list[0] = 'New'


# In[36]:


my_list


# In[37]:


nest = [1,2,3,[4,5, ['target']]]


# In[38]:


nest[3]


# In[39]:


nest[3][2]


# In[40]:


nest[3][2][0]


# # Dictionaries

# In[44]:


d= {'key1': 'item1', 'key2':'item2'}


# In[42]:


d


# In[45]:


d['key1']


# # Booleans

# In[46]:


True


# In[48]:


False


# # Tuples

# In[52]:


t=(1,2,3)


# In[53]:


t[0]


# In[56]:


t[0]=


# # Sets

# In[57]:


{1,2,3}


# In[58]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,1,1,2}


# # Comparison Operators

# In[59]:


1>2


# In[60]:


1<2


# In[61]:


1>=1


# In[62]:


1<=4


# In[63]:


1==1


# In[64]:


'hi' == 'bye'


# # Logic Operators

# In[66]:


(1>2) and (2<3)


# In[67]:


(1>2) or (2<3)


# In[68]:


(1==2) or (2==3) or (4==4)


# # If, elseif, else Statement

# In[69]:


if 1<2: print('Yep!')


# In[70]:


if 1<2: print('yep!')


# In[72]:


if 1<2: print ('first')
else:
    print('last')


# In[73]:


if 1> 2: print('first')
else:
    print('last')


# In[75]:


if 1==2: 
    print('first')
elif 3==3: 
    print('middle')
else :
    print('Last')


# # For loops

# In[76]:


seq = [1,2,3,4,5]


# In[77]:


for item in seq:
    print(item)


# In[78]:


for item in seq:
    print('yep')


# In[79]:


for jelly in seq: 
    print(jelly+jelly)


# # While Loops

# In[80]:


i=1
while i<5:
    print('i in: {}'.format(i))
    i=i+1


# # Range

# In[82]:


range(5)


# In[83]:


for i in range(5): 
    print(i)


# In[85]:


list(range(5))


# # List Comprehension

# In[86]:


x=[1,2,3,4]


# In[87]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[88]:


[item**2 for item in x] 


# # Functions

# In[92]:


def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)


# In[93]:


my_func


# In[94]:


my_func()


# In[95]:


my_func('new param')


# In[96]:


my_func('new param')


# In[97]:


def square(x):
    return x**2


# In[98]:


out = square(2)


# In[99]:


print(out)


# # r.Lambda expression

# In[100]:


def times2(var):
    return var*2


# In[101]:


times2(2)


# In[102]:


lambda var: var*2


# # s. Map and filter

# In[103]:


seq = [1,2,3,4,5]


# In[104]:


map(times2, seq)


# In[105]:


list(map(times2, seq))


# In[106]:


list(map(lambda var: var*2, seq))


# In[107]:


filter(lambda item: item%2 == 0, seq)


# In[108]:


list(filter(lambda item: item%2 == 0 ,seq))


# # Methods

# In[109]:


st = 'hello my name is Sam'


# In[110]:


st.lower()


# In[111]:


st.upper()


# In[112]:


st.split()


# In[113]:


tweet = 'Go Sportal # Sports'


# In[114]:


tweet.split('#')[1]


# In[115]:


d


# In[116]:


d.keys()


# In[117]:


d.items()


# In[118]:


lst = [1,2,3]


# In[119]:


lst.pop()


# In[121]:


lst


# In[122]:


'x' in [1,2,3]


# In[124]:


'x' in ['x', 'y' , 's']


# In[ ]:




