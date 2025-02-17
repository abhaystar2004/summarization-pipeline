from requests_html import HTMLSession

# Create an HTML session
session = HTMLSession()

# Define the URL
url = 'https://ethresear.ch/t/ahead-of-time-block-auctions-to-enable-execution-preconfirmations/21345'

# Send a GET request to the URL
response = session.get(url)

# Render the JavaScript
response.html.render(sleep=5)

# Find all elements with the class 'cooked'
cooked_elements = response.html.find('.cooked')

# Extract and print text from each 'cooked' element
for element in cooked_elements:
    print(element.text)