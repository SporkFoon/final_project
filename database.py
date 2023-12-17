import csv
import os

class Database:
    def __init__(self):
        self.tables = {}

    def add_table(self, table_name, table):
        self.tables[table_name] = table

class Table:
    def __init__(self, csv_file_path):
        self.file_path = csv_file_path
        self.entries = self.read_csv()

    def read_csv(self):
        with open(self.file_path) as f:
            rows = csv.DictReader(f)
            return [dict(r) for r in rows]

    def write_csv(self):
        with open(self.file_path, 'w', newline='') as f:
            fieldnames = self.entries[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.entries)

    def insert_entry(self, entry):
        self.entries.append(entry)
        self.write_csv()

    def update_entry(self, entry_id, key, value):
        for entry in self.entries:
            if entry['ID'] == entry_id:
                entry[key] = value
                self.write_csv()
                break