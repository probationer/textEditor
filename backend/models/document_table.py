import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query
from sqlite3 import Error

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
                INSERT INTO document(doc_id, file_path, file_name, created_at, updated_at) VALUES(?,?,?,?,?)
            '''
    hash_object = hashlib.md5(str(data['file_path']).encode('UTF-8'))
    doc_id = hash_object.hexdigest()
    date = datetime.datetime.now()
    try:
        insert_query(query, (doc_id, data['file_path'], data['file_name'], date, date))
    except Error as e:
        print("Row already Exixts")


    

if __name__ == '__main__':
    pass
    # create_new_table(table_structure)