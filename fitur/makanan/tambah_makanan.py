from object.makanan import Makanan
from fitur.makanan.datamanage_makanan import save_makanan

def tambah_makanan(daftar_makanan):
    print("\n=== Tambah Makanan ===")
    id_makanan = input("ID makanan: ")
    if not id_makanan:
        print("ID tidak boleh kosong")
        return
    
    for m in daftar_makanan:
        if m.id_makanan == id_makanan:
            print("ID sudah digunakan, coba yang lain")
            return
        
    nama = input("Nama makanan: ")
    harga = float(input("Harga: "))
    stok = int(input("Stok: "))

    makanan_baru = Makanan(id_makanan, nama, harga, stok)
    daftar_makanan.append(makanan_baru)

    save_makanan(daftar_makanan)

    print(f"{nama} berhasil ditambahkan!\n")
