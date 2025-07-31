import json

def load_schema(schema_path: str) -> dict:
    with open(schema_path, 'r') as file:
        return json.load(file)
