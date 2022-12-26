import time
import pyperclip
from src.pwd_manager import PasswordManager
from src.util.sql_connector import SqliteConnector
from src.util.utils import read_json_config


def retrieve_password():
    passwords = pwd_manager.list_passwords()
    ids = []
    print('\n')  # Add a bit of blank space for aesthetics
    for id, name in passwords.items():
        print(f'{id}: {name}')
        ids.append(str(id))

    pwd_id = input("Select password that you want to retrive: ")
    
    pwd_dict = pwd_manager.fetch_password(pwd_id)

    if pwd_dict.get('copy_user') == 1:
        # Put user name into clipboard

        # Press enter to proceed

        raise NotImplementedError

    if pwd_dict.get('copy_pass') == 1:
        # Put password into clipboard
        password = pwd_dict.get('pass')
        pyperclip.copy(password)

        print("\nYou have 30 seconds to paste the password\n\n")
        time.sleep(30)
        
        # This won't be fool proof as clipboard now can hold multiple entries
        pyperclip.copy('Some random text to replace the password on the clipboard')


def edit_password():
    raise NotImplementedError


def add_password():
    raise NotImplementedError


if __name__ == '__main__':
    # Read config
    config = read_json_config('config.json')
    set_queries = read_json_config('./src/util/set_queries.json')

    db_con = SqliteConnector(config.get('db_path'))
    db_con.execute_query(set_queries['create_table'])

    pwd_manager = PasswordManager(db_con)

    while True:
        action = input("What do you want to do? \nq: Quit  r: Retrieve  a: Add  e: Edit\n")
        if action == 'q':
            print('Quit now')
            
            # Close connection
            db_con.close_connection()

            time.sleep(2)
            break
        elif action == 'r':
            retrieve_password()

        elif action == 'e':
            edit_password()

        elif action == 'a':
            add_password()
