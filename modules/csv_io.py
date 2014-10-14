import csv

def read_csv(file_name):
    data = [] 
    with open(file_name, 'r') as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            data.append(row)
    return data[0] if len(data) == 1 else data

def write_csv(file_name, content):
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)  
        writer.writerows(content)  

