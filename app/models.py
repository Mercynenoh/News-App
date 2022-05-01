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
    def __init__(self, id,name,author,title,urlToImage,publishedAt,content):  
        self.id = id 
        self.name = name
        self.author = author
        self.title = title
        self.urlToImage =urlToImage
        self.publishedAt = publishedAt
        self.content = content
