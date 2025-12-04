from fitur.makanan.datamanage_makanan import save_makanan

def hapus_makanan(daftar_makanan):
    print("\n=== Hapus Makanan ===")
    id_makanan = input("Masukkan ID makanan yang ingin dihapus: ").strip()

    index_del = -1
    for i, makanan in enumerate(daftar_makanan):
        if makanan.id_makanan == id_makanan:
            index_del = i
            break

    if index_del != -1:
        nama_del = daftar_makanan[index_del].nama
        daftar_makanan.pop(index_del)
        save_makanan(daftar_makanan)
        print(f"{makanan.nama} berhasil dihapus.\n")
    else:
        print("Makanan tidak ditemukan.\n")
