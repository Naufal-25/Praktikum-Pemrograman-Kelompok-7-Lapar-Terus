from fitur.makanan.datamanage_makanan import save_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def ubah_pesanan(daftar_transaksi, daftar_makanan):
    print("\n=== Ubah Pesanan ===")
    id_transaksi = input("Masukkan ID transaksi: ").strip()

    transaksi = None
    for t in daftar_transaksi:
        if t.id_transaksi == id_transaksi:
            transaksi = t
            break
    
    if not transaksi:
        print("Transaksi tidak ditemukan\n")
        return
    
    if not transaksi.detail:
        print("Transaksi ini kosong")
        return

    print(f"\nIsi Pesanan {transaksi.pembeli.nama}:")
    for d in transaksi.detail:
        nama_menu = d.makanan.nama if d.makanan else "???"
        print(f"ID: {d.id_detail} | {nama_menu} | Jumlah: {d.jumlah}")

    id_detail = input("\nMasukkan ID detail yang ingin diubah: ").strip()

    target_detail = None
    for d in transaksi.detail:
        if d.id_detail == id_detail:
            target_detail = d
            break
    
    if not target_detail:
        print("ID detail tidak ditemukan.")
        return
    
    makanan_obj = target_detail.makanan
    if not makanan_obj:
        print("Data tidak ditemukan dalam database")
        return

    print(f"\nItem terpilih: {makanan_obj.nama} (saat ini: {target_detail.jumlah})")
    print("1. Ubah jumlah")
    print("2. Hapus detail pesanan")
    print("0. Batal")
    pilihan = input("Pilih aksi: ").strip()

    if pilihan == "1":
        try:
            jumlah_baru = int(input(f"Masukkan jumlah baru : "))
        except ValueError:
            print("Jumlah harus angka.")
            return

        if jumlah_baru <= 0:
            print("Jumlah harus lebih dari 0")
            return

        selisih = jumlah_baru - target_detail.jumlah

        if selisih > 0 and selisih > makanan_obj.stok:
            print(f"Stok tidak cukup! sisa stok: {makanan_obj.stok}")
            return
            
        makanan_obj.stok -= selisih
        target_detail.jumlah = jumlah_baru
        target_detail.cal_subtotal(makanan_obj)

        print("Jumlah berhasil diubah")

    elif pilihan == "2":
        makanan_obj.stok += target_detail.jumlah

        transaksi.detail.remove(target_detail)

        print("Item berhasil dihapus!")

    elif pilihan == "0":
        return

    else:
        print("Pilihan tidak valid.")
        return
    
    save_makanan(daftar_makanan)
    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)

    print("\nPerubahan telah disimpan.")