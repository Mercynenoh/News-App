from app import app
import urllib.request,json
from .models import News
from .models import Articles

api_key = app.config['NEWS_API_KEY']
article_url = app.config['ARTICLES_API_BASE_URL']
base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_result = None
        
        if get_sources_response['sources']:
            sources_result_list = get_sources_response['sources']
            sources_result = process_results(sources_result_list)
    return sources_result
def process_results(sources_list):
   
    sources_result = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        image = source_item.get('url')
        category= source_item.get('category')
        language = source_item.get ('language')
        country = source_item.get('country')
        
        
        if image:
           sources_object =News(id,name, description, image, category, language, country)
           sources_result.append(sources_object)   

    return sources_result

def get_articles(category):
    get_articles_url = article_url.format(category,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        print(get_articles_response)
        articles_results = None
        if get_articles_response ['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = article_results (articles_results_list)
    return articles_results

def article_results(article_list):
   
    articles_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        url = article_item.get('url')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        publishedAt= article_item.get('publishedAt')
        content= article_item.get ('content')
        
        
        
        if urlToImage:
           articles_object =Articles(id,name,author,title, url, urlToImage, publishedAt,content)
           articles_results.append(articles_object)   

    return articles_results

