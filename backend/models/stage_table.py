import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query, select_query, update_query
from sqlite3 import Error
from .document_table import (NEW, STAGED, COMMIT, MERGED)

table_structure = '''
                    CREATE TABLE IF NOT EXIST staging(
                        doc_id varchar(16) NOT NULL,
                        last_version varchar(5) NOT NULL,
                        diff TEXT NOT NULL,
                        created_at DATE NOT NULL,
                        updated_at DATE NOT NULL,
                        FOREIGN KEY (doc_id) REFERENCES document(doc_id)
                    );
                    '''
def staging_create_or_update(data):
    print("mark 1")
    date = datetime.datetime.now()
    row = get_staging_data(data['doc_id'])
    if row:
        previous_file_content = row[0][2]
        update_sql = ''' UPDATE staging SET diff = ?, updated_at = ?  WHERE doc_id = ? '''
        update_query(update_sql, (data['content'], date, data['doc_id']))
    else:
        try:   
            ins_query = '''
                INSERT INTO staging(doc_id, last_version, diff, created_at, updated_at) VALUES(?,?,?,?,?)
                '''
            doc_ins = '''
                        UPDATE document SET status = ?, updated_at = ?  WHERE doc_id = ?
                    '''
            values = (data['doc_id'], '1', data['content'], date, date)
            insert_query(ins_query, values)
            insert_query(doc_ins, (STAGED, date, data['doc_id']))
        except Error as e:
            print("\n\nRow already Exixts")
            raise e


def get_staging_data(doc_id):
    s_query = ' SELECT * from staging where doc_id = "{}"'.format(doc_id)
    row = select_query(s_query)
    return row

if __name__ == '__main__':
    pass
    # create_new_table(table_structure)