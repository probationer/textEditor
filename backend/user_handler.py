from models.auth_table import auth_insert
from models.sqlite_connect import select_query
from sqlite3 import Error

def user_id_checker(user_id):
    try:
        sel_query = 'select * from auth where user_id = "{}"'.format(user_id)
        rows = select_query(sel_query)
        return True
    except Error as e:
        return False
def user_register(username, email, password, confirm_password):
    if password == confirm_password:
        try:
            data = dict()
            data['username'] = username
            data['email'] = email
            data['password'] = password
            auth_insert(data)
            print('registerd')
        except Error as e :
            raise "ERROR WHILE INSERT DATA"
    else :
        raise "PASSWORDS NOT MATCHED"

if __name__ == "__main__":
    user_register('test2', 'teat2@gmail.com', '123345', '123345')