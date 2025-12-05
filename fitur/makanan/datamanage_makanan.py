from utils.file_manager import FileManager
from object.makanan import Makanan

file = "makanan.txt"

def load_makanan():
    lines = FileManager.read(file)
    daftar_makanan = []
    
    for line in lines:
        makanan_obj = Makanan.from_text(line)
        if makanan_obj is not None:
            daftar_makanan.append(makanan_obj)
    
    return daftar_makanan

def save_makanan(daftar_makanan):
    lines = [m.to_text() for m in daftar_makanan]
    FileManager.write(file, lines)