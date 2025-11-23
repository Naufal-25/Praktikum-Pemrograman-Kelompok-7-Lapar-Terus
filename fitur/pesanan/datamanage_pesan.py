from utils.file_manager import FileManager
from object.transaksi import Transaksi

file = "transaksi.txt"

def load_transaksi():
    lines = FileManager.read(file)
    return [Transaksi.from_text(l) for l in lines]

def save_transaksi(daftar_transaksi):
    lines = [t.to_text() for t in daftar_transaksi]
    FileManager.write(file, lines)