# Data-Pipeline-To-Tableau
Soccer data scraped using selenium, processed in python and presented in Tableau.

This project presents a match up preview for upcoming soccer games in in a Tableau dashboard. The data is scraped from xscores.com using selenium in python, processed in python using pandas, and set to automatically update and export to a Google Sheets file.
The dashboard on Tableau Public uses this Google Sheets file as a data source and is set to automatically update with the file. Using cron or Windows Task Scheduler, the 'Update Current Season Data.py' file can be run automatically and maintain the Google Sheets file with up-to-date match results.

All together, this creates a customizable way to view information on upcoming soccer games.

Here is the link to the Tableau dashboard:
https://public.tableau.com/app/profile/william.fitzhugh/viz/EuropeanSoccerMatchPreview/Dashboard5

soon to come: explanations things like, the .py version of the Update Current Season script is there so you can run the script from your terminal using an task automator and keep the data source maintained automatically.
