from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        """
        Overrides the base read method to perform text file reading.
        """
        with open(filepath, "r") as f:
            data = f.read()
            print(data)
            return data

    def write(self, filepath, data):
        """
        Overrides the base write method to perform text file writing.
        """
        with open(filepath, "w") as f:
            f.write(str(data))
            print(f"Data successfully written to {filepath}")