#11
liste =["gülcihan", 46]
print(type(liste)) """ # liste yapısı  <class 'list'>

demet1 = ("gülcihan") # str yapıda <class 'str'>

demet2 =("gülcihan", 46) # demet yapıda <class 'tuple'> 
print(type(demet2))
# demetler birleştirilemez, değiştirilemez, üzerinde işlem yapılmaz


# kümeler 12
# indekslenemez , tekrarlı eleman olamaz, süslü parantezle gösterilir
# metotlar olmadan değişiklik yapılmaz
küme ={"gülcihan", 46}
print(type(küme)) # <class 'set'>
küme2 = set() # boş küme oluşturma
print(küme2) # set() """

# veri  tiplerini dönüştürme 13

a =2 
b=2.6
c="24"

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'str'>

d = str(a) # int to str
print(d+c) # 224
print(type(d)) # <class 'str'>

e = int(b) # float to int
print(type(e)) # <class 'int'>
print(e+b) # 4.6

f = float(c) # str to float
print(type(f)) # <class 'float'>
print(f) # 24.0

x=[1,3,5,7,9]
print(type(x)) # <class 'list'>

y= tuple(x)
print(type(y)) # <class 'tuple'> demet yapısına dönüştürme

z= set(x) 
print(type(z)) # <class 'set'>
print(z) # {1, 3, 5, 7, 9} kümeye dönüştürme


#ınput fonksiyonu 14
x = input("ilk sayıyı giriniz: ")
y = input("ikinci sayıyı giriniz: ")
z=float(x)+float(y)
print("sonuç: " + str(z) )
#tip dönüşümü yapmadan toplama işlemi yapmaz string olarak toplar.

#örnek
çap= input("lütfen dairenin çapını giriniz: ")
yçap = float(çap)/2
Pi =3.14159
Alan= Pi*(yçap*yçap)
print("dairenin alanı: " + str(Alan)) 


#sınıf- nesne- metot -15
x= "merhaba"
print(x.index("e")) #indeks num verir
print(x.count("a")) # kaç tane a harfi bulunuyor? >> 2
print(dir(str))

print(dir(list)) 

# sayısal metotlar -16

x=-2
print(x.__abs__())
print(abs(x))
print(pow(x,3)) # 3.kuvvetini aldı
print(x.__pow__(3)) # 3.kuvvetini aldı

y=15
print(y.__divmod__(2)) # bölen ve kalan

z=4.5
print(z.as_integer_ratio()) # z sayısını yakalayabilmek için bölünmesi gereken sayıları gösteriyor

print(z.is_integer()) # ondalık kısım 0 dan farklı ise false 


#karakter dizleri metodları -17

 x= "     anlaşılır ekonomi" 
y= x.upper()  # lower() tamamını küçük harf yapar
print(y) #ANLAŞILIR EKONOMI

y=x.islower() # tamamı küçük harften veya büyük harften oluşuyorsa true
print(y) # true

y=x.isnumeric() # ifade sayılardan mı oluşuyor bool kont
print(y) # False

z="235"
c = z.isnumeric()
print(c) # True

y= x.isalnum() # sayı yahut alfabe harici her objede False döndürür 
print(y)  # space karakteri bulunduğu için >> False

y=x.capitalize() # cümleninn sadece ilk harfini büyük yapar
print(y)

y=x.title() # cümledeki her kelimenin baş harfini büyük yapar
print(y)

y=x.swapcase() # küçük harfleri büyük, büyük harfleri küçük yapar
print(y)

y=x.strip(" ") # başta ve sondaki boşluk ifadelerini düzenler 
print(y) # baştaki ve sondaki istenmeyen yapıları kaldırabilir

y=x.rstrip("mi")
print(y) #     anlaşılır ekono


d = " merhaba bu bir düzenleme metnidir."
f=d.split(" ") # parçalama işlemi gerçekleştirir
print(f) #['', 'merhaba', 'bu', 'bir', 'düzenleme', 'metnidir.']

f=d.split("b") 
print(f) #[' merha', 'a ', 'u ', 'ir düzenleme metnidir.']

