
### Objectives
YWBAT 
- explain one of the day to day tasks of a data engineer
- build a shell script that executes db writing
- write a pipeline to execute db writing
- apply oop to handle daily tasks

### Outcomes
- write a script to write data to a specific mongo collection in a specific database
- write an argument parser to parser command line arguments for shell scripting
- explain the importance of writing an argument parser
- explain the importance of writing a shell script


### Outline
- run demo of project
- discuss the shell script that runs the project
- discuss the argument parser
- review the files: `mongo_connector.py, twitter_connector.py, mongo_twitter_executor.py`
- add a function in the `mongo_connector.py or twitter_connector.py` files



### Why learn this?
You will almost definitely use this in your job. 

Using JN is awesome and fun...but they're not deployable. 


### Let's run a basic shell script! 

```
echo 'hello world!'
```

### Let's create and run a python script using our shell

1) first make a `.py` file and the a `.sh` file to run the `.py` file

How do we run a python file called file.py?

`python file.py`

### Questions/Comments?
- why the `#! /bin/bash` because this indicates a shell script

- nothing cool....I guess

### Now let's dive into the project! 

First let's look at 

`mongo_connector.py`


```python
from pymongo import MongoClient
```


```python
client = MongoClient(host='localhost', port=27017)
```


```python
client.list_database_names()
```




    ['admin',
     'config',
     'local',
     'marchmadness',
     'music_tweets',
     'mydb',
     'new_db',
     'text_for_lesson',
     'tweets']




```python
db_for_lesson = client["text_for_lesson"]
```


```python
db_for_lesson.list_collection_names()
```




    ['twitter_test_collection']




```python
coll_for_lesson = db_for_lesson["twitter_test_collection"]
```


```python
coll_for_lesson.count()
```

    /Users/rafael/anaconda3/envs/flatiron-env/lib/python3.6/site-packages/ipykernel_launcher.py:1: DeprecationWarning: count is deprecated. Use estimated_document_count or count_documents instead. Please note that $where must be replaced by $expr, $near must be replaced by $geoWithin with $center, and $nearSphere must be replaced by $geoWithin with $centerSphere
      """Entry point for launching an IPython kernel.





    72




```python
entries = list(coll_for_lesson.find({}))
entries[0]
```




    {'_id': ObjectId('5d64450bf01309eab84e2d04'),
     'created_at': 'Mon Aug 26 20:45:20 +0000 2019',
     'id': 1166089264188338176,
     'id_str': '1166089264188338176',
     'full_text': 'Old video still hot to this day #NewVideoAlert #Viral_SMS #hiphop #Monday  https://t.co/MPHXo72i2b',
     'truncated': False,
     'display_text_range': [0, 98],
     'entities': {'hashtags': [{'text': 'NewVideoAlert', 'indices': [32, 46]},
       {'text': 'Viral_SMS', 'indices': [47, 57]},
       {'text': 'hiphop', 'indices': [58, 65]},
       {'text': 'Monday', 'indices': [66, 73]}],
      'symbols': [],
      'user_mentions': [],
      'urls': [{'url': 'https://t.co/MPHXo72i2b',
        'expanded_url': 'https://youtu.be/9jtsnzHicow',
        'display_url': 'youtu.be/9jtsnzHicow',
        'indices': [75, 98]}]},
     'metadata': {'iso_language_code': 'en', 'result_type': 'recent'},
     'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
     'in_reply_to_status_id': None,
     'in_reply_to_status_id_str': None,
     'in_reply_to_user_id': None,
     'in_reply_to_user_id_str': None,
     'in_reply_to_screen_name': None,
     'user': {'id': 2821278987,
      'id_str': '2821278987',
      'name': 'MONEYIGOTEM',
      'screen_name': 'moneyigotem',
      'location': 'worldwide',
      'description': 'For Bookings, Features & Press: Contact: musicmoneymgt@gmail.com',
      'url': 'https://t.co/cq5B2vaOtl',
      'entities': {'url': {'urls': [{'url': 'https://t.co/cq5B2vaOtl',
          'expanded_url': 'https://soundcloud.com/moneyigotem',
          'display_url': 'soundcloud.com/moneyigotem',
          'indices': [0, 23]}]},
       'description': {'urls': []}},
      'protected': False,
      'followers_count': 365,
      'friends_count': 43,
      'listed_count': 1,
      'created_at': 'Fri Oct 10 16:12:18 +0000 2014',
      'favourites_count': 22,
      'utc_offset': None,
      'time_zone': None,
      'geo_enabled': False,
      'verified': False,
      'statuses_count': 80,
      'lang': None,
      'contributors_enabled': False,
      'is_translator': False,
      'is_translation_enabled': False,
      'profile_background_color': '131516',
      'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme14/bg.gif',
      'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme14/bg.gif',
      'profile_background_tile': True,
      'profile_image_url': 'http://pbs.twimg.com/profile_images/815972486907133952/QaW73uBx_normal.jpg',
      'profile_image_url_https': 'https://pbs.twimg.com/profile_images/815972486907133952/QaW73uBx_normal.jpg',
      'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2821278987/1483378051',
      'profile_link_color': 'ABB8C2',
      'profile_sidebar_border_color': '000000',
      'profile_sidebar_fill_color': 'DDEEF6',
      'profile_text_color': '333333',
      'profile_use_background_image': True,
      'has_extended_profile': False,
      'default_profile': False,
      'default_profile_image': False,
      'following': None,
      'follow_request_sent': None,
      'notifications': None,
      'translator_type': 'none'},
     'geo': None,
     'coordinates': None,
     'place': None,
     'contributors': None,
     'is_quote_status': False,
     'retweet_count': 0,
     'favorite_count': 0,
     'favorited': False,
     'retweeted': False,
     'possibly_sensitive': False,
     'lang': 'en'}




```python
db_for_lesson.list_collection_names()
```




    ['twitter_test_collection', 'new_collection']




```python
list(db_for_lesson['new_collection'].find({}))
```




    [{'_id': ObjectId('5d67fd92c7f6d2b06283fa5c'),
      'name': 'Juan Sanchez',
      'age': '32'}]



### After looking at the `mongo_connector.py` file, what have we learned?

- specify database in `__init__` method
- the purpose of `if __name__=="__main__":`
- moving from jupyter to scripting
- how to create your own `verbose` parameter

### let's review Tweepy


```python
import tweepy as tw
import json
```


```python
with open("your_file_perms_here") as f:
    d = json.load(f)
print(d.keys())
```


    ---------------------------------------------------------------

    FileNotFoundError             Traceback (most recent call last)

    <ipython-input-51-f5dc971f9e54> in <module>
    ----> 1 with open("your_file_perms_here") as f:
          2     d = json.load(f)
          3 print(d.keys())


    FileNotFoundError: [Errno 2] No such file or directory: 'your_file_perms_here'



```python
auth = tw.OAuthHandler(consumer_key=d["consumer_key"], consumer_secret=d["consumer_secret"])
```


```python
api = tw.API(auth_handler=auth)
```

### what did we learn from this?
- Trust noone with your permissions
- `with` closes the file at the end of the operation

### let's put these together

### The next step would be to automate this using autosys or crontab
