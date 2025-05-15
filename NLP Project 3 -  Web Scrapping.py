#!/usr/bin/env python
# coding: utf-8

# # Web Scrapping
# 

# In[99]:


import pandas as pd
import numpy as np

from bs4 import BeautifulSoup as bs
import csv
import requests


# In[100]:


url = 'https://www.flipkart.com/apple-iphone-16-teal-128-gb/product-reviews/itmce4bb3f55cc2f?pid=MOBH4DQFSY9ETDUU&lid=LSTMOBH4DQFSY9ETDUU6JV9DJ&sortOrder=MOST_HELPFUL&certifiedBuyer=false&aid=overall'


# In[101]:


url


# In[102]:


response = requests.get(url)


# ### Scrapping using inbuild library Beautifulsoup

# In[103]:


soup = bs(response.content, features='xml')


# In[104]:


soup = bs(response.content)


# In[105]:


print(bs.prettify(soup))


# In[106]:


# Extract Informations from the users

name = soup.find_all('p', class_ ="_2NsDsF AwS1CA" )

name


# In[115]:


title = soup.find_all('p', class_ = "z9E0IG")

title


# In[116]:


rating = soup.find_all('div', class_ = "XQDdHH Ga3i8K")

rating


# In[117]:


comments = soup.find_all('div', class_ ="ZmyHeo" )
comments


# In[126]:


#

Name = []
Title = []
Rating = []
Comments = []


# In[127]:


for i in name:
    Name.append(i.get_text())
    
Name  


# In[128]:


for i in title:
    Title.append(i.get_text())

    
Title


# In[129]:


for i in rating:
    Rating.append(i.get_text())
    
Rating


# In[130]:


Title


# In[131]:


for i in comments:
    Comments.append(i.get_text())
    
Comments


# In[132]:


# Create a dataframe using the given extracted files from the website.

df = pd.DataFrame({"Name":Name,"Title":Title,"Rating":Rating,"Comments":Comments})


# In[133]:


df


# In[139]:


df.to_csv("C:/Users/Prathmesh/OneDrive/Apple_16_Review")


# In[ ]:





# ## Extracting informations from all customers!

# In[159]:


Cust_Name=[]
Cust_Rating=[]
Cust_Title=[]
Cust_Comment=[]


# In[160]:


pages = 66

for i in range(1, pages + 1):
    url = 'https://www.flipkart.com/apple-iphone-16-teal-128-gb/product-reviews/itmce4bb3f55cc2f?pid=MOBH4DQFSY9ETDUU&lid=LSTMOBH4DQFSY9ETDUU6JV9DJ&sortOrder=MOST_HELPFUL&certifiedBuyer=false&aid=overall&page='+str(i)
    print(url)
    
    # HTTP get request
    response = requests.get(url)
    
    #
    soup = bs(response.content)
    
    #Extracting Customer Names:
    name = soup.find_all('p', class_ ="_2NsDsF AwS1CA" )
    for i in name:
        Cust_Name.append(i.get_text())
    
    #Extracting Customer Titles:
    title = soup.find_all('p', class_ = "z9E0IG")
    for i in title:
        Cust_Title.append(i.get_text())
    
    #Extracting Customer Rating:
    rating = soup.find_all('div', class_ = "XQDdHH Ga3i8K")
    for i in rating:
        Cust_Rating.append(i.get_text())
    
    #Extracting Customer Comments:
    comments = soup.find_all('div', class_ ="ZmyHeo" )
    for i in comments:
        Cust_Comment.append(i.get_text())
    


# In[161]:


print(len(Cust_Name))


# In[171]:


df1 = pd.DataFrame({"Name":pd.Series(Cust_Name),"Title":pd.Series(Cust_Title),"Rating":pd.Series(Cust_Rating),"Comments":pd.Series(Cust_Comment)})


# In[172]:


df1


# In[176]:


df1.to_csv("C:/Users/Prathmesh/OneDrive/Desktop/Iphone_16_review.csv", index=False)


# In[ ]:




