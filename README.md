# Summarization Pipeline

This project provides a pipeline to fetch the latest blog posts from `ethresear.ch`, extract their content, and summarize the articles. It uses the `requests` library to fetch data, `BeautifulSoup` for parsing HTML content, and `transformers` for summarization.

## Requirements

To run this project, you need the following Python libraries:

- `requests`
- `json`
- `beautifulsoup4`
- `transformers`

You can install these dependencies using `pip`:

```bash
pip install requests beautifulsoup4 transformers
```

## Usage

### Get URLs from JSON File

The `urls` function reads the URLs from a JSON file (`latest.json`) and constructs the complete URLs.

```python
def urls():
    # Implementation here
```

### Get New Blog URLs

The `get_urls` function fetches the latest blog URLs from `ethresear.ch`. If `new_posts` is `True`, it retrieves new blog URLs and updates the JSON file if `update_json` is `True`.

```python
def get_urls(new_posts=False, update_json=False):
    # Implementation here
```

### Get Blog Content

The `get_content` function fetches the content of the blogs given a list of URLs.

```python
def get_content(urls):
    # Implementation here
```

### Get Single Article

The `get_article` function fetches the content of a single blog post given its URL.

```python
def get_article(url):
    # Implementation here
```

### Tokenize Text

The `tokenize` function splits the text into chunks for summarization.

```python
def tokenize(text, max_chunk=500):
    # Implementation here
```

### Summarize Article

The `summarize` function summarizes a given article using the `transformers` library.

```python
def summarize(article):
    # Implementation here
```

### Summarize List of Articles

The `summarize_list` function summarizes a list of articles.

```python
def summarize_list(articles):
    # Implementation here
```

### Example Usage

To fetch the latest blog URLs and print them:

```python
urls = get_urls(new_posts=True)
print(urls)
```

## Notes

- Make sure to have the `latest.json` file in the same directory as your script.
- The `transformers` library is optional and used for summarization. Uncomment the relevant lines if you want to use summarization.

---

Feel free to customize the `README.md` file as needed! If you have any more questions or need further assistance, let me know.
