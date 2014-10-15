import json
  
def write_json(file_name, content):
    with open(file_name, 'w') as output_file:
        json.dump(content, output_file, indent=4)

def read_json(file_name):
    with open(file_name, 'r') as input_file:
        return json.load(input_file)

