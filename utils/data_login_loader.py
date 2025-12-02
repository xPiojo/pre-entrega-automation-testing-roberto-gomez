# Leer el csv y devolver una lista de tuplas
import csv

def load_login_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [
            (
                row['username'],
                row['password'],
                row['debe_funcionar'].strip().lower() == 'true'
            )
            for row in reader
        ]
