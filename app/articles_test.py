import unittest
from models import Articles

News = news.News
class ArticlesTest(unittest.Testcase)

def setUp(self):
    self.new_articles = Articles("business-insider", "Business Insider","as it is today", "https://i.insider.com/626e4d040983640018c098c7?width=1200&format=jpeg", "2022-04-22T20:02:17Z", "A Texan lawmaker has told")

def test_instance(self):
    self.assertTrue(isInstance(self.new_articles, Articles))

if __name__ == '__main__'
unittest(main)