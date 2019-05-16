import sys
import json
import random
from models.stage_table import staging_create_or_update
from models.document_table import get_doc_data_by_path, update_doc_status

def stage_file(file_path, content):
    doc_id = get_doc_data_by_path(file_path)[0][0]
    data = dict()
    if doc_id:
        data['doc_id'] = doc_id
        data['content'] = content
        staging_create_or_update(data)
        print("Changed Staged")
    else:
        raise 'File Not Saved Properly'

if __name__ == "__main__":
    arguments = sys.argv[1:]
    # if len(arguments) != 1:
    #     print("Should be exactly 2 arguments")
    # else:
    stage_file(file_path = arguments[0], content = arguments[1])
    #test
    # stage_file('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text1.txt',"22222")
