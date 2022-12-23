import time
from src.pwd_manager import PasswordManager
from src.util.sql_connector import SqliteConnector
from src.util.utils import read_json_config


if __name__ == '__main__':
    # Read config
    config = read_json_config('config.json')

    db_con = SqliteConnector('test_db.db')
    pwd_manager = PasswordManager(db_con)
    print(pwd_manager.list_passwords())

    while True:
        action = input("What do you want to do? ")
        if action == 'q':
            print('Quit now')
            
            # Close connection

            time.sleep(2)
            break