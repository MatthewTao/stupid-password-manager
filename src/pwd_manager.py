"""
Stupid Password Manager
"""


class PasswordManager:
    def __init__(self, db_connector):
        self.db_connector = db_connector
        self.passwords = []

    def _read_password(self, pwd_id):
        # get password from db
        password = None
        return password

    def list_passwords(self):
        # Get list of passwords from db
        passwords = None
        self.passwords = passwords
        return passwords

    def fetch_password(self, pwd_id):
        if pwd_id not in self.passwords:
            raise Exception('Password does not exist')
        else:
            pwd = self._read_password(pwd_id)
            return pwd
