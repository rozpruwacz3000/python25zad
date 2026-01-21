# # variable_int_1 =10
# # variable_int_2 =20 #w taki sposob tworzymy zmienna, typy musza byc takie same!
# # variable_int_1 + variable_int_2
# #
# # variable_int_3 =10
# # variable_string_1 = "abc"
# # #variable_int_3 + variable_string_1 ## to sie nie wykona bo mamy niezgodnosc typow!:P
# #
# # print(type(42)) # w ten sposob sprawdzamy jakiego typu jest okreslona zmienna:P
#
# #ZAD1 SPRAWDZ TYPY ZMIENNYCH
# a = 10
# b = "Text"
#
# print(type(a))
# print(type(b))
#
# c=str(a) # zmieniam typ zmiennej na string (kontrowersja typow)
# print(c)
#
#
# ### DZIALANIA NA LICZBACH
# # + -> dodawanie, - -> odejmowanie, * -> mnozenie, / -> dzielenie , // -> dzielenie z reszta, % -> reszta z dzielenia, ** -> potegowanie.
# d= 77
# e = 10
# f = 0.10001
#
# x = e/f   #dzielenie
# y = e//f #dzielenie calkowite
# print(x)
# print(y)
#
#
# #Operacje na znakach ciaglych
#
#
# my_text = 'Tekst'
# print(len(my_text)) # zwraca dlugosc tekstu
#
#
# ###
#
# #'text' - text w pojedynczej lini (tak samo jak "text")
# # """text""" - text w wielu liniach
#
# j = 'Test_1;Test_2'
# k = j.split(';') #separuje tekst wzgledem znaku w nawiasach
# print(k)
#
#
#
# #####Obsluga wejsca/wyjscia####
#
# first_number =input("Podaj pierwsza liczbe: ")
# second_number = int(input("Podaj druga liczbe: "))
# first_number = int(first_number) ## rzutowanie --> zmieniam typ na int
#
# print('Suma liczb: ' + str(first_number + second_number))
#
#
# third_number = input("Podaj ciag znakow:")
# fourth_number = input("Podaj drugI ciag znakow:")
#
# print('Polaczony ciag znakow: ' + str(third_number + fourth_number))

# #ZAD 8
# a = int(input("Podaj pierwsza liczbe: "))
# b = int(input("Podaj druga liczbe: "))
#
# print("Dzielenie calkowite liczby a przez b  " + str(a/b))
# print("Reszta z tego dzielenia: " + str(a % b))
# ZAD 7

# c = int(input("Podaj podstawe potegi: "))
# d = int(input("Podaj wykladnik potegi:"))
# e = c ** d
# print("Wynik potegowania wynosi " +str(e))



# #Zadania powtorkowe!
# #ZAD1Napisz program, który wczytuje od użytkownika ciąg liczb oddzielonych spacjami,
# # a następnie konwertuje go na listę liczb całkowitych i wyświetla tę listę.
#
# wejscie = input("Podaj liczby oddzielone spacjami: ")
# liczby = [int(x) for x in wejscie.split()]
# print(liczby)
#
# #ZAD2 Stwórz listę zawierającą 5 dowolnych kolorów (zapisanych jako łańcuchy znakowe).
# # Następnie, poproś użytkownika o podanie nazwy koloru i sprawdź, czy znajduje się on na liście.
#
#
# # kolory = ["czerwony","niebieski","zielony","zolty","czarny"]
# # wybor = input("Podaj kolor: ").lower()
# # print(f"Czy jest na liscie? {wybor in kolory}")
# #
# # #ZAD3 Napisz program, który wczytuje od użytkownika dwie liczby całkowite i wyświetla ich sumę,
# # # różnicę, iloczyn i iloraz (z obsługą dzielenia przez zero).
# #
# # liczba_1 = int(input("Podaj liczbe calkowita: "))
# # liczba_2 = int(input("Podaj druga liczbe calkowita: "))
# # suma = liczba_1 + liczba_2
# # roznica = liczba_1 - liczba_2
# # iloczyn = liczba_1 * liczba_2
# #
# # if liczba_2 != 0:
# #     iloraz = liczba_1 / liczba_2
# #     print(iloraz)
# # else:
# #     print("Nie dziel przez zero")
# #
# # print(suma)
# # print(roznica)
# # print(iloczyn)
#
# #ZAD4Za pomocą instrukcji warunkowej if-elif-else napisz program, który sprawdza,
# # czy podana przez użytkownika liczba jest dodatnia, ujemna, czy równa zero.
#
#
# number_1 = int(input("Podaj liczbe: "))
# if number_1 > 0:
#     print(f"{number_1}  jest dodatnia!")
# elif number_1 == 0:
#     print(f"{number_1}  jest rowna 0")
# elif number_1 < 0:
#     print(f"{number_1}  jest ujemna!")
#
#
# #ZAD5 Napisz program, który wczytuje od użytkownika ciąg znaków i wyświetla go w odwrotnej kolejności.
#
#
# ciag_znakow= str(input("Podaj ciag znakow:"))
# print(ciag_znakow[::-1])


