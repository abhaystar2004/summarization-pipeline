import bs4 as bs
import requests

def extract_text_by_id(html, element_id):
    soup = bs.BeautifulSoup(html, 'html.parser')
    element = soup.find(id=element_id)
    
    if element:
        return element.get_text()
    else:
        return f"No element with id '{element_id}' found."

url = 'https://ethresear.ch/t/based-rollups-superpowers-from-l1-sequencing/15016'
html = requests.get(url).text

ex = extract_text_by_id(html ,'post_1')
