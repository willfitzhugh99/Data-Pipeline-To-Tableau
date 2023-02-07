#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[2]:


from ipynb.fs.full.scrape_xscores_completed_function import scrape_xscores_completed
from ipynb.fs.full.scrape_xscores_upcoming_function import scrape_xscores_upcoming_fixtures


# ---

# ### This script is designed to scrape xscores.com for results from the current soccer season in Europe's top leagues, and compile with results from past season, then export the data to an excel file.

# In[3]:


#Leagues and countries of interest:

league_names = pd.DataFrame({
    'country':['spain', 'england','germany','france','italy'],
    'league_name':['primera-division','premier-league','bundesliga','ligue-1','serie-a']
})
cup_names = pd.DataFrame({
    'country':['europe-uefa','europe-uefa','spain','england','germany','france', 'italy'],
    'league_name':['uefa-champions-league','uefa-europa-league','fa-cup','fa-cup','fa-cup','fa-cup','fa-cup']
})
leagues_cups = pd.concat([league_names,cup_names])
leagues_cups


# In[4]:


#scrape completed and upcoming games for each league, compile into current season data

year = 2022   #select year of ongoing season (currently the 2022-2023 season)

data = pd.DataFrame(columns=['Round', 'Date', 'Time', 'Home_Team', 'Home_Score', 'Away_Score', 'Away_Team',
                                'Home_Score_AET', 'Away_Score_AET', 'Home_Penalties', 'Away_Penalties',
                                'Home_Points', 'Away_Points','season', 'Country', 'Competition'])

for i in range(len(leagues_cups)):
    
    completed = scrape_xscores_completed(year, leagues_cups.iloc[i,0], leagues_cups.iloc[i,1])
    upcoming = scrape_xscores_upcoming_fixtures(leagues_cups.iloc[i,0], leagues_cups.iloc[i,1])
    
    current_season = pd.concat( [completed, upcoming] )
    current_season['season'] = year
    current_season['Country'] = leagues_cups.iloc[i,0]       #add country and competition indicator columns
    current_season['Competition'] = leagues_cups.iloc[i,1]
    
    data = pd.concat([data, current_season])


# In[ ]:


#Compile current season data with data from past 20 years, and transform to work with in Tableau.

past_seasons = pd.read_csv('/Users/willfitzhugh/Desktop/Coding/Tableau Game Preview/Past_20years_Data.csv')

raw_data = pd.concat([past_seasons, data])
    
home = raw_data.rename(columns = {
        'Home_Team':'Team',
        'Away_Team':'Opponent',
        'Home_Score':'Team_Score',
        'Away_Score':'Opponent_Score',
        'Home_Points':'Team_Points',
        'Away_Points':'Opponent_Points'
})
home['Location'] = 'Home'
    
away = raw_data.rename(columns = {
        'Away_Team':'Team',
        'Home_Team':'Opponent',
        'Away_Score':'Team_Score',
        'Home_Score':'Opponent_Score',
        'Away_Points':'Team_Points',
        'Home_Points':'Opponent_Points'
})
away['Location'] = 'Away'

full_dataset = pd.concat([home, away])
    
full_dataset.to_csv('Full_Dataset.csv',index=False)


# In[6]:


#export updated data to google sheets via pygsheets

#this part requires the path relative to the home directory for Full_Dataset.csv and the google sheets API 
#authentication file. 
path = ''

import pygsheets

# google sheets authentication
creds = path + 'Tableau Game Preview/pygsheets_api_authorization_file.json'
api = pygsheets.authorize(service_file=creds)

# open the sheet by name (my sheet name is Soccer Data)
sheet = api.open('Soccer Data').sheet1

#read data
data = pd.read_csv( path + 'Tableau Game Preview/Full_Dataset.csv')

#set dataframe
sheet.set_dataframe(data, (1,1), fit=True)
