class Araba:
    marka = "BUGATTİ"

    def __init__(self, renk,marka):
        self.renk = renk
        self.marka =marka

    def __str__(self):
        return f" {self.renk} {self.marka} "

araba1 = Araba("kırmızı", "BUGATTİ")
araba2 = Araba("siyah", "BMW")

print(araba1)
print(araba2)

