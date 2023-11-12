import json
import yaml

def read_json_file(file_path):
  with open(file_path, 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
  return data

def json_to_yaml(json_data):
  return yaml.dump(json_data)

def write_yaml_file(file_path, yaml_data):
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(yaml_data)

data = read_json_file('src_start/Person.json')
yaml_data = json_to_yaml(data)
write_yaml_file('src_start/Person.yaml', yaml_data)