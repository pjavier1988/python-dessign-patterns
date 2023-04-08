class JSONAdapter:
    def __init__(self, json_data):
        if not all(isinstance(item, dict) for item in json_data):
            raise ValueError("Data must be in JSON Format")
        self.data = json_data

    def get_value(self, key):

        return self.data[key]


class CSVLibrary:
    def __init__(self, csv_data):
        self.data = csv_data

    def get_data(self):
        return self.data

    def get_value(self, key):
        return self.data[key]


class CSVToJSONAdapter(CSVLibrary):
    def __init__(self, csv_data):
        super().__init__(csv_data)

    def get_data(self):
        json_data = []

        for row in self.data:
            json_data.append({
                'name': row[0],
                'age': row[1],
                'address': row[2]
            })
        return json_data

    def get_value(self, key):
        return self.get_data()[key]


csv_data = [
    ['John', 28, '123 Main St.'],
    ['Jane', 32, '456 Oak Ave.'],
    ['Bob', 45, '789 Elm St.']
]

csv_to_json_adapter = CSVToJSONAdapter(csv_data)

json_adapter = JSONAdapter(csv_to_json_adapter.get_data())
print(json_adapter.get_value(1))  # Output: {'name': 'Jane', 'age': 32, 'address': '456 Oak Ave.'}
