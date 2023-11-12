import json

def read_json_file(file_path):
  with open(file_path, 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
  return data

data = read_json_file('src_start/Person.json')
for person in data:
    print(person['Name'])