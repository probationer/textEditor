import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query, select_query
from sqlite3 import Error

table_structure = '''
                    CREATE TABLE IF NOT EXIST Version(
						doc_id TEXT NOT NULL,
						version_id TEXT primary key NOT NULL,
						commit_id varchar(32) UNIQUE NOT NULL, 
						user_id TEXT NOT NULL,
						created_at DATE NOT NULL,
						updated_at DATE NOT NULL,
						FOREIGN KEY (doc_id) REFERENCES document(doc_id),
						FOREIGN KEY (commit_id) REFERENCES commit_table(commit_id),
						FOREIGN KEY (user_id) REFERENCES Auth(user_id)
					);
                    '''

def version_insert(data):
		ins_query = 'INSERT INTO version(doc_id, version_id, commit_id, user_id, created_at, updated_at) VALUES(?,?,?,?,?,?)'
		doc_id = data['doc_id']
		commit_id = data['commit_id']
		user_id = data['user_id']
		date = datetime.datetime.now()
		ver_obj = hashlib.md5((str(date.timestamp())+str(commit_id)).encode('UTF-8'))
		version_id = ver_obj.hexdigest()
		try:
			insert_query(ins_query, (doc_id, version_id, commit_id, user_id, date, date))
		except Error as e:
			print("Row already Exixts")

def get_all_rows(data):
	sel = 'select * from version where doc_id = "{}"'.format(data)
	rows = select_query(sel)
	return rows

if __name__ == '__main__':
    pass
    # create_new_table(table_structure)