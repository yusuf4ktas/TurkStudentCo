class Urun:
    def __init__(self, urun_adi: str, urun_fiyati: float, urun_miktari: int):
        self.urun_adi = urun_adi
        self.urun_fiyati = urun_fiyati
        self.urun_miktari = urun_miktari

class Sepet:
    def __init__(self):
        self.urunler = []  # Ürünleri depolamak için liste

    def urun_ekle(self, ad: str, fiyat: float, miktar: int):
        yeni_urun = Urun(ad, fiyat, miktar)
        self.urunler.append(yeni_urun)

    def urun_cikar(self, ad: str):
        for urun in self.urunler:
            if urun.urun_adi == ad:
                self.urunler.remove(urun)
                return  #Eşleşme bulunca dur

    def toplam(self):
        toplam_tutar = 0
        for urun in self.urunler:
            toplam_tutar += urun.urun_fiyati * urun.urun_miktari
        return toplam_tutar
    
    def listele(self):
        return [(urun.urun_adi, urun.urun_miktari, urun.urun_fiyati) for urun in self.urunler]


    
#Sepet oluşturma 
sepet = Sepet()

#Ürün ekleme (ad,fiyat,miktar)
sepet.urun_ekle("Elma", 3.0, 5) 
sepet.urun_ekle("Armut", 4.0, 3) 
sepet.urun_ekle("Portakal", 2.5, 10)

# Toplam hesaplama
toplam_tutar = sepet.toplam()

# Sepetteki ürünleri listeler
urun_listesi = sepet.listele()

sepet.urun_cikar("Armut")

# Calculate total price after removal
islem_sonrasi_toplam_tutar = sepet.toplam()

# Updated product list
islem_sonrasi_urun_listesi = sepet.listele()

urun_listesi, toplam_tutar, islem_sonrasi_urun_listesi, islem_sonrasi_toplam_tutar