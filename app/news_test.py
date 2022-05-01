import unittest
from models import News

News = news.News
class NewsTest(unittest.Testcase)

def setUp(self):
    self.new_news = News('Tesla will finally start selling the Cybertruck', "https://s.yimg.com/os/creatr-uploaded-images/2022-03/733d9be0-b2cd-11ec-b7f9-382caaedc1ae", "2022-04-22T20:02:17Z")

def test_instance(self):
    self.assertTrue(isInstance(self.new_news, News))

if __name__ == '__main__'
unittest(main)