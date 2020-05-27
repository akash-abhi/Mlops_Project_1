#!/usr/bin/env python
# coding: utf-8

# In[45]:


from keras.datasets import mnist


# In[46]:


import os


# In[47]:


(X_train,y_train),(X_test,y_test) = mnist.load_data()


# In[48]:


X_train=X_train.reshape(60000,28,28,1)


# In[49]:


X_test=X_test.reshape(10000,28,28,1)


# In[50]:


from keras.utils import to_categorical


# In[51]:


y_train = to_categorical(y_train)


# In[52]:


y_test = to_categorical(y_test)


# In[53]:


from keras.models import Sequential


# In[54]:


from keras.layers import Dense, Conv2D,Flatten


# In[55]:


model = Sequential()


# In[56]:


model.add(Conv2D(2, kernel_size=3, activation="relu",input_shape=(28,28,1)))


# In[43]:


try:
   f=open("/layers.txt","r")
   i = f.read()
except:
   print(end="")
finally:
    f.close()
    print(i)

    #i = int(i)
n=4


# In[57]:


i=2
n=4


# In[58]:


for i in range(i):
    model.add(Conv2D(filters=n,kernel_size=3,activation="relu"))
    n=n*2
    


# In[59]:


model.add(Flatten())


# In[60]:


model.add(Dense(10,activation="softmax"))


# In[61]:


model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])


# In[62]:


model.fit(X_train,y_train,epochs=1)


# In[63]:


Accuracy=model.evaluate(X_test,y_test)


# In[64]:


print("Accuracy is :-",Accuracy[1]*100)


# In[23]:


#os.system('echo{} | cat /Users/AKS/Desktop/accuracy.txt'.format(str(int(Accuracy[1]))))


# In[41]:


try:
   f=open("/data.txt","w")
   f.write(str(int(Accuracy[1]*100)))
except:
   print(end="")
finally:
    f.close()


# In[ ]:


from keras.datasets import mnist
import os
(X_train,y_train),(X_test,y_test) = mnist.load_data()
X_train=X_train.reshape(60000,28,28,1)
X_test=X_test.reshape(10000,28,28,1)
from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
from keras.models import Sequential
from keras.layers import Dense, Conv2D,Flatten
model = Sequential()
model.add(Conv2D(2, kernel_size=3, activation="relu",input_shape=(28,28,1)))
try:
   f=open("/layers.txt","r")
   i = f.read()
except:
   print(end="")
finally:
    f.close()
    print(i)

    #i = int(i)
n=4


# In[45]:




