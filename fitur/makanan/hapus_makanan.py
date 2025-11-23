from fitur.makanan.datamanage_makanan import save_makanan

def hapus_makanan(daftar_makanan):
    print("\n=== Hapus Makanan ===")
    id_makanan = input("Masukkan ID makanan yang ingin dihapus: ")
    if not id_makanan:
        print("ID tidak boleh kosong")
        return

    for i, makanan in enumerate(daftar_makanan):
        if makanan.id_makanan == id_makanan:
            daftar_makanan.pop(i)

            save_makanan(daftar_makanan)

            print(f"{makanan.nama} berhasil dihapus.\n")
            return
        
    print("Makanan tidak ditemukan.\n")
