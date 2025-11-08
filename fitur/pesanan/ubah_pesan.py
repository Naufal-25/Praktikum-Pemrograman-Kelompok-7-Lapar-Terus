def ubah_pesanan(daftar_transaksi):
    print("\n=== Ubah Pesanan ===")
    id_transaksi = input("Masukkan ID transaksi: ")

    for transaksi in daftar_transaksi:
        if transaksi.id_transaksi == id_transaksi:
            if not transaksi.detail:
                print("Transaksi ini belum memiliki detail.")
                return
            for d in transaksi.detail:
                print(f"{d.id_detail}: {d}")
            id_detail = input("Masukkan ID detail yang ingin diubah: ")
            for d in transaksi.detail:
                if d.id_detail == id_detail:
                    d.jumlah = int(input(f"Jumlah baru ({d.jumlah}): ") or d.jumlah)
                    print("Detail pesanan berhasil diperbarui!\n")
                    return
            print("ID detail tidak ditemukan.")
            return
    print("Transaksi tidak ditemukan.\n")
#[[Placehoder]]
