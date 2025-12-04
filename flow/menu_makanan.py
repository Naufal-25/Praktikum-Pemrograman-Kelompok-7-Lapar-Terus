from fitur.makanan.tambah_makanan import tambah_makanan
from fitur.makanan.baca_makanan import baca_makanan
from fitur.makanan.ubah_makanan import ubah_makanan
from fitur.makanan.hapus_makanan import hapus_makanan

def menu_makanan(daftar_makanan):
    while True:
        print("\n=== MENU MAKANAN ===")
        print("1. Tambah Makanan")
        print("2. Lihat Daftar Makanan")
        print("3. Ubah Makanan")
        print("4. Hapus Makanan")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_makanan(daftar_makanan)
        elif pilihan == "2":
            baca_makanan(daftar_makanan)
        elif pilihan == "3":
            ubah_makanan(daftar_makanan)
        elif pilihan == "4":
            hapus_makanan(daftar_makanan)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")
