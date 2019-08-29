import json
import argparse 

from mongo_connector import MyMongoConnector
from twitter_connector import MyTwitterConnector


parser = argparse.ArgumentParser()

parser.add_argument('-collection_name', 
                    type=str, 
                    default=None, 
                    help="name of table for mongo to write into")

parser.add_argument('-perms_file_path',
                    type=str,
                    default=None,
                    help="filepath of twitter permissions json file")




def main():
    parser_variables = vars(parser.parse_args())
    collection_name = parser_variables["collection_name"]
    perms_file_path = parser_variables["perms_file_path"]

    try:
        # Instantiate my MongoConnector
        mongo_connector = MyMongoConnector()
    except Exception as e:
        print('failed at mongo connection')
        print(e)
        exit(1)
    
    try:
        # Instatiate my TwitterConnector
        twitter_connector = MyTwitterConnector(permissions_file_path=perms_file_path)
    except Exception as e:
        print(e)
        exit(1)
    
    print('connected to both mongo and twitter now')

    # Query twitter for #monday and get the results
    search_query = "#monday"
    res = twitter_connector.search_twitter(search_query=search_query)
    

    # insert res into your database/collection
    for r in res:
        data = r._json
        mongo_connector.insert_data_into_collection(collection_name=collection_name, 
                                                    data=data, 
                                                    verbose=True)

    print('finished!')

if __name__=="__main__":
    main()
