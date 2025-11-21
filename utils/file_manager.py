import os

class FileManager:
    
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    database = os.path.join(base, "database")

    #tes folder ada engga
    @staticmethod
    def testfolder():
        if not os.path.exists(FileManager.database):
            os.makedirs(FileManager.database)
    
    #fungsi ambil path folder
    def getfolder(file):
        FileManager.testfolder()
        return os.path.join(FileManager.database, file)
    
    #baca isi file
    def read(file):
        path = FileManager.getfolder(file)
        if not os.path.exists(path):
            return []
        
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    
    #tulis data ke file
    def write(file, lines):
        path = FileManager.getfolder(file)
        with open(path, "w", encoding="utf=8") as f:
            for l in lines:
                file.write(l + "\n")
    
    #tambah data ke file, reti lah append
    def write(file, line):
        path = FileManager.getfolder(file)
        with open(path, "a", encoding="utf=8") as f:
            file.write(line + "\n")