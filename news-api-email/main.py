import requests
from send_email import send_email

api_key = "f5e9fc8a3fc243929738e3d8e2380b3c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-19&sortBy=publishedAt&apiKey=f5e9fc8a3fc243929738e3d8e2380b3c"

request = requests.get(url)

# extract the response
content = request.json()

# Access the article titles and description
message = ""
for article in content["articles"]:
    message = message + article["title"] + "\n"
    if article["description"] is not None:
        message = message + article['description'] + "\n"
    message = message + "\n"

message = message.encode("utf-8")
send_email(message=message)