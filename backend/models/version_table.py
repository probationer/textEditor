import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query
from sqlite3 import Error

table_structure = '''
                    CREATE TABLE IF NOT EXISTS version (
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



    '''


CREATE TABLE Auth(
	user_id varchar(16) PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	email TEXT,
	password varchar(20),
	created_at DATE NOT NULL,
   	updated_at DATE NOT NULL
);

CREATE TABLE document(
	doc_id varchar(16) PRIMARY KEY NOT NULL,
	file_path TEXT NOT NULL,
	file_name TEXT NOT NULL,
	user_id varchar(16) NOT NULL,
	staus varchar(10) NOT NULL,
	created_at DATE NOT NULL,
   	updated_at DATE NOT NULL,
   	FOREIGN KEY (user_id) REFERENCES Auth(user_id)
)

CREATE TABLE staging(
	doc_id varchar(16) NOT NULL,
	last_version varchar(5) NOT NULL,
	diff TEXT NOT NULL,
	created_at DATE NOT NULL,
   	updated_at DATE NOT NULL,
	FOREIGN KEY (doc_id) REFERENCES document(doc_id)
);

CREATE TABLE merged(
	doc_id varchar(16) NOT NULL,
	commit_id varchar(5) NOT NULL,
	created_at DATE NOT NULL,
   	updated_at DATE NOT NULL,
	FOREIGN KEY (doc_id) REFERENCES document(doc_id)
);


CREATE TABLE Version(
	doc_id TEXT NOT NULL,
	version_id TEXT primary key NOT NULL,
	diff TEXT NOT NULL,
	user_id TEXT NOT NULL,
	created_at DATE NOT NULL,
   	updated_at DATE NOT NULL,
	FOREIGN KEY (doc_id) REFERENCES document(doc_id),
	FOREIGN KEY (user_id) REFERENCES Auth(user_id)
);



    '''