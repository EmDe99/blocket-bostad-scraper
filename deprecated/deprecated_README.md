# Blocket Bostad Scraper

A tool to scrape data in the form of rent, amount of rooms, type and size from blocket bostad and save it to a .csv file. 

### Built with

- Python
- Selenium
- Pandas

### To Run

Install the required dependencies using the following command: 
```
pip install -r requirements.txt
```
If needed modify the webdriver to point towards your chromedriver. 

Next modify the url to match the area you want to scrape from. The following is an example to scrape from the Stockholm Area:
```
driver.get('https://bostad.blocket.se/p2/sv/find-home/?searchAreas=Stockholm')
```
Now you are ready to scrape!
