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

    print(f"\nData ditemukan: [{target.id_makanan}] {target.nama} - Rp{target.harga} | Stok: {target.stok}")

    while True:
        print("""
Apa yang ingin Anda ubah?
1. Nama
2. Harga
3. Stok
4. Ubah Semua
0. Batal
""")

        pilih = input("Pilih menu: ").strip()

        # batal
        if pilih == "0":
            print("Perubahan dibatalkan.\n")
            return
        
        # ubah nama
        elif pilih == "1":
            nama_baru = input(f"Nama baru ({target.nama}): ").strip()
            if nama_baru:
                target.nama = nama_baru
            print("Nama berhasil diperbarui!\n")
            break

        # ubah harga
        elif pilih == "2":
            harga_baru = input(f"Harga baru ({target.harga}): ").strip()
            if harga_baru:
                try:
                    target.harga = float(harga_baru)
                except ValueError:
                    print("Input harga tidak valid!")
                    continue
            print("Harga berhasil diperbarui!\n")
            break

        # ubah stok
        elif pilih == "3":
            stok_baru = input(f"Stok baru ({target.stok}): ").strip()
            if stok_baru:
                try:
                    target.stok = int(stok_baru)
                except ValueError:
                    print("Input stok tidak valid!")
                    continue
            print("Stok berhasil diperbarui!\n")
            break

        # ubah semua
        elif pilih == "4":
            # nama
            nama_baru = input(f"Nama baru ({target.nama}): ").strip()
            if nama_baru:
                target.nama = nama_baru
            
            # harga
            harga_baru = input(f"Harga baru ({target.harga}): ").strip()
            if harga_baru:
                try:
                    target.harga = float(harga_baru)
                except ValueError:
                    print("Input harga tidak valid! Ubah semua dibatalkan.")
                    return

            # stok
            stok_baru = input(f"Stok baru ({target.stok}): ").strip()
            if stok_baru:
                try:
                    target.stok = int(stok_baru)
                except ValueError:
                    print("Input stok tidak valid! Ubah semua dibatalkan.")
                    return

            print("Semua data berhasil diperbarui!\n")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

    save_makanan(daftar_makanan)