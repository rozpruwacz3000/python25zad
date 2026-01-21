import numpy as np

my_list = [1, 2, 3, 4, 623, 22]
np_table = np.array(my_list)
print(np_table)

tab_0_9 = np.arange(10)
print(tab_0_9)

tab_2d = np.array([[1,2,3],[5,6,7]])
print(tab_2d)

print(tab_2d.shape) # ksztalt
print(tab_2d.dtype) # jakiego typu jest
print(tab_2d.ndim)  # liczba wymiarow

new_tab = np.arange(20, 40,3)
print(new_tab)
print(new_tab[0]) # wyswietl wartosci na indeksie 0
print(new_tab[3:5]) # wyswietl wartosci od indeksu 3 do 5
print(new_tab[:5]) # wyswietl wartosci od indeksu 0 do 5

print(tab_2d[1,1]) # wyswietl wartosc w 1 wierszu i 1 kolumnie
print(tab_2d[:,1]) # wyswietl wartosci we wszystkich wierszach 1 kolumny


tab = np.arange(12)
tab_reshaped = tab.reshape(3, 4) #zmienia ksztalt tablicy (3 wiersze 4 kolumny)
print(tab_reshaped)





tab = np.array([1,2,3])
print(tab+10) # do kazdego elementu tablicy dodaje 10
print(tab *10) # kazdy element tablicy mnoze razy 10
print(np.sum(tab)) # suma elementow
print(np.median(tab)) #mediana elementow
print(np.std(tab)) # odchylenie standardowe elementow


tab = np.arange(10)
filtrowane = tab[tab > 5] #wybieramy elementy wieksze od 5
print(filtrowane)



tab = np.arange(4)
print(tab[[False,True,True,False]])