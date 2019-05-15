import sys
import json
import random
from sqlite3 import Error
from models.document_table import document_insert

def StorePath(file_path):
    data = dict()
    data['file_name'] = file_path.split("/")[-1] if file_path.split("/") else None
    # content = str()
    data['file_path'] = file_path
    try : 
        document_insert(data)
    except Error as e: 
        print("file already exists")

# def StorePath(json_path, info):
#     json_path += 'path.json'
#     data =dict()
#     with open(json_path, 'r') as file:
#         data = json.load(file)
#         file_list = list(data["path"])
#     file.close()
#     if info not in file_list:
#         file_list.append(info)
#     data["path"] = file_list
#     # print(json.dumps(data, indent=4))
#     with open(json_path, 'w') as file:
#         file.write(json.dumps(data, indent=4))
#     file.close()
    # print("files Stored")

def Inventory_file(file_path, path_file = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/.meta/path.json'):
    with open(path_file) as paths:
        path = json.load(paths)
        if path[file_path]:
            return path[file_path]
        else: 
            return False

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("Should be exactly 2 arguments")
    else:
        print(arguments[0])
        StorePath(arguments[0])

    #test
    # StorePath('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/.meta/',"2")
