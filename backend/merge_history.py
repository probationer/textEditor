import sys
import json
import random
from models.commit_table import commit_insert, get_doc_data_by_commit_id, get_last_commit_id
from models.document_table import get_doc_data_by_path, update_doc_status
from models.stage_table import exist_in_staging
from models.version_table import version_insert, get_all_rows
from sqlite3 import Error
import datetime

def merge_history(file_path):
    doc_id = get_doc_data_by_path(file_path)[0][0]
    file_name = get_doc_data_by_path(file_path)[0][2]
    rows = get_all_rows(doc_id)
    for row in rows:
        print('Sandeep')
        print(file_name)
        print(row[4])

if __name__ == "__main__":
    arguments = sys.argv[1:]
    # if len(arguments) != 1:
    #     print("Should be exactly 2 arguments")
    # else:
    merge_history(file_path = arguments[0])
    #test
    # stage_file('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text1.txt',"22222")
