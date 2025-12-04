def bayar_pesanan(daftar_transaksi, daftar_makanan):
    print("\n=== Pembayaran (Kasir) ===")
    id_transaksi = input("Masukkan ID transaksi: ").strip()

    target = None
    for t in daftar_transaksi:
        if t.id_transaksi == id_transaksi:
            target = t
            break

    if not target:
        print("transakasi tidak ditemukan")
        return
    
    total_tagihan = target.hitung_total()

    print("\n"+"="*30)
    print(f"Tagihan : {target.pembeli.nama}")
    print(f"Total   : Rp{total_tagihan}")
    print("="*30)
    try:
        uang = float(input("Uang Tunai: Rp "))
        if uang < total_tagihan:
            kurang = total_tagihan - uang
            print(f"Uang kurang: Rp {kurang}")
        else:
            kembalian =  uang - total_tagihan
            print(f"Kembalian : Rp {kembalian}")
            print("\n--- Pembayaran Lunas ---")
    except ValueError:
        print("Input uang tidak valid")
    