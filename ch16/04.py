import json

# json - dump, load <-- file
# json - dumps, loads <-- fast API, Flask

data = {"name": "Kim", "age":23}

print(data["name"], type(data), json.dumps(data), type(json.dumps(data))) # dumps: dict -> string type으로
res_data = json.dumps(data)
print(type(json.loads(res_data))) # loads: string -> dict type으로