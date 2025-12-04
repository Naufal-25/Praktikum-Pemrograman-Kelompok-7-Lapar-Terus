class Detail:
    def __init__(self, id_detail, id_transaksi, id_makanan, makanan, jumlah, subtotal):
        self.id_detail = id_detail
        self.id_transaksi = id_transaksi
        self.id_makanan = id_makanan
        self.makanan = makanan
        self.jumlah = jumlah
        self.subtotal = subtotal
    
    def cal_subtotal(self, makanan):
        self.makanan = makanan
        self.subtotal = makanan.harga * self.jumlah
        return self.subtotal
    
    def __str__(self):
        nama = self.makanan.nama if self.makanan else f"ID:{self.id_makanan}"
        return f"Item [{self.id_detail}] {nama} x {self.jumlah} = Rp{self.subtotal}"

    #Simpan ke database txt
    def to_text(self):
        return f"{self.id_detail}|{self.id_transaksi}|{self.id_makanan}|{self.jumlah}|{self.subtotal}"

    #Buka dari database txt
    @staticmethod
    def from_text(line):
        id_detail, id_transaksi, id_makanan, jumlah, subtotal = line.strip().split("|")
        return Detail(id_detail, id_transaksi, id_makanan, None, int(jumlah), float(subtotal))