f="*".join(d) # parçalanmış yapıyı birleştirme
print(f) #  *m*e*r*h*a*b*a* *b*u* *b*i*r* *d*ü*z*e*n*l*e*m*e* *m*e*t*n*i*d*i*r*.

f=d.find("bu") # bu ifadesinin bulunduğu indeks num verir
print(f) #9  eğer aranılan ifade bulunamasaydı -1 dönecekti

f=d.replace("düzenleme", "tanımlama")
print(f)  # merhaba bu bir tanımlama metnidir.

adı= "behçet"
soyadı= "kaya"
görevi ="emekli"
bilgiler =[adı,soyadı,görevi]

print("kişinin adı:{} ,kişinin soyadı:{} ,kişinin görevi:{}"
      .format(bilgiler[0],bilgiler[1],bilgiler[2])) 
#kişinin adı:behçet ,kişinin soyadı:kaya ,kişinin görevi:emekli


# liste metotları -18
liste=[1,2,5,"merhaba",2.5]
liste.append("anlaşılır ekonomi") # başka bir ifadeye atama yapmaz sadece kendi içinde yapar
print(liste) #[1, 2, 5, 'merhaba', 2.5, 'anlaşılır ekonomi']

liste.insert(3,"bugün") # 3. indise ekle
print(liste) #[1, 2, 5, 'bugün', 'merhaba', 2.5, 'anlaşılır ekonomi']

liste.remove(2) #değeri gördüğünde siler
print(liste) #[1, 5, 'bugün', 'merhaba', 2.5, 'anlaşılır ekonomi']

liste.pop(5) # indis değerindeki ifadeyi siler
print(liste) #[1, 5, 'bugün', 'merhaba', 2.5]

liste2=liste.copy()
print(liste2)#[1, 5, 'bugün', 'merhaba', 2.5]


liste3=[1,2,3,4]
liste4=["a","b","c","d"]
liste3.extend(liste4)
print(liste3) #[1, 2, 3, 4, 'a', 'b', 'c', 'd']

liste5=[9,6,3,8,1,7,1,9,5]
liste5.sort()
print(liste5) #[1, 1, 3, 5, 6, 7, 8, 9, 9]

liste5.sort(reverse=True)
print(liste5) #[9, 9, 8, 7, 6, 5, 3, 1, 1]

liste5.reverse() #listeyi tersten yazdırıyor
print(liste5) #[1, 1, 3, 5, 6, 7, 8, 9, 9]

liste5.clear()
print(liste5) #[]

#demet metotları -19

x = (1,1,"Merhaba",2.5)
print(x.index(2.5)) # 2.5 verisinin kaçıncı indekste olduğunu yazdıran metot.
#.count(2.5) metodu ise bize 2.5 verisinden demetimizde kaç tane olduğunu yazdıracak.


#sözlük metotları -20
Bilgi ={
    "Ad":"anlaşılır",
    "soyad":"ekonomi",
    "dyer":"ankara",
    "Tcno":12345
}
print(Bilgi) # {'Ad': 'anlaşılır', 'soyad': 'ekonomi', 'dyer': 'ankara', 'Tcno': 12345}
print(Bilgi.values()) # dict_values(['anlaşılır', 'ekonomi', 'ankara', 12345])
print(Bilgi.items()) #([('Ad', 'anlaşılır'), ('soyad', 'ekonomi'), ('dyer', 'ankara'), ('Tcno', 12345)])
print(Bilgi.get("Ad")) # anlaşılır
Bilgi.update({"cinsiyet":"erkek"})
print(Bilgi) # {'Ad': 'anlaşılır', 'soyad': 'ekonomi', 'dyer': 'ankara', 'Tcno': 12345, 'cinsiyet': 'erkek'}
print(Bilgi.__len__()) #5
Bilgi.pop("Tcno")
print(Bilgi) # {'Ad': 'anlaşılır', 'soyad': 'ekonomi', 'dyer': 'ankara', 'cinsiyet': 'erkek'}
# copy ve clear metodu da kullanılabilir
