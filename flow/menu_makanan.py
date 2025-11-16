from fitur.makanan.tambah_makanan import tambah_makanan
from fitur.makanan.baca_makanan import baca_makanan
from fitur.makanan.ubah_makanan import ubah_makanan
from fitur.makanan.hapus_makanan import hapus_makanan

def menu_makanan():
    while True:
        print("\n=== MENU MAKANAN ===")
        print("1. Tambah Makanan")
        print("2. Lihat Daftar Makanan")
        print("3. Ubah Makanan")
        print("4. Hapus Makanan")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_makanan()
        elif pilihan == "2":
            baca_makanan()
        elif pilihan == "3":
            ubah_makanan()
        elif pilihan == "4":
            hapus_makanan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")
