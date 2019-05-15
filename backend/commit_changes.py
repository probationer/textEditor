import sys
import json
import random
from models.commit_table import commit_insert, get_doc_data_by_commit_id
from models.document_table import get_doc_data_by_path, update_doc_status
from models.stage_table import exist_in_staging
from sqlite3 import Error

def commit_file(file_path, content):
    doc_id = get_doc_data_by_path(file_path)[0][0]
    if exist_in_staging(doc_id):
        data = dict()
        try : 
            data['doc_id'] = doc_id
            data['content'] = content
            data['user_id'] = '123456'
            commit_insert(data)
            print("File Commited")
        except Error as e:
            raise e
    else: 
        print("ADD_TO_STAGING")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    # if len(arguments) != 1:
    #     print("Should be exactly 2 arguments")
    # else:
    print()
    commit_file(file_path = arguments[0], content = arguments[1])

    #test
    # stage_file('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text1.txt',"22222")
