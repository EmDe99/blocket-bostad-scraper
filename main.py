from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import Listings

house_list = []
max_page_number = 0
current_page_number = 1
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)


def main():
    """"
    Main function to run the program
    """
    driver.get('https://bostad.blocket.se/p2/sv/find-home/?searchAreas=Visby')
    time.sleep(5)
    click_cookie_button()


def click_cookie_button():
    """"
    Function to click the cookie button on the website
    Switches to the iframe, waits for the button to be clickable and then clicks it.
    Switches back to the default content frame.
    """
    iframe_id = "sp_message_iframe_967837"
    driver.switch_to.frame(iframe_id)

    button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//button[@title="Accept all cookies" and @aria-label="Accept all cookies"]'))
    )
    button.click()

    driver.switch_to.default_content()
    highest_page_number()

    find_house_information()


def find_house_information():
    """"
    Function to find houses listings on the website
    """
    current_house = []
    house_container = driver.find_elements(By.CLASS_NAME, 'qds-1xk2oqv')
    for house in house_container:
        house_info = house.find_elements(By.CLASS_NAME, 'qds-ei5yx4')
        house_type = house_info[0].text
        rooms = house_info[1].text
        size = house_info[2].text
        current_house = house.find_element(By.CLASS_NAME, 'qds-y8cht8')
        price = current_house.text

        listing = Listings.Listings(house_type, rooms, size, price)
        print(listing.price)
        print(listing.house_type)
        print(listing.rooms)
        print(listing.size)
        house_list.append(listing)

    next_page()


def next_page():
    """"
    Function to go to the next page
    """
    global current_page_number
    global max_page_number
    next_page_button = driver.find_element(By.XPATH, '//a[@aria-label="Nästa"]') # Swedish for next
    current_page_number += 1
    next_page_button.click()

    time.sleep(5)

    if current_page_number > int(max_page_number):
        print("No more pages")
        return
    else:
        find_house_information()


def highest_page_number():
    """"
    Function to find the highest page number
    """
    global max_page_number
    pages = driver.find_elements(By.XPATH, "//a[@class='sc-gEvEer ifEzhZ qds-14qxs5p']")
    page_number = pages[-2]
    print("printing page number " + page_number.text)
    max_page_number = page_number.text


def save_to_dataframe():
    """"
    Function to save the data to a dataframe
    """
    house_dict_list = [vars(listing) for listing in house_list]
    df = pd.DataFrame(house_dict_list)
    df.to_csv('houses.csv', index=False)


main()
save_to_dataframe()

driver.quit()
