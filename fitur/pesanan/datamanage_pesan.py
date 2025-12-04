from utils.file_manager import FileManager
from object.transaksi import Transaksi

file = "transaksi.txt"

def load_transaksi():
    lines = FileManager.read(file)
    daftar_transaksi = []

    for line in lines:
        t = Transaksi.from_text(line)
        if t is not None:
            daftar_transaksi.append(t)
    return daftar_transaksi

def save_transaksi(daftar_transaksi):
    lines = [t.to_text() for t in daftar_transaksi]
    FileManager.write(file, lines)