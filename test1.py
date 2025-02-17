import requests
from bs4 import BeautifulSoup

# URL of the article
url = "https://ethresear.ch/t/ahead-of-time-block-auctions-to-enable-execution-preconfirmations/21345"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the main content of the article
article = soup.find("div", {"class": "post"}).get_text()