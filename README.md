# Data-Pipeline-To-Tableau
Soccer data scraped using selenium, processed in python and presented in Tableau.

This project presents a match up preview for upcoming soccer games in a Tableau dashboard. Link to the Tableau dashboard: https://public.tableau.com/app/profile/william.fitzhugh/viz/EuropeanSoccerMatchPreview/Dashboard5

The data is scraped from xscores.com using selenium in python, processed in python using pandas, and set to automatically update and export to a Google Sheets file. 

All together, this creates a customizable way to view information on upcoming soccer games.

## Some Explanation:
These scripts are designed to allow anyone to clone this repository and maintain a dataset of soccer scores for the past 20 years, just by runnning a signle script.

"Update Current Season Data" uses functions defined in "xscores_selenium_functions" to populate the file "Full_Dataset.csv" with up-to-date soccer results from Europe's top leagues, as well data 20 years of historical data.