#ZAD6 Napisz program, który wczytuje od użytkownika zdanie i wyświetla liczbę słów w tym zdaniu.

#
# zdanie = input("Podaj zdanie: ")
# print(f"Liczba słów: {len(zdanie.split())}")
#
#
# #ZAD7Stwórz słownik, w którym kluczami będą imiona, a wartościami odpowiadającymi im wiek osób.
# # Następnie wyświetl imię i wiek najstarszej osoby.
# imiona = {"Szymon":19,"Robert":19,"Igor":20,"Radek":21}
# najstarszy = max(imiona, key=imiona.get)
# print(f"Najstarszy: {najstarszy} , wiek: {imiona[najstarszy]}")



#ZAD8 Napisz program, który wczytuje od użytkownika zdanie
#i wyświetla to zdanie z# zamienionymi miejscami pierwszym i ostatnim słowem.
# s = input("Zdanie: ").split()
# if len(s) >1:
#     s[0],s[-1] =s[-1],s[0]
# print("".join(s))


#ZAD9Zdefiniuj klasę bazową Zwierze z metodą daj_glos(),
# która wyświetla komunikat "Dźwięk zwierzęcia"
# Następnie utwórz klasy pochodne Pies i Kot, które nadpisują metodę daj_glos()
# , wyświetlając odpowiednio "Hau hau" i "Miau".
#
# class Zwierze:
#     def daj_glos(self): print("Dzwiek zwierzecia!")
#
#     class Pies(Zwierze):
#         def daj_glos(self): print("Hau hau")
# class Kot(Zwierze):
#     def daj_glos(self): print("Miau")


    #ZAD10 Stwórz klasę Student z atrybutami imie, nazwisko i lista_ocen.
    # Dodaj metodę srednia_ocen(), która oblicza średnią ocen studenta.

# class Student:
#     def __init__(self,imie, nazwisko,oceny):
#         self.imie, self.nazwisko, self.oceny = imie, nazwisko, oceny
#     def srednia_ocen(self):
#         return sum(self.oceny)/len(self.oceny) if self.oceny else 0
#
#
#
#
#  #ZAD11 Napisz funkcję znajdz_slowo(tekst, slowo), która sprawdza,
#  # czy podane słowo znajduje się w tekście. Funkcja powinna zwracać True,
#  # jeśli słowo znajduje  się w tekście, a False w przeciwnym wypadku.
#
#   def znajdz_slowo(tekst,slowo):
#         return slowo in tekst
#
# #ZAD12  Zdefiniuj klasę Kolo z atrybutem promien.
# # Dodaj metody oblicz_pole() i oblicz_obwod().
# # Stwórz obiekt klasy Kolo i przetestuj działanie metod.
#     class Kolo:
#         def __init__(self,promien): self.promien = promien
#         def oblicz_pole(self): return 3.14  * self.promien**2
#         def oblicz_obwod(self): return 2* 3.14 * self.promien

#ZAD13 Stwórz klasę Pracownik z atrybutami imie, nazwisko i stawka_godzinowa.
# Dodaj metodę oblicz_wynagrodzenie(liczba_godzin),
# która oblicza wynagrodzenie pracownika za przepracowane godziny.

# class Pracownik:
#     def __init__(self,imie,nazwisko,stawka):
#         self.imie, self.nazwisko,  self.stawka = imie,nazwisko,stawka
#     def oblicz_wynagrodzenie(self,h): return h * self.stawka
#
# #ZAD14 Wczytaj zawartość pliku dane.txt
# # (który sam utwórz z danymi w formacie CSV, np. imię,nazwisko,wiek)
# # i zapisz przetworzone dane do pliku wynik.txt, zamieniając przecinki na średniki.
#
#
# with open("dane.txt","r") as f_in, open("wynik.txt","w") as f_out:
#     for linia in f_in:
#         f_out.write(linia.replace(",",";"))
#
# #ZAD15 Napisz funkcję cenzuruj(tekst, zakazane_slowa), która zastępuje wszystkie
# # wystąpienia zakazanych słów (podanych jako lista) w tekście gwiazdkami (***)
# def cenzuruj(tekst,zakazane):
#     slowa = tekst.split()
#     wynik = [("***" if s.strip(".,")in zakazane else s) for s in slowa]
#     return " ".join(wynik)

#ZAD16Stwórz słownik, w którym kluczami są nazwy produktów,
# a wartościami ich ceny. Następnie oblicz i wyświetl
# sumaryczną wartość koszyka zakupów.

# koszyk = {"Chleb":4.5,"Mleko":3.2,"Ser":12.0}
# print(f"Suma:{sum(koszyk.values())})

