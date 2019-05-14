import sqlite3
from sqlite3 import Error

def sqlite_connect(db_file = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/database/writerBox.db'):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        raise e
    
def create_new_table(statement):
    try:
        conn = sqlite_connect()
        cursor = conn.cursor()
        cursor.execute(statement)
    except Error as e:
        raise e
    finally:
        conn.close()
 
def select_query(sql):
    try:
        conn = sqlite_connect()
        cursor = conn.cursor()
        rows = cursor.execute(sql)
        return rows.fetchall()
    except Error as e:
        raise e
    finally:
        conn.close()

def insert_query(query, variable):
    try:
        conn = sqlite_connect()
        cur = conn.cursor()
        cur.execute(query, variable)
        conn.commit()
    except Error as e:
        raise e
    finally:
        conn.close()

def update_query(query, variable):
    try:
        conn = sqlite_connect()
        cur = conn.cursor()
        cur.execute(query, variable)
        conn.commit()
    except Error as e:
        raise e
    finally:
        conn.close()

if __name__ == '__main__':
    select= 'Select * from document;'
    select_query(select, 'document')
    # sqlite_connect("../../database/writerBox.db")