import numpy as np
#1
new_tab = np.arange(100, 109,1)
print(new_tab[2:5])
#2
tab_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(tab_2d[1,:])
print(tab_2d[1,2])


#3
tab = np.array([4, 8, 15, 16, 23, 42])
print(np.sum(tab))
print(np.mean(tab))
print(np.median(tab))

filtrowanie = tab[tab>10]
print(filtrowanie)
#4

data = np.random.rand(10)
print(np.max(data))
print(np.min(data))


#5
tab = np.arange(12)
tab_reshaped = tab.reshape(3, 4)
print(tab_reshaped)



############# PANDAS ############
print("--------------------")


# Tworzenie Series

import pandas as pd
ser = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(ser)

# Tworzenie DataFrame z słownika
data = {
    "imie": ["Jan", "Anna", "Kasia"],
    "wiek": [28, 22, 35],
    "miasto": ["Warszawa", "Kraków", "Gdańsk"]
}
df = pd.DataFrame(data)
print(df)

print("Pierwsze wiersze:\n", df.head())
print("Ostatnie wiersze:\n", df.tail())
print("Informacje o DataFrame:\n", df.info())
print("Statystyki:\n", df.describe())
# 1
data = {
    "imie": ["Radek","Robert","Igor","Szymon"],
    "ocena": [2, 2, 2,5],
    "miasto":["Brodnica","Malbork","Kozieglowy","Swiebodzin"],

}
df = pd.DataFrame(data)
print(df)
print("Srednia ocena :", df["ocena"].mean())
print("Najlepsza ocena:", df["ocena"].max())


#2
print(df["ocena"])

#3

wieksza = df[df["ocena"] > 3.5]
print(wieksza)


#4
print("Średnia ocena:", df["ocena"].mean())

#5


df['status'] = 'niezaliczony'
df.loc[df['ocena'] > 3.0, 'status'] = 'zaliczony'