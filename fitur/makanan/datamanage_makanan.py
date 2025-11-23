from utils.file_manager import FileManager
from object.makanan import Makanan

file = "makanan.txt"

def load_makanan():
    lines = FileManager.read(file)
    return [Makanan.from_text(l) for l in lines]

def save_makanan(daftar_makanan):
    lines = [m.to_text() for m in daftar_makanan]
    FileManager.write(file, lines)