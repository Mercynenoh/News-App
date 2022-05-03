import unittest
from models import News

News = news.News
class NewsTest(unittest.Testcase)

def setUp(self):
    self.new_news = News('abc-news','ABC News','Your trusted source for breaking news','https://abcnews.go.com','general','en','us')

def test_instance(self):
    self.assertTrue(isInstance(self.new_news, News))

if __name__ == '__main__'
unittest(main)

