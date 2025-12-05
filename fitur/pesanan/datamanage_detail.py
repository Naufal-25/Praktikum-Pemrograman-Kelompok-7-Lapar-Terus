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
    map_transaksi = {t.id_transaksi: t for t in daftar_transaksi}
    map_makanan = {m.id_makanan: m for m in daftar_makanan}

    lines = FileManager.read(file)
    for line in lines:
        d = Detail.from_text(line)
        if d is None:
            continue

        makanan_obj = map_makanan.get(d.id_makanan)

        if makanan_obj is not None:
            d.makanan = makanan_obj
        else:
            pass

        transaksi_obj = map_transaksi.get(d.id_transaksi)
        if transaksi_obj:
            transaksi_obj.tambah_detail(d)