from dataclasses import dataclass

@dataclass
class FileObject:
    full_path: str

@dataclass
class File(FileObject):
    hash: str

@dataclass
class Directory(FileObject):
    pass