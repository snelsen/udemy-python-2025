import requests
from send_email import send_email

api_key = "f5e9fc8a3fc243929738e3d8e2380b3c"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2025-12-19" \
      "&sortBy=publishedAt" \
      "&apiKey=f5e9fc8a3fc243929738e3d8e2380b3c" \
      "&language=en"

request = requests.get(url)

# extract the response
content = request.json()

# Access the article titles and description
message = "Subject: Today's News\n"
for article in content["articles"][:20]:
    message = message + article["title"] + "\n"
    if article["description"] is not None:
        message = message + article['description'] + "\n"
    if article["url"] is not None:
        message = message + article["url"] + "\n"
    message = message + "\n"

message = message.encode("utf-8")
send_email(message=message)