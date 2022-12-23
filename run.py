import time
import pyperclip
from src.pwd_manager import PasswordManager
from src.util.sql_connector import SqliteConnector
from src.util.utils import read_json_config


if __name__ == '__main__':
    # Read config
    config = read_json_config('config.json')
    set_queries = read_json_config('./src/util/set_queries.json')

    db_con = SqliteConnector(config.get('db_path'))
    db_con.execute_query(set_queries['create_table'])

    pwd_manager = PasswordManager(db_con)
    passwords = pwd_manager.list_passwords()
    ids = []
    for id, name in passwords.items():
        print(f'{id}: {name}')
        ids.append(str(id))

    while True:
        action = input("What do you want to do? ")
        if action == 'q':
            print('Quit now')
            
            # Close connection
            db_con.close_connection()

            time.sleep(2)
            break

        elif action in ids:
            # Here the action is the same as the password id
            # Therefore we can pass in action to fetch_password()
            password = pwd_manager.fetch_password(action)

            # Put password into clipboard
            pyperclip.copy(password)

            print("You have 30 seconds to paste the password\n\n")
            time.sleep(30)
            
            # This won't be fool proof as clipboard now can hold multiple entries
            pyperclip.copy('Some random text to replace the password on the clipboard')

