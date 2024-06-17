from django.shortcuts import render
import requests
from newsapi import NewsApiClient

# change your news api key
def index(request):
    api_key = 'your key'
    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(
        language='en',
        country='in'  # change to get specific country news   
    )
    
    limited_articles = top_headlines['articles'][:9] # change the number of news displayed at one time
    articles = []
    for article in limited_articles:
        # Check for image URL presence before including it
        if article['urlToImage'] is not None:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'image_url': article['urlToImage'],
            })

    context = {'articles': articles}
    return render(request, 'main/index.html', context)

def news_filter_page(request):
  keyword = request.GET.get('keyword')
  articles = []

  if keyword:
   # Replace 'YOUR_NEWS_API_KEY' with your actual API key
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey=your key"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    if data['status'] == 'ok':
      articles = data['articles'][:12]  # Limit to first 12 articles
    else:
      print(f"Error retrieving news: {data['status']}")
  else:
        pass

  processed_articles = [
        {'title': article['title'],
         'description': article['description'],
         'url': article['url'],
         'image_url': article.get('urlToImage')}  
        for article in articles
    ]

  context = {'articles': processed_articles}
  return render(request, 'newsapp/news_filter.html', context)
