import requests
import json

class NewsData(object):

    def __init__(self):
        self.api_key = "d0961344e16546a88bb499872b9808b5"
        self.top_stories = ""

    def getTopStories(self):
        url = ('http://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey='+self.api_key)
        response = requests.get(url)
        jsonData = json.loads(str(response.text))
        self.top_stories = self.parseStories(jsonData)

    def parseStories(self,jsonData):
        topStories = ""
        for i in range(0,len(jsonData['articles'])):
            topStories = topStories + str(jsonData['articles'][i]['title'])+"\n\n"
        return topStories     


