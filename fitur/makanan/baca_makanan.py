def baca_makanan(daftar_makanan):
    print("\n=== Daftar Makanan ===")
    if not daftar_makanan:
        print("Belum ada data makanan.")
        
    print(f"{'ID':<10} | {'Nama Makanan':<20} | {'Harga':<12} | {'Stok':<5}")
    print("-"*55)
    
    for makanan in daftar_makanan:
        print(f"{makanan.id_makanan:<10} | {makanan.nama:<20} | Rp{makanan.harga:<10} | {makanan.stok:<5}")
