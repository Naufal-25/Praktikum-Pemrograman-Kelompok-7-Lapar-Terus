def hapus_pesanan(daftar_transaksi):
    print("\n=== Hapus Transaksi ===")
    id_transaksi = input("Masukkan ID transaksi: ")

    for transaksi in daftar_transaksi:
        if transaksi.id_transaksi == id_transaksi:
            daftar_transaksi.remove(transaksi)
            print(f"Transaksi {id_transaksi} berhasil dihapus.\n")
            return
    print("Transaksi tidak ditemukan.\n")
#[[Placehoder]]
