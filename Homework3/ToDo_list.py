class Görev:
    def __init__(self, görev_adi: str, tamamlanma_durumu: bool = False):
        self.görev_adi = görev_adi
        self.tamamlanma_durumu = tamamlanma_durumu

    def __repr__(self):
        durum = "✔" if self.tamamlanma_durumu else "✘"
        return f"{self.görev_adi} [{durum}]"


class GörevYönetici:
    def __init__(self):
        self.görevler = []

    def görev_ekle(self, görev_adi: str):
        görev = Görev(görev_adi)
        self.görevler.append(görev)

    def görev_tamamlama(self, görev_adi: str):
        for görev in self.görevler:
            if görev.görev_adi == görev_adi:
                görev.tamamlanma_durumu = True
                break

    def tamamlananlari_sil(self):
        self.görevler = [görev for görev in self.görevler if not görev.tamamlanma_durumu]

    def görevleri_görüntüle(self):
        tamamlanmamiş = [görev for görev in self.görevler if not görev.tamamlanma_durumu]
        tamamlanmiş = [görev for görev in self.görevler if görev.tamamlanma_durumu]
        return tamamlanmamiş, tamamlanmiş

    def dosyaya_kaydet(self, dosya_adi: str):
        with open(dosya_adi, "w") as dosya:
            for görev in self.görevler:
                dosya.write(f"{görev.görev_adi},{görev.tamamlanma_durumu}\n")

    def dosyadan_yükle(self, dosya_adi: str):
        try:
            with open(dosya_adi, "r") as dosya:
                for satir in dosya:
                    görev_adi, tamamlanma_durumu = satir.strip().split(",")
                    self.görevler.append(Görev(görev_adi, tamamlanma_durumu == "True"))
        except FileNotFoundError:
            pass


# Test durumları
görev_yönetici = GörevYönetici()

# Görev ekleme
görev_yönetici.görev_ekle("Ödevi bitir")
görev_yönetici.görev_ekle("Evi temizle")
görev_yönetici.görev_ekle("Market alışverişi yap")

# Görevi tamamlama
görev_yönetici.görev_tamamlama("Ödevi bitir")

# Görevleri görüntüleme
tamamlanmamiş_görevler, tamamlanmiş_görevler = görev_yönetici.görevleri_görüntüle()

# Görevleri bir dosyaya kaydet
dosya_adi = "dosya_yolu\görevler.txt"
görev_yönetici.dosyaya_kaydet(dosya_adi)

# Yeni bir yöneticiyle dosyadan yükleme
yeni_görev_yönetici = GörevYönetici()
yeni_görev_yönetici.dosyadan_yükle(dosya_adi)
yeni_tamamlanmamiş_görevler, yeni_tamamlanmiş_görevler = yeni_görev_yönetici.görevleri_görüntüle()

tamamlanmamiş_görevler, tamamlanmiş_görevler, yeni_tamamlanmamiş_görevler, yeni_tamamlanmiş_görevler
