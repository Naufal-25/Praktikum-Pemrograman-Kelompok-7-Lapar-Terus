from utils.file_manager import FileManager
from object.detail import Detail

file = "detail.txt"

def save_detail(daftar_transaksi):
    lines = []
    for t in daftar_transaksi:
        for d in t.detail:
            lines.append(d.to_text())
    FileManager.write(file, lines)

def load_detail(daftar_transaksi, daftar_makanan):
    dir_transaksi = {t.id_transaksi: t for t in daftar_transaksi}
    dir_makanan = {m.id_makanan: m for m in daftar_makanan}

    lines = FileManager.read(file)
    for line in lines:
        d = Detail.from_text(line)
        d.makanan = dir_makanan.get(d.id_makanan)
        
        tr = dir_transaksi.get(d.id_transaksi)
        if tr is not None:
            tr.detail.append(d)