class Makanan:
    def __init__(self, id_makanan, nama, harga, stok):
        self.id_makanan = id_makanan
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def __str__(self):
        return f"{self.nama} - Rp{self.harga} | Stok: {self.stok}"
    
    #buat simpan ke database txt
    def to_text(self):
        return f"{self.id_makanan}|{self.nama}|{self.harga}|{self.stok}"
    
    #buat liat dari database txt
    @staticmethod
    def from_text(line):
        id_makanan, nama, harga, stok = line.strip().split("|")
        return Makanan(id_makanan, nama, int(float(harga)), int(stok))