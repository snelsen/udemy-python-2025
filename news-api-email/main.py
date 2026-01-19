import requests

api_key = "f5e9fc8a3fc243929738e3d8e2380b3c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-19&sortBy=publishedAt&apiKey=f5e9fc8a3fc243929738e3d8e2380b3c"

request = requests.get(url)

# extract the response
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print('\n')
