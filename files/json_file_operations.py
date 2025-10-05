import json

def read_json_file(fn, pretty, sort):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=sort, indent=4 if pretty else data))

def update_json_file(fn, arr_name, pos, key, value):
    with open(fn, 'r') as read_file:
        data = json.load(read_file)
        data[arr_name][pos][key] = value
    with open(fn, 'w') as write_file:
        json.dump(data, write_file, indent=4)


def add_to_json_file(fn, arr_name, key, value):
    with open(fn, 'r') as read_file:
        data = json.load(read_file)
        data[arr_name].append({key: value})


# read_json_file('./authors.json', pretty=True, sort=True)
# update_json_file('./authors.json', 'authors', 0, 'id', 101)
add_to_json_file('./authors.json', 'authors', 'id', 102)

