import json

def read_json_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
      data = json.load(file)
    return data
  except FileNotFoundError:
    print(f"ファイル {file_path} が見つかりませんでした。")
  except json.JSONDecodeError:
    print(f"ファイル {file_path} は有効なJSONではありません。")

data = read_json_file('src_start/Person.json')
for person in data:
    print(person['Name'])