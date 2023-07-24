from dupman.reader import Reader

class Analyzer:
    def __init__(self, reader=Reader):
        self.reader = reader
    
    def analyze_directory(self, root_path, recursively=True):
        self.reader.get_files()
        pass