def baca_makanan(daftar_makanan):
    print("\n=== Daftar Makanan ===")
    if not daftar_makanan:
        print("Belum ada data makanan.")
        return
    for makanan in daftar_makanan:
        print(f"[{makanan.id_makanan}] {makanan.nama} - Rp{makanan.harga} | Stok: {makanan.stok}")
#[[Placehoder]]
