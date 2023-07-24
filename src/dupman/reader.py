from dupman.file_manager import FileManager


class Reader:
    def get_files(path: str, recursively=True, f_manager=FileManager):
        local_files = f_manager.get_files(path)
        if recursively:
            directories = f_manager.get_directories(path)
            child_files = [Reader.get_files(d) for d in directories]
            return local_files + child_files