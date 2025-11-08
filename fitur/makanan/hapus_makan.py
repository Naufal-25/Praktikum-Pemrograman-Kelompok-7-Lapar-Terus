def hapus_makanan(daftar_makanan):
    print("\n=== Hapus Makanan ===")
    id_makanan = input("Masukkan ID makanan yang ingin dihapus: ")

    for makanan in daftar_makanan:
        if makanan.id_makanan == id_makanan:
            daftar_makanan.remove(makanan)
            print(f"{makanan.nama} berhasil dihapus.\n")
            return
    print("Makanan tidak ditemukan.\n")
#[[Placehoder]]
