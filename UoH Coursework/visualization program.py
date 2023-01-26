#!/usr/bin/env python
# coding: utf-8

# In[1]:


# funtions using here for visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# In[22]:


# importing a csv file from the desktop
# https://www.kaggle.com/marcvelmer/barcelona-2017accidents open source file link attached
accidents = pd.read_csv ("C:/Users/Naseer/Desktop/accidents_2017.csv")
accidents


# In[3]:


accidents.info()


# In[23]:


# data source consists of 10339 rows and 15 columns
# using head viewing fist 5
accidents.head ()


# In[5]:


# indentifying the columns available
accidents.columns


# In[ ]:





# In[ ]:





# In[25]:


# no null values.
accidents.isnull().sum().any()


# replacing Unknown with n.a
accidents.replace ('Unknown', np.nan, inplace = True)

# null values are present now
accidents.isnull(). sum() .any()
# True

# info method can be used to access null value
accidents.info ()


# In[36]:



#Change upper case letters to lower-case letters and spaces with underscores.
accidents.rename ( 
    columns = lambda x:x.replace(' ','_').
    lower(),
    inplace = True)

# adding column for year 2017
accidents ['year'] = np.repeat
(
    2017,
    accidents.shape
    [0]
)
accidents.head ()


# New column nameaccidents.columns
# Index (['id', 'street', 'weekday', 'month', 'day', 'hour', 'mild_injuries','serious_injuries', 'victims', 'vehicles_involved', 'longitude','latitude'],dtype='object')


# In[38]:



# month names
list (
    accidents. month. unique()
)
# ['October','September','December','July','May','June','January','April','March','November','February','August']

# names of the month to int
month_to_int = {
    'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12
}
# Converting month names into there respective numbers
accidents ['month'].replace(
    month_to_int,
    inplace = 
    True )

# Obtain new month names with numbers
list (
    accidents.month.unique()
)
# [10, 9, 12, 7, 5, 6, 1, 4, 3, 11, 2, 8]


# In[9]:


# To create a single datetime column, combine month, day, and year columns.
accidents['date'] = pd.to_datetime(
    accidents[[
        'year', 'month', 'day', 'hour'
    ]])

# Observe the first 5 columns.
accidents.head()


# In[10]:


# Drop columns for hour, day, month, year and weekday
accidents.drop (
    ['hour','day','month','year','weekday'],
    axis=1,
    inplace = True
)

# Dataset columns
list (
    accidents.columns
)
# ['id','street','mild_injuries','serious_injuries','victims','vehicles_involved','longitude','latitude','date']


# In[11]:


#Make sure the dataset does not contain duplicate rows.
accidents.duplicated(). sum()

# Print the duplicated rows.
accidents [accidents.duplicated()
          ]


# In[ ]:





# In[12]:


# Following up removing duplicated columns
accidents.shape
# (10339, 12)

# Drop duplicates.
accidents.drop_duplicates(
    inplace = 
    True
)

# Following the removal of duplicate columns.
accidents.shape


# In[13]:


import calendar
#accident per month
month_accidents_name = 
accidents.groupby(
    accidents['date']
    .dt.month.count().date

# Replace the month integers by month names.
month_accidents_name.index = 
    [calendar.month_name [x]
     for x in range (
         1,13
     )]

month_accidents_name


# In[ ]:





# In[33]:


#method used refering https://www.youtube.com/watch?v=VFsRLjSc8GA&list=PLu0W_9lII9agK8pojo23OHiNz3Jm6VQCH&index=14
#Visualing the number of accidents happended in a month
plt.style.use (
    'ggplot' )

# plotting accidents per month
month_accidents_name.plot (kind = 'bar',
    figsize = ( 12 , 7),
    color = 'orange', 
    alpha = 0.5)

# title and x,y labels including there font sizes
plt.title ('Barcelona Accidents 2017', 
    fontsize = 21 
)
plt.xlabel ('Month',
    fontsize = 15
)
plt.ylabel ('Accidents Count',
    fontsize = 15
     )
plt.show ()


# In[15]:


dates_accidents = accidents.groupby(
    accidents['date'
             ].dt.date).count().date

dates_accidents.plot(
    figsize = ( 18, 14 ),
    color = 'green'
)

# accidents on sundays
sunday = accidents.groupby ( 
    accidents [accidents['date'].dt.
               dayofweek == 6]
    .date.dt.date
).count().date
plt.scatter (sunday.index,
    sunday,
    color='red',
    label='Sunday'
)

# accidents on fridays
friday = accidents.groupby (accidents [accidents['day'].dt.dayofweek==4]
    .date.dt.date
).count().date
plt.scatter ( 
    friday.index,
    friday, 
    color = 'blue',
    label = 'Friday'
)

# Title, x label and y label
plt.xlabel (
    'Dates of Accidents',
    fontsize = 18
)
plt.title (
    'Barcelona Accidents 2017',
    fontsize = 20
)
plt.ylabel (
    'Per Day Accidents',
    fontsize = 18
)
plt.legend ()


# In[ ]:





# In[16]:


#used anaconda powershell to install folium
#pip 
import folium
# Created a map of Barcelona
#using latitude and longitude for serious injuries points
map_barcelona =
folium.Map(
    location = [
        41.38879, 
        2.15899],
    zoom_start = 
    11.5
)

# Display only accidents where serious injuries happended
for lat, lng, label in zip ( accidents.latitude, accidents.longitude, accidents.serious_injuries.astype(str) ):
    if label!='0':
        folium.features.CircleMarker(
            [lat, lng],
            radius=4,
            color='yellow',
            fill=True,
            popup=label,
            fill_color='green',
            fill_opacity=0.7
        ).add_to(map_barcelona)
    
# Viewing map
map_barcelona


# In[17]:


# Number of accident per day of the week
accidents_weekday = 
accidents.groupby(
    accidents[
        'date'
    ].dt.dayofweek
).count().date

# Replace the day integers by day names.
accidents_weekday.index = [
    calendar.day_name[x]
    for x in range ( 0, 7 ) ]

# plot accidents per day
accidents_weekday.plot (
    kind = 'bar',
    figsize = ( 10, 7 ),
    color = 
    'purple',
    alpha = 
    0.5)

# title and x,y labels
plt.title (
    'Barcelona Accidents 2017',
    fontsize = 21 )
plt.xlabel ( 'Weekday', fontsize = 18 )
plt.ylabel ('No. of accidents', fontsize = 18 );


# In[18]:


# Serie with number of mild injuries and serious injuries
victim_injuries =
accidents [['mild_injuries',
            'serious_injuries'] ].sum()

# Pie plot with the percentage of victims with mild and serious injuries
victim_injuries.plot(
    kind = 'pie',
    figsize = ( 9, 79),
    colors = ['red','white'],
    labels = None,
    autopct ='%1.1f%%', 
    fontsize = 18
)

# Legend and title
plt.legend ( labels = [ 'Mild Injuries', 'Serious Injuries' ] )
plt.title (
    'Barcelona Serious/Mild Injuries 2017',
    fontsize = 18
)
plt.ylabel (' ')


# In[ ]:





# In[ ]:





# In[19]:


#scatter plot
from matplotlib import pyplot as plt
plt.scatter ( accidents [
    'part_of_the_day' ] ,
             accidents[ 'victims' ]
)
plt.xlabel( 
    "Part of the day" 
)
plt.ylabel(
    "Victims involved in Accidents" 
)
plt.show()


# In[ ]:




