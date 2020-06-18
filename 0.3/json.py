import json5

x = {
"name": "Viktor",
"age": 30,
"married": True,
"divorced": False,
"children": ("Anna","Bogdan"),
"pets": None,
"cars": [
{"model": "BMW 230", "mpg":  27.5},
{"model": "Ford Edge", "mpg": 24.1}
]
}
print(json5.dumps(x))