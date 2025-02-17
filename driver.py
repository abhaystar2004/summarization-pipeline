from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver (replace 'chromedriver' with the path to your WebDriver)
driver = webdriver.Chrome()

try:
    # Open the webpage
    url = 'https://ethresear.ch/t/ahead-of-time-block-auctions-to-enable-execution-preconfirmations/21345'
    driver.get(url)

    # Allow time for JavaScript to load
    time.sleep(5)

    # Get the page source after rendering
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with the class 'cooked'
    cooked_elements = soup.find_all(class_='cooked')

    # Extract and print text from each 'cooked' element
    for element in cooked_elements:
        print(element.get_text(strip=True))

finally:
    # Close the WebDriver
    driver.quit()
