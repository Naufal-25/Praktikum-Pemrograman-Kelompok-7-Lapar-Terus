class Detail:
    def __init__(self, id_detail, transaksi, makanan, jumlah):
        self.id_detail = id_detail
        self.transaksi = transaksi
        self.makanan = makanan
        self.jumlah = jumlah
    
    def subtotal(self):
        return self.makanan.harga * self.jumlah
    
    def __str__(self):
        return f"{self.makanan.nama} x {self.jumlah} = Rp{self.subtotal()}"