# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r))
# print(persons)

# add in code for a Database class

# add in code for a Table class

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated

class Database:
    def __init__(self):
        self.tables = {}

    def load_table(self, table_name, file_path):
        table = Table(file_path)
        self.tables[table_name] = table

    def load_login_table(self, table_name, file_path):
        login_table = LoginTable(file_path)
        self.tables[table_name] = login_table

    def save_table(self, table_name):
        if table_name in self.tables:
            self.tables[table_name].save_data()
        else:
            print(f"Table '{table_name}' not found.")

class Table:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        data = []
        with open(self.file_path) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return data

    def save_data(self):
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)

    def insert_entry(self, entry):
        self.data.append(entry)

    def update_entry(self, entry_id, key, value):
        for entry in self.data:
            if entry.get('ID') == entry_id:
                entry[key] = value
                break

class LoginTable(Table):
    # Inherits from Table, but can have additional functionality specific to login information
    def authenticate(self, username, password):
        for entry in self.data:
            if entry['username'] == username and entry['password'] == password:
                return entry['role']
        return None

# # Example usage
# if __name__ == "__main__":
#     # Instantiate the Database
#     db = Database()

#     # Load the 'persons' table
#     db.load_table('persons', 'persons.csv')

#     # Load the 'login' table
#     db.load_login_table('login', 'login.csv')

#     # Insert a new entry into the 'persons' table
#     new_person = {'ID': '9999999', 'first': 'New', 'last': 'Person', 'type': 'student'}
#     db.tables['persons'].insert_entry(new_person)

#     # Update the 'type' of a specific entry in the 'persons' table
#     db.tables['persons'].update_entry('9999999', 'type', 'lead')

#     # Save changes to the 'persons' table
#     db.save_table('persons')

#     # Print the updated 'persons' table
#     print(db.tables['persons'].data)

#     # Authenticate a user
#     role = db.tables['login'].authenticate('Cristiano.R', '2255')
#     print(f"Authenticated user role: {role}")
