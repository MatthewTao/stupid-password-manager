"""
Stupid Password Manager
"""


class PasswordManager:
    def __init__(self, db_connector):
        self.db_connector = db_connector
        self.passwords = []

    def _read_password(self, pwd_id):
        # get password from db
        if isinstance(pwd_id, int) is not True:
            raise Exception(f'Invalid password ID provided: {pwd_id}')
        else:
            password_tuple = self.db_connector.execute_query(
                f"SELECT * FROM pwd_table WHERE id = {pwd_id}"
            ).fetchall()[0]
        
        # 3rd element is the password for now
        password_dict = {
            "id": password_tuple[0],
            "name": password_tuple[1],
            "user": password_tuple[2],
            "pass": password_tuple[3],
            "copy_user": password_tuple[4],
            "copy_pass": password_tuple[5],
            "encrypted": password_tuple[6]
        }
        return password_dict

    def list_passwords(self):
        # Get list of passwords from db
        passwords = self.db_connector.execute_query(
            "SELECT id, name FROM pwd_table"
        ).fetchall()

        # SQLite returns the data as a tuple of tuples
        # Iterate over the tuple and build a dict out of it
        # 0 is the ID and 1 is the name of the password
        passwords_dict = {}
        for password in passwords:
            passwords_dict.update(
                {
                    str(password[0]): password[1]
                }
            )
        self.passwords = passwords_dict
        return passwords_dict

    def fetch_password(self, pwd_id):
        if pwd_id not in self.passwords:
            raise Exception('Password does not exist')
        else:
            pwd_dict = self._read_password(int(pwd_id))
        
        # The entire row has now been fetch.
        # Now process the dict so that the user can use it.
        if pwd_dict['copy_pass'] == 1 and pwd_dict['copy_user'] == 0 and pwd_dict['encrypted'] == 0:
            # The password should not be encrypted therefore no futher action needed.
            # Just need to remove some keys
            keys_to_remove = ['id', 'name', 'user', 'encrypted']

        elif pwd_dict['copy_pass'] == 1 and pwd_dict['copy_user'] == 1 and pwd_dict['encrypted'] == 0:
            # The password should not be encrypted therefore no futher action needed.
            # Just need to remove some keys
            keys_to_remove = ['id', 'name', 'encrypted']
        
        # Remove the keys that won't be used.
        for key in keys_to_remove:
            pwd_dict.pop(key, None)

        return pwd_dict
