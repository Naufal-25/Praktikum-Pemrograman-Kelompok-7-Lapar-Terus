from fitur.makanan.datamanage_makanan import save_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def hapus_pesanan(daftar_transaksi, daftar_makanan):
    print("\n=== Hapus Transaksi ===")
    id_transaksi = input("Masukkan ID transaksi: ")

    index_target = -1
    for i, t in enumerate(daftar_transaksi):
        if t.id_transaksi == id_transaksi:
            index_target = i
            break
    
    if index_target == -1:
        print("transaksi tidak ditemukan")
        return
    transaksi = daftar_transaksi[index_target]
    
    print("Mengembalikan stok makanan...")
    for d in transaksi.detail:
        if d.makanan:
            d.makanan.stok += d.jumlah
            print(f" + {d.makanan.nama} (stok kembali {d.jumlah})" )
    
    daftar_transaksi.pop(index_target)

    save_makanan(daftar_makanan)
    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)
    
    print(f"Transaksi {id_transaksi} berhasil dihapus.\n")
    return

