class News:

    def __init__(self, id,name,description, image, category, language, country):
        self.id = id
        self.name = name
        self.description= description
        self.image = image
        self.category= category
        self.language = language
        self.country= country
        

class Articles:
    def __init__(self, id,name,author,url,title,urlToImage,publishedAt,content,football):  
        self.id = id 
        self.name = name
        self.author = author
        self.title = title
        self.urlToImage =urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.football= football
