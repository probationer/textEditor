import hashlib
import random
import datetime
from .sqlite_connect import create_new_table, insert_query, select_query
from sqlite3 import Error

table_structure = '''
                    CREATE TABLE Auth(
                        user_id varchar(16) PRIMARY KEY NOT NULL,
                        username TEXT NOT NULL,
                        email TEXT,
                        password varchar(20),
                        created_at DATE NOT NULL,
                        updated_at DATE NOT NULL
                    );
                    '''
def auth_insert(data):
    query = '''
                INSERT INTO auth(user_id, username, email, password, created_at, updated_at) VALUES(?,?,?,?,?,?)
            '''
    hash_object = hashlib.md5(str(data['username'] + str(data['email'])).encode('UTF-8'))
    user_id = hash_object.hexdigest()
    date = datetime.datetime.now()
    username = data['username']
    email = data['email']
    pass_obj = hashlib.md5(str(data['password']).encode('UTF-8'))
    password = pass_obj.hexdigest()
    
    try:
        insert_query(query, (user_id, username, email, password, date, date))
    except Error as e:
        print("Row already Exixts")
        raise e

def get_user_by_id(user_id):
    s_query = ' SELECT * from auth where user_id = "{}"'.format(user_id)
    rows = select_query(s_query)
    return rows

if __name__ == '__main__':
    data = dict()
    data['username'] = 'sandeep'
    data['email'] = 'sandeep@gmail.com'
    data['password'] = '123456789'

    auth_insert(data)