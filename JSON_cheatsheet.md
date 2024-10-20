# Python JSON Handling Cheat Sheet

## 1. Basic JSON Operations

### Importing JSON Module

```python
import json
```
Function               | Description
-----------------------|------------------------------------------------------------
json.load(fp)          | Parse JSON from a file-like object (fp) into a Python object.
json.loads(s)          | Parse a JSON formatted string (s) into a Python object.
json.dump(obj, fp)     | Serialize a Python object (obj) and write it to a file.
json.dumps(obj)        | Serialize a Python object (obj) into a JSON formatted string.

## 2. Reading JSON 

### From a file
```python
with open('data.json', 'r') as file:
    data = json.load(file)
# `data` now contains the parsed JSON as a Python dictionary or list
```

### From a string
```python
json_string = '{"name": "Emma", "age": 25, "city": "Paris"}'
data = json.loads(json_string)
# `data` will now contain the Python dictionary: {'name': 'Emma', 'age': 25, 'city': 'Paris'}
```
## 3. Writing JSON
### Writing to a file

```python
data = {"name": "Emma", "age": 25, "city": "Paris"}

with open('output.json', 'w') as file:
    json.dump(data, file)
```

### Writing to a string
```python 
data = {"name": "Emma", "age": 25, "city": "Paris"}
json_string = json.dumps(data)
# `json_string` will now contain the JSON string: '{"name": "Emma", "age": 25, "city": "Paris"}'
```

## 4. Formatting options
### Pretty printing JSON
```python 
json_string = json.dumps(data, indent=4)
# Outputs JSON string with indentation of 4 spaces
```

### Sorting Keys in JSON Output
```python
json_string = json.dumps(data, sort_keys=True)
# Sorts the keys in alphabetical order
```

## 5. Handling special data types
### Handling Non-Serializable Objects
Some Python objects, like datetime, set, and custom objects, aren't serializable by default.
Custom Encoder for Non-Serializable Types

```python
import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to string
        return super().default(obj)

data = {"name": "Emma", "created_at": datetime.now()}

json_string = json.dumps(data, cls=CustomEncoder)
```

## 6. Working with Complex Nested JSON
### Accessing Data in Nested JSON
```python 
data = {
    "name": "Emma",
    "details": {
        "age": 25,
        "city": "Paris"
    }
}

# Accessing nested values
name = data["name"]
age = data["details"]["age"]
```

### Updating Nested JSON
```python
data["details"]["age"] = 26
```

## 7. Exception Handling in JSON
### JSONDecode Error
```python
import json

json_string = '{"name": "Emma", "age": 25, "city": "Paris"}'

try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
```

### Common Exception
```csharp
Exception Type        | Description
----------------------|------------------------------------------
json.JSONDecodeError  | Raised when the JSON is invalid or malformed
TypeError             | Raised when an object cannot be serialized into JSON
```
## 8. Merging and Updating JSON Objects
### Merging Two JSON Objects

```python
data1 = {"name": "Emma", "age": 25}
data2 = {"city": "Paris", "age": 26}

# Merging two dictionaries, 'age' in data2 will overwrite 'age' in data1
merged_data = {**data1, **data2}
# `merged_data` will be: {'name': 'Emma', 'age': 26, 'city': 'Paris'}
```

### Updating a JSON Object
```python
data = {"name": "Emma", "age": 25}
update_data = {"age": 26, "city": "Paris"}

data.update(update_data)
# `data` will be updated to: {'name': 'Emma', 'age': 26, 'city': 'Paris'}
```

## 9. Validating JSON
### Checking if a String is Valid JSON
```python
import json

json_string = '{"name": "Emma", "age": 25, "city": "Paris"}'

def is_valid_json(s: str) -> bool:
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

valid = is_valid_json(json_string)
```

## 10. Converting JSON to Other Formats
### Converting JSON to CSV

```python 
import json
import csv

json_data = [
    {"name": "Emma", "age": 25, "city": "Paris"},
    {"name": "John", "age": 30, "city": "London"}
]

# Specify CSV file path
csv_file_path = 'output.csv'

# Convert JSON to CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=json_data[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(json_data)
```

### Converting JSON to XML (using xmltodict)
```python
import json
import xmltodict

json_data = {"name": "Emma", "age": 25, "city": "Paris"}

# Convert JSON to XML
xml_data = xmltodict.unparse({"person": json_data})
# Outputs: "<person><name>Emma</name><age>25</age><city>Paris</city></person>"
```

