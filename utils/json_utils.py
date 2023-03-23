import json

def change_json_values(json_path,name,job):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    data["name"] = name
    data["job"] = job
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file)

def write_response_to_file(json_rs_path,res_json):
    with open(json_rs_path, 'a') as output_file:
        json.dump(res_json, output_file)