#ZAD17  Napisz program, który wczytuje od użytkownika zdanie
# i wypisuje słowa w zdaniu w kolejności od najdłuższego do najkrótszego.

# zdanie = input("Zdanie: ").split()
# print(sorted(zdanie, key = len, reverse=True))

#ZAD18 Napisz program, który wyświetla liczby od 1 do 20,
# ale zamiast liczb podzielnych przez 3 wyświetla słowo "Fizz",
# zamiast liczb podzielnych przez 5 wyświetla "Buzz",
# a zamiast liczb podzielnych przez 3 i 5 wyświetla "FizzBuzz".

# for i in range(1,21):
#     if i % 15 == 0: print("FizzBuz")
#     if i % 5 == 0: print("Buz")
#     if i % 3 == 0: print("Fizz")
#     else: print(i)

#ZAD19 Wczytaj zawartość pliku tekst.txt
# (sam utwórz plik i umieść w nim przykładowy tekst) do zmiennej.
# Następnie wyświetl liczbę linii, słów i znaków w tym pliku.

# with open("tekst.txt","r") as f:
#     content = f.read()
#     f.seek(0)
#     linie = f.readlines()
# print(f"Linie: {len(linie)},Slowa: {len(content.split())}, Znaki: {len(content)}")


#ZAD20Zdefiniuj klasę Bilet z atrybutami: miejsce, rząd, cena.
# Napisz metodę wyświetlającą pełną informację o bilecie.
# Następnie zdefiniuj klasę BiletVIP, która dziedziczy z Bilet,
# ale ma dodatkowy atrybut strefa_vip (np. 'Złota', 'Platynowa') i
# odpowiednio modyfikuje sposób wyświetlania informacji (np. dopisując strefa_vip).

#
# class Bilet:
#     def __init__(self,miejsce,rzad,cena):
#         self.miejsce,self.rzad,self.cena = miejsce,rzad,cena
#
#     def info(self):
#         return f"M: {self.miejsce},R: {self.rzad},C: {self.cena}"
#
# class BiletVIP(Bilet):
#     def __init__(self,miejsce,rzad,cena,strefa):
#         super().__init__(miejsce,rzad,cena)
#         self.strefa = strefa
#     def info(self):
#         return super().info() + f",Strefa: {self.strefa}"


#ZAD21 Zdefiniuj klasę Punkt z atrybutami x i y.
# Dodaj metodę odleglosc(inny_punkt),
# która oblicza odległość między dwoma punktami.

# class Punkt:
#     def __init(self,x,y):
#         self.x = x
#         self.y = y
#     def odleglosc(self,p):
#         return ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
#ZAD 22 Napisz program, który wczyta od użytkownika tekst składający się z kilku zdań.
# Następnie policz liczbę słów o tej samej długości w nim występujących. Wynik należy umieścić w słowniku.

# tekst = input("Podaj tekst: ").split()
# staty = {}
# for s in tekst:
#     dl = len(s.strip(".,"))
#     staty[dl] = staty.get(dl,0) + 1
# print(staty)
#ZAD 23 Zdefiniuj klasę Komparator z atrybutami wynik, tekst_1, tekst_2, która będzie porównywała dwa ciągi znakowe.
# Dodaj metodę porownaj(), która zapisze rezultat porównania do atrybutu wynik. Utwórz metodę podaj_wynik(),
# która wyświetli rezultat porównania i odpowiednio go sformatuje (np. {tekst_1} jest identyczny jak {tekst_2}).

class Komparator:
    def __init__(self,t1,t2):
        self.t1 = t1
        self.t2 = t2
        self.wynik = t1,t2, None

    def porownaj(self): self.wynik = (self.t1==self.t2)
    def podaj_wynik(self):
        status = "identyczny jak" if self.wynik else "rozny od"
        print(f"'{self.t1}' jest {status} '{self.t2}'")


#ZAD24 Utwórz macierz 8x8 zawierającą wartości losowe, w tym większe od zera.
# Przekształć ją do struktury słownika i zapisz w formacie JSON.
# Kluczami powinny być frazy zapisane w notacji "val_wiersz_kolumna" (np. "val_0_0").


import random, json
macierz = {}
for r in range(8):
    for c in range(8):
        macierz[f"val_{r}_{c}"] = random.uniform(0,100)
with open("macierz.json", "w") as f:
    json.dump(macierz,f)


#ZAD25  Napisz program, który wczyta od użytkownika pojedynczą liczbę N,
# a następnie wygeneruje listę wartości 50, 51, … 5N. Lista powinna zostać zapisana
# do pliku w formacie CSV, gdzie wartości zostaną oddzielone od siebie znakiem myślnika.


N = int(input("Podaj N:"))

lista = [str(x) for x in range(50,50+N)]
with open("wynik.csv", "w") as f:
    f.write("-".join(lista))


