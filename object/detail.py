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
        if self.makanan is not None:
            nama_tampil = self.makanan.nama
        else:
            nama_tampil = f"Item Terhapus ({self.id_makanan})"
        
        return f"{nama_tampil} x {self.jumlah} = Rp{self.subtotal}"

    #Simpan ke database txt
    def to_text(self):
        return f"{self.id_detail}|{self.id_transaksi}|{self.id_makanan}|{self.jumlah}|{self.subtotal}"

    #Buka dari database txt
    @staticmethod
    def from_text(line):
        try:
            parts = line.strip().split("|")
            if len(parts) < 5:
                return None
            
            id_detail = parts[0]
            id_transaksi = parts[1]
            id_makanan = parts[2]
            jumlah = int(parts[3])
            subtotal = float(parts[4])
            return Detail(id_detail, id_transaksi, id_makanan, None, jumlah, subtotal)
        except (ValueError, IndexError):
            return None