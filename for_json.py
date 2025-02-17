import requests
import json
from bs4 import BeautifulSoup

# for the summarization
# from transformers import pipeline

# fucntion for getting the urls from the json file
def urls():
    try:
        with open('latest.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return "No data found."

    urls = []
    for topic in data["topic_list"]["topics"]:
        custom_url = f"https://ethresear.ch/t/{topic['slug']}/{topic['id']}"
        urls.append(custom_url)

    return urls

# Function for getting the new blog URLs
def get_urls(new_posts=False, update_json=False):
    if not new_posts:
        return urls()
    
    url = "https://ethresear.ch/latest.json"
    response = requests.get(url)
    latest_data = response.json()

    try:
        with open('latest.json', 'r') as f:
            previous_data = json.load(f)
    except FileNotFoundError:
        previous_data = {"topic_list": {"topics": []}}

    latest_topics = {topic["id"]: topic for topic in latest_data["topic_list"]["topics"]}
    previous_topics = {topic["id"]: topic for topic in previous_data["topic_list"]["topics"]}
    new_blogs = [topic for topic_id, topic in latest_topics.items() if topic_id not in previous_topics]

    new_urls = []
    if new_blogs:
        for blog in new_blogs:
            custom_url = f"https://ethresear.ch/t/{blog['slug']}/{blog['id']}"
            new_urls.append(custom_url)
    
    if update_json:
        with open('latest.json', 'w') as f:
            json.dump(latest_data, f)
    
    return new_urls

# Function for getting the content of the blog
def get_content(urls):
    content = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        article = soup.find("div", {"class": "post"}).get_text()
        content.append(article)
    return content

# function for getting the article
def get_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    article = soup.find("div", {"class": "post"}).get_text()
    return article

# function for summarizing the article

def tokenize(text, max_chunk=500):
    text = text.replace('.\n', '.<eos>')
    text = text.replace('?', '?<eos>')
    text = text.replace('!', '!<eos>')
    max_chunk = 500
    sentences = text.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    return chunks

def summarize(article):
    summarizer = pipeline("summarization")
    chunks = tokenize(article)
    res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)
    text = ' '.join([summ['summary_text'] for summ in res])
    return text

# summarize for list of articles
def summarize_list(articles):
    summaries = []
    for article in articles:
        summaries.append(summarize(article))
    return summaries



urls = get_urls(new_posts=True)
print(urls)
# article = get_article(urls[1])
# print(article)
