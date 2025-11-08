from object.makanan import Makanan

def tambah_makanan(daftar_makanan):
    print("\n=== Tambah Makanan ===")
    id_makanan = input("ID makanan: ")
    nama = input("Nama makanan: ")
    harga = float(input("Harga: "))
    stok = int(input("Stok: "))

    makanan_baru = Makanan(id_makanan, nama, harga, stok)
    daftar_makanan.append(makanan_baru)
    print(f"{nama} berhasil ditambahkan!\n")
#[[Placehoder]]
