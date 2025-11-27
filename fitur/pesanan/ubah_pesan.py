from fitur.makanan.datamanage_makanan import save_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def ubah_pesanan(daftar_transaksi, daftar_makanan):
    print("\n=== Ubah Pesanan ===")
    id_transaksi = input("Masukkan ID transaksi: ")

    transaksi = next((t for t in daftar_transaksi if t.id_transaksi == id_transaksi), None)
    if not transaksi:
        print("Transaksi tidak ditemukan.\n")
        return
    
    if not transaksi.detail:
        print("Transaksi ini belum memiliki detail pesanan.")
        return

    print("\n=== Detail Pesanan ===")
    for d in transaksi.detail:
        print(f"{d.id_detail}: {d}")

    id_detail = input("\nMasukkan ID detail yang ingin diubah: ")


    target = next((d for d in transaksi.detail if d.id_detail == id_detail), None)
    
    if not target:
        print("ID detail tidak ditemukan.")
        return
    
    makanan_obj = target.makanan
    if not makanan_obj:
        for m in daftar_makanan:
            if m.id_makanan == target.id_makanan:
                makanan_obj = m
                target.makanan = m

    print(f"\nDetail terpilih: {target}")
    print("1. Ubah jumlah")
    print("2. Hapus detail pesanan")
    pilihan = input("Pilih aksi: ")

    if pilihan == "1":
        try:
            n_jumlah = int(input(f"Jumlah baru ({target.jumlah}): ") or target.jumlah)
        except ValueError:
            print("Jumlah harus angka.")
            return

        if n_jumlah <= 0:
            print("Jumlah harus > 0.")
            return

        selisih = n_jumlah - target.jumlah

        if selisih > 0:
            if selisih > makanan_obj.stok:
                print("Stok tidak cukup untuk menambah jumlah.")
                return
            makanan_obj.stok -= selisih
        
        elif selisih < 0:
            makanan_obj.stok += abs(selisih)

        target.jumlah = n_jumlah
        target.subtotal = n_jumlah * makanan_obj.harga

        print("Jumlah pesanan berhasil diperbarui!")

    elif pilihan == "2":
        makanan_obj.stok += target.jumlah

        transaksi.detail = [d for d in transaksi.detail if d.id_detail != id_detail]

        print("Detail pesanan berhasil dihapus!")

    else:
        print("Pilihan tidak valid.")
        return

    transaksi.totalnya = transaksi.hitung_total()
    
    save_makanan(daftar_makanan)
    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)

    print("\nPerubahan telah disimpan.\n")