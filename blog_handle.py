import json


with open('blogs.json', 'r') as f:
    data = json.load(f)

print(data[2])