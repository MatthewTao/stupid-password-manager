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
        password = password_tuple[3]

        return password

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
            pwd = self._read_password(int(pwd_id))
            return pwd
