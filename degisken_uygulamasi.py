""",Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

"""
musteri_ismi = "Abdulkadir Tutar"
musteri_no = "05422423965"
musteri_mail = "abdulkadirtutar1@gmail.com"
musteri_sehri = "van"
print(musteri_ismi,musteri_mail,musteri_no,musteri_sehri)

urun1Adi = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Ad = "Kablozus klavye"
urun2Fiyat = 650   

toplamOdenenUcret = urun1Fiyat + urun2Fiyat
print("Toplam ödenen ücret :" + str(toplamOdenenUcret))

print("Toplam ödenen KDV :" + str(toplamOdenenUcret * 0.18))


    
