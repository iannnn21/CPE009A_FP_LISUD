from FileReaderWriter import FileReaderWriter
import json

class JSONFileReaderWriter():
    def read(self, filepath):
        with open(filepath, newline='') as read_file:
            data = json.load(read_file)
            print(data)
            return data

    def write(self, filepath, data):
        with open(filepath, 'w', newline='') as write_file:
            json.dump(obj=data, fp=write_file)
