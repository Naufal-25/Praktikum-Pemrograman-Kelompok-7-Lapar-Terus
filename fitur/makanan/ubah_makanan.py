from fitur.makanan.datamanage_makanan import save_makanan

def ubah_makanan(daftar_makanan):
    print("\n=== Ubah Data Makanan ===")
    id_makanan = input("Masukkan ID makanan yang ingin diubah: ")

    for makanan in daftar_makanan:
        if makanan.id_makanan == id_makanan:
            makanan.nama = input(f"Nama baru ({makanan.nama}): ") or makanan.nama
            try:
                makanan.harga = float(input(f"Harga baru ({makanan.harga}): ") or makanan.harga)
                makanan.stok = int(input(f"Stok baru ({makanan.stok}): ") or makanan.stok)
            except ValueError:
                print("Input tidak valid, perubahan dibatalkan.")
                return
            print("Data makanan berhasil diperbarui!\n")
            return
    print("Makanan tidak ditemukan.\n")
