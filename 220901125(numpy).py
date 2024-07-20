#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a = np.array([[1, 2, 4], [5, 8, 7]])

print ("Array created using passed list:\n", a)


# In[2]:


b = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", b)


# In[3]:


c = np.full((3, 3), 6)
print ("\nAn array initialized with all 6s.\n", c)


# In[4]:


d = np.random.random((2, 2))
print ("\nA random array:\n", d)


# In[5]:


e = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", e)


# In[6]:


arr = np.array([[1, 2, 3, 4],[5, 2, 4, 2],[1, 2, 0, 1]])
newarr = arr.reshape(4, 3)
print ("\nOriginal array:\n", arr)
print ("Reshaped array[4,3]:\n", newarr)


# In[7]:


print("\nNo. of dimensions: ", arr.ndim)


# In[8]:


print("\nShape of array: ", arr.shape)


# In[9]:


print("\nSize of array: ", arr.size)


# In[10]:


print("\nArray stores elements of type: ",arr.dtype)


# In[11]:


flarr = arr.flatten()
print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)


# In[12]:


newtype=arr.astype('f')
print("\nConverted array elements:\n",newtype)
print("Converted array type:",newtype.dtype)


# In[14]:


arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print (arr)
print (arr[[4, 3, 0, 6]])
print (arr[[-3, -5, -7]])


# In[15]:


arr =np.arange(15).reshape((3, 5))
print (arr)
print (arr.shape)
print (arr.T)
print (arr.T.shape)


# In[16]:


arr = np.array([[1, 2, 3, 4],[5, 2, 4, 2],[3, 5, 8, 9],[5, 9, 2, 0],[1, 2, 0, 1]])
print("every alternate row\n",arr[0:4:2])
print("first 2 rows and 3 columns\n",arr[:2,:3])
print("except first 2 rows and 2columns\n",arr[2:,2:])
print("extracting 2nd row, 3rd value\n",arr[2,3])
print("first 2 rows\n", arr[:2])
print("except first 3 rows\n",arr[3:])
print("first 3 columns\n",arr[:,:3])


# In[17]:


print("Original array:\n", arr)
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1, 2), (2, 1),""(3, 0):\n", temp)


# In[19]:


cond=arr>2
temp=arr[cond]
print("\nElements greater than 2:\n",temp)


# In[20]:


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print("\nOriginal arrays:\n",arr1,arr2)
print("\nJoined array:\n",arr)


# In[21]:


arr = np.hstack((arr1, arr2))
print("\horizontal joining:\n",arr)


# In[22]:


print("\nOriginal arrays:\n",arr1,arr2)


# In[23]:


arr = np.vstack((arr1, arr2))
print("\nVertical joining:\n",arr)


# In[24]:


arr = np.dstack((arr1, arr2))
print("\nDepth joining:\n",arr)


# In[25]:


arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("\nOriginal Array:\n",arr)
print("\nSplitted array:\n",newarr)


# In[26]:


print("\nSplit array in another form:\n")
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[27]:


arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("Original array:",arr)
x = np.where(arr == 4)
print("\nIndexes where the value is 4:",x)


# In[31]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print("\nOriginal array:\n",arr)
print("\nIndexes where the values are even:",x)


# In[32]:


arr=np.array([[3,2,4],[5,0,1]])
print("\nOriginal array:",arr)
print("\nSorted array:",np.sort(arr))


# In[33]:


arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print("\nOriginal array:",arr)
print("\nFilter index:",x)
print("\nFilter array:",newarr)


# In[34]:


arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print("\nOriginal array:",arr)
print("\nFilter array:condition- >42:",filter_arr)
print("\nNew array:",newarr)


# In[35]:


arr1=[10,20,30,40,50]
arr2=[2,3,4,8,10]
a=np.array(arr1)
b=np.array(arr2)
print("Original arrays")
print(a)
print(b)


# In[36]:


print("\nVector addition")
print(a+b)


# In[37]:


print("\nVector subtraction")
print(a-b)


# In[38]:


print("\nVector multipilication")
print(a*b)


# In[39]:


print("\nVector division")
print(a/b)


# In[40]:


print("\nVector Dot product")
print(a.dot(b))


# In[41]:


print("\nScalar multipilication")
sclr=5
print("scalar value=",sclr)
print("array=",a)
print("result=",a*sclr)

