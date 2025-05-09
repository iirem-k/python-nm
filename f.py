""" x=2+3
print(type(x))
print(x.imag)
print(x.real) """

""" z= "anlaşılır ekonomi"
print(z)
print(z[0])
print(z[0:5])  # 0'dan 5'e kadar olan elemanları alır
print(z[0:5:2])  # 2. ve 3. elemanları alır
print(type(z)) """

""" 
F = "anlaşılır "
G="Ekonomi"
print(F+G)
print(3*F) # * işareti tekrarlama
print(F + "\n" + G)
print(len(F)) # len() fonksiyonu stringin uzunluğunu verir
print(F[len(F)-2]) # son elemanı verir // son elemanı boşluk olduğu için -2 dedim
 """

""" Bilgi = ["Ahmet", "Yıldız", 25,"evli"]
print(Bilgi[0])
Bilgi[0] = "Mehmet" # listenin 0. elemanını değiştirir
print(Bilgi[0])
print(Bilgi)

Bilgi2 = ["Mehmet", "Yıldız", 25,"evli"]
Bilgi3 = [Bilgi ,Bilgi2]
print(len(Bilgi)) # 4 tane eleman var
print(len(Bilgi3)) # 2 tane liste var """

""" ürünler =["televizyon", "buzdolabı","bilgisayar","fırın"]
print(ürünler)
print(len(ürünler)) # 4 tane eleman var
print(ürünler[0:2]) # 0'dan 2'ye kadar olan elemanları alır

print(ürünler[0] ,ürünler[len(ürünler)-1]) # 0. ve son elemanı alır
ürünler[len(ürünler)-1] = "telefon" # 0. elemanı değiştirir

ürünler = ürünler + ["çamaşır makinesi"] # yeni bir eleman ekler
print(ürünler)
print(ürünler[::-1]) # listeyi ters çevirir """

""" Kimlik={"isim": "irem", 
        "soyisim":"kaya",
        "yaş":23}

print(Kimlik) #{'isim': 'irem', 'soyisim': 'kaya', 'yaş': 21}
print(Kimlik["isim"]) # irem

Kimlik["isim"] = "Gülsüm"
print(Kimlik) #{'isim': 'Gülsüm', 'soyisim': 'kaya', 'yaş': 21}

Kimlik["Tc"]=123456 # yeni bir eleman ekler
print(Kimlik) 
 """

# sözlük yapısı
""" kullanicilar ={
    "Ahmetcan":{"TC":31234512, "yaş":34, "D_yeri": "İstanbul",},
    "Mehmetcan":{"TC":8765432, "yaş":65, "D_yeri": "ankara",},
    "Arzucan":{"TC":1234567, "yaş":23, "D_yeri": "İzmir",}
}

print(kullanicilar["Ahmetcan"])
print(kullanicilar["Arzucan"])
 """