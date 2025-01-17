import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(type(data))
print(data)
Json = json.dumps(data)
print(type(Json))
print(Json)

data2='{ "name": "John", "age": 30, "city": "New York" }'
print(type(data2))
print(data2)
Json2=json.loads(data2)
print(type(Json2))
print(Json2)