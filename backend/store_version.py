import sys
import json
import random
from models.commit_table import commit_insert, get_doc_data_by_commit_id, get_last_commit_id
from models.document_table import get_doc_data_by_path, update_doc_status
from models.stage_table import exist_in_staging
from models.version_table import version_insert, get_all_rows
from sqlite3 import Error
import datetime

def create_version(file_path):
    doc_id = get_doc_data_by_path(file_path)[0][0]
    commit_id =  get_last_commit_id(doc_id)
    if commit_id:
        data = dict()
        try : 
            data['doc_id'] = doc_id
            data['user_id'] = '123456'
            data['commit_id'] = commit_id
            version_insert(data)
            print('Sandeep')
            print(str(datetime.datetime.now()))
            print('File Merged')
        except Error as e:
            print("ERROR WHILE MERGE : " + commit_id)
    else: 
        print('Please Commit Before Merge')


if __name__ == "__main__":
    arguments = sys.argv[1:]
    # if len(arguments) != 1:
    #     print("Should be exactly 2 arguments")
    # else:
    create_version(file_path = arguments[0])
    #test
    # stage_file('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text1.txt',"22222")
