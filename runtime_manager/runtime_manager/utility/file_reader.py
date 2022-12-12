class File_Reader:

    def __init__(self):
        pass 

    @staticmethod
    def read_file(path):
        print("[File_Reader] - reading file")
        file_object = open(path, "r")
        file_data = file_object.read()
        File_Reader.__close_file__(file_object)
        return file_data

    def __close_file__(file):
        print("[File_Reader] - closing file")
        file.close()