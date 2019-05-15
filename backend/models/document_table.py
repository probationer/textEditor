import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query, select_query
from sqlite3 import Error

NEW = 1
STAGED = 2
COMMIT = 3
MERGED = 4

table_structure = '''
                    CREATE TABLE IF NOT EXISTS document (
                                        doc_id      text        PRIMARY KEY,
                                        file_path   text        NOT NULL,
                                        file_name   text        ,
                                        content     text        NOT NULL,
                                        created_at  DATETIME    NOT NULL,
                                        updated_at  DATETIME    NOT NULL
                    );
                    '''
def document_insert(data):
    query = '''
                INSERT INTO document(doc_id, file_path, file_name, user_id, status, created_at, updated_at) VALUES(?,?,?,?,?,?,?)
            '''
    hash_object = hashlib.md5(str(data['file_path']).encode('UTF-8'))
    doc_id = hash_object.hexdigest()
    date = datetime.datetime.now()
    user_id = '1234567'
    status = '1'
    try:
        insert_query(query, (doc_id, data['file_path'], data['file_name'], user_id, status, date, date))
    except Error as e:
        print("Row already Exixts")
        raise e

def get_doc_data_by_path(path):
    s_query = ' SELECT * from document where file_path = "{}"'.format(path)
    rows = select_query(s_query)
    return rows

    

if __name__ == '__main__':
    pass
    # create_new_table(table_structure)