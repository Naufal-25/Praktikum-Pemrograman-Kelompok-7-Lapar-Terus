from fitur.makanan.datamanage_makanan import save_makanan

def ubah_makanan(daftar_makanan):
    print("\n=== Ubah Data Makanan ===")
    id_makanan = input("Masukkan ID makanan yang ingin diubah: ")

    target = None
    for makanan in daftar_makanan:
        if makanan.id_makanan == id_makanan:
            target = makanan
            break
    
    if not target:
        print("Makanan tidak ditemukan.\n")
        return

    print(f"Mengubah: {target.nama}")

    print("1. Ubah Nama")
    print("2. Ubah Harga")
    print("3. Ubah Stok")
    print("0. Batal")

    pilih = input("Pilih menu: ").strip()

    # batal
    if pilih == "0":
        print("Perubahan dibatalkan")
        return
        
    # ubah nama
    elif pilih == "1":
        nama_baru = input(f"Nama baru ({target.nama}): ").strip()
        if nama_baru:
            target.nama = nama_baru
        print("Nama berhasil diperbarui!")

    # ubah harga
    elif pilih == "2":
        try:
            str_harga = input(f"Harga baru ({target.harga}): ").strip()
            if str_harga:
                harga_baru = float(str_harga)
                if harga_baru >= 0:
                    target.harga = harga_baru
                    print("Harga berhasil diperbarui!")
                else:
                    print("Harga tidak boleh negatif")
        except ValueError:
            print("Input harga tidak valid")

    # ubah stok
    elif pilih == "3":
        try:
            str_stok = input(f"Stok baru ({target.stok}): ").strip()
            if str_stok:
                stok_baru = int(str_stok)
                if stok_baru >= 0:
                    target.stok = stok_baru
                    print("Stok berhasil diubah.")
                else:
                    print("Stok tidak boleh negatif.")
        except ValueError:
            print("Input stok tidak valid.")
    else:
        ("Pilihan tidak valid, coba lagi.")

    save_makanan(daftar_makanan)