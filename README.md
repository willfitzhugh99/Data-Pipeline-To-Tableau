# Data-Pipeline-To-Tableau
Soccer data scraped using selenium, processed in python and presented in Tableau.

This project presents a match up preview for upcoming soccer games in a Tableau dashboard. Link to the Tableau dashboard: https://public.tableau.com/app/profile/william.fitzhugh/viz/EuropeanSoccerMatchPreview/Dashboard5

The data is scraped from xscores.com using selenium in python, processed in python using pandas, and set to automatically update and export to Tableau. 

All together, this creates a customizable way to view information on upcoming soccer games.

---
### Some Explanation:
These scripts are designed to allow anyone to clone this repository and maintain a dataset of soccer scores for the past 20+ years, just by runnning a single script.

"Update Current Season Data.ipynb" uses functions defined in "xscores_selenium_functions.ipynb" to populate "Full_Dataset.csv" with up-to-date soccer results from Europe's top leagues, as well as 20 years of historical data.

"Update Current Season Data.py" exists to be run on a task manager, like crontab. This way the script can be set to run automatically and maintain "Full_Dataset.csv". Once the file has been updated, the last cell of "Update Current Season Data.py" connects to the Google Sheets API and exports "Full_Dataset.csv" to a Google Sheets worksheet, which is used as the data source for the previously mentioned Tableau dashboard.

---
#### Necessary Alterations:
To successfully run this program on your computer, you just have to open each of the .ipynb files and enter the path to the clone of this repository and the path to your chromedriver (you also need a chromedriver). 

See requirements.txt for package versions
