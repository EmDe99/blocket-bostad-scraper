# Blocket Bostad Scraper

A tool to scrape data such as rent, amount of rooms, type and size from blocket bostad and save it to a .csv file. Now using the "hidden" blocket api instead of scraping from the front-end. 

## Built with

- Python
- Pandas
- Requests

## To Run

Install the required dependencies using the following command: 
```
pip install -r requirements.txt
```
Now just run main.py to start scraping!

## Location to Scrape

As of now the main.py file scrapes data from everything on blocket bostad regardless of location. 
To change this we can modify the payload:
```
"areaIdentifier": [],
```

To (if you want to scrape only from the Stockholm area):

```
"areaIdentifier": ["se/stockholm"]
```
