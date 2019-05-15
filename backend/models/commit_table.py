import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query, select_query, update_query
from sqlite3 import Error
from .document_table import COMMIT
from .stage_table import remove_from_staging

table_structure = '''
                    CREATE TABLE commit_table(
                        doc_id varchar(16) NOT NULL,
                        commit_id varchar(32) PRIMARY KEY NOT NULL,
                        diff TEXT NOT NULL,
                        created_at DATE NOT NULL,
                        updated_at DATE NOT NULL,
                        FOREIGN KEY (doc_id) REFERENCES document(doc_id)
                    );
                    '''

date = datetime.datetime.now()

def commit_insert(data):
    query = '''
                INSERT INTO commit_table(doc_id, commit_id, diff,  created_at, updated_at) VALUES(?,?,?,?,?)
            '''
    doc_id = data['doc_id']
    diff = data['content']
    hash_object = hashlib.md5((str(data['user_id']) + str(doc_id) + str(date.timestamp())).encode('UTF-8'))
    commit_id = hash_object.hexdigest()
    try:
        insert_query(query, (doc_id, commit_id, diff, date, date))
        doc_status_update(doc_id)
        remove_from_staging(doc_id)
    except Error as e:
        print("ERROR : " +str(e))

def get_doc_data_by_commit_id(commit_id):
    s_query = ' SELECT * from commit_table where commit_id = "{}"'.format(commit_id)
    rows = select_query(s_query)
    return rows

def doc_status_update(doc_id):
    up_query = '''
                UPDATE document SET status = ?, updated_at = ? where doc_id = ?
                '''
    try:
        update_query(up_query, (COMMIT, date, doc_id))
    except Error as e:
        print("doc table couldn't be update from commit table")
        raise e

if __name__ == '__main__':
    pass
    #commit_insert(table_structure)