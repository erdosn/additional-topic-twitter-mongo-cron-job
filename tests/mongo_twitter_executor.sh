#!/bin/bash
echo "running test for mongo_twitter_exececutor.py"
cd ..
pwd 
python mongo_twitter_executor.py -collection_name "twitter_test_collection" -perms_file_path "/your/path/to/file.json" 
cd tests
echo "finished!"