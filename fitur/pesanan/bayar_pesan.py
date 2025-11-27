from fitur.makanan.datamanage_makanan import save_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def hapus_pesanan(daftar_transaksi, daftar_makanan):
    print("\n=== Hapus Transaksi ===")
    id_transaksi = input("Masukkan ID transaksi: ")

    index = None
    for i, transaksi in enumerate(daftar_transaksi):
        if transaksi.id_transaksi == id_transaksi:
            index = i
            for d in transaksi.detail:
                for m in daftar_makanan:
                    if m.id_makanan == d.id_makanan:
                        m.stok += d.jumlah
            break
    
    if index is None:
        print("Transaksi tidak ditemukan\n")
        return
    
    daftar_transaksi.pop(i)

    transaksi.total = sum(d.subtotal for d in transaksi.detail)

    save_makanan(daftar_makanan)
    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)
    
    print(f"Transaksi {id_transaksi} berhasil dihapus.\n")
    return

