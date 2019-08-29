import json
import tweepy as tw


class MyTwitterConnector():

    
    def __init__(self, permissions_file_path=""):
        self.api = self._connect_to_twitter(permissions_file_path=permissions_file_path)

    
    def _connect_to_twitter(self, permissions_file_path):
        with open(permissions_file_path) as f:
            d = json.load(f)
        
        auth = tw.OAuthHandler(consumer_key=d["consumer_key"], consumer_secret=d["consumer_secret"])

        api = tw.API(auth_handler=auth)
        return api

    
    def search_twitter(self, search_query=None):
        if search_query == None:
            print("Please enter search query and try again")
            return None

        res = self.api.search(search_query, tweet_mode='extended')
        return list(res)

if __name__=="__main__":
    connector = MyTwitterConnector(permissions_file_path="/Users/rafael/.ssh/twitter_app00.json")

    connector.search_twitter(search_query="python")