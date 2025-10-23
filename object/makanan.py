class Makanan:
    def __init__(self, id_makanan, nama, harga, stok):
        self.id_makanan = id_makanan
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def __str__(self):
        return f"{self.nama} - Rp{self.harga} | Stok: {self.stok}"