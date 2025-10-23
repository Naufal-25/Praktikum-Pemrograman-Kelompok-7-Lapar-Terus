class Transaksi:
    def __init__(self, id_transaksi, pembeli):
        self.id_transaksi = id_transaksi
        self.pembeli = pembeli
        self.detail = []
        self.status = "Belum Bayar"

    def tambah_detail(self, makan):
        self.detail.append(makan)
    
    def total(self):
        return sum(d.subtotal() for d in self.detail)
    
    def __str__(self):
        total = self.total()
        return f"Transaksi[{self.id_transaksi}] - {self.pembeli.nama} | Total: Rp{total} | Status: {self.status}"