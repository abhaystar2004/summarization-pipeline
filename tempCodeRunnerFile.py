
# # Fetch the latest data from the URL
# url = "https://ethresear.ch/latest.json"
# response = requests.get(url)
# latest_data = response.json()

# # Load the previously saved data from 'latest.json'
# try:
#     with open('latest.json', 'r') as f:
#         previous_data = json.load(f)
# except FileNotFoundError:
#     previous_data = {"topic_list": {"topics": []}}

# # Compare the two datasets to check for new blogs
# latest_topics = {topic["id"]: topic for topic in latest_data["topic_list"]["topics"]}
# previous_topics = {topic["id"]: topic for topic in previous_data["topic_list"]["topics"]}
# new_blogs = [topic for topic_id, topic in latest_topics.items() if topic_id not in previous_topics]
