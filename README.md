# Blocket Bostad Scraper

A tool to scrape data such as rent, amount of rooms, type and size from blocket bostad and save it to a .csv file. Now using the "hidden" blocket api instead of scraping from the front-end. 

## Disclaimer

This is a scraper project specifically designed for Blocket.se. Scraping Blocket.se or other websites might violate their terms and conditions, which you agree to as a user. It is your responsibility to review and comply with these terms. The availability of this tool does not guarantee your right to use it, and usage may result in legal consequences. This project is provided "as is," and the author(s) make no warranties regarding its functionality, accuracy, or legality.

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

To (if you want to, for example, only scrape from the Stockholm area):

```
"areaIdentifier": ["se/stockholm"]
```
