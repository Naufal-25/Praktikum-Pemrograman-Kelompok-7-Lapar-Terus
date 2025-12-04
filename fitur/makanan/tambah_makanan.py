from object.makanan import Makanan
from fitur.makanan.datamanage_makanan import save_makanan

def tambah_makanan(daftar_makanan):
    print("\n=== Tambah Makanan ===")
    id_makanan = input("ID makanan: ").strip()
    if not id_makanan:
        print("ID tidak boleh kosong")
        return
    
    for m in daftar_makanan:
        if m.id_makanan == id_makanan:
            print(f"ID {id_makanan} sudah digunakan oleh {m.nama}, coba yang lain")
            return
        
    nama = input("Nama makanan: ").strip()
    if not nama:
        print("Nama tidak boleh kosong")
        return
    try:
        harga = float(input("Harga: "))
        stok = int(input("Stok: "))
    except ValueError:
        print("Harga / Stok harus berupa angka!")
        return
    
    if harga < 0 or stok < 0:
        print("Harga / Stok tidak boleh negatif")
        
    makanan_baru = Makanan(id_makanan, nama, harga, stok)
    daftar_makanan.append(makanan_baru)

    save_makanan(daftar_makanan)

    print(f"{nama} berhasil ditambahkan!\n")
