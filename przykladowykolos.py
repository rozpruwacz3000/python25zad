import csv
import random
import json
import numpy as np

# --- SEKCJA KLASY (Zadania 1-4) ---

class DailyFoodIntake:
    def __init__(self, day):
        # ZAD 1: Sprawdzenie typu i zakresu
        if not isinstance(day, int) or not (1 <= day <= 7):
            raise ValueError("Dzien musi byc liczba calkowita od 1 do 7")

        self.day = day
        self.kcal = 0.0  # float
        self.count = 0   # int

    # ZAD 2: Metoda dodająca posiłek
    def add_meal(self, meal_kcal):
        self.kcal += float(meal_kcal)
        self.count += 1

    # ZAD 3: Sformatowana informacja
    def get_info(self):
        days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
                5: "Friday", 6: "Saturday", 7: "Sunday"}
        day_name = days[self.day]
        return f"Daily Food intake for {day_name} is {self.kcal} kcal, {self.count} meals"

    # ZAD 4: Zrzut danych do listy
    def dump(self):
        return [self.day, self.kcal, self.count]

# --- SEKCJA FUNKCJI WOLNYCH (Zadanie 6) ---

def save(objects_list, filename="data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for obj in objects_list:
            writer.writerow(obj.dump())

# --- SEKCJA LOGIKI (Zadanie 5) ---

intakes = []
for r in range(50):
    random_day = random.randint(1, 7)
    obj = DailyFoodIntake(random_day)

    # Losowanie liczby posiłków od 3 do 10
    num_meals = random.randint(3, 10)
    for _ in range(num_meals):
        # Losowanie kalorii od 100 do 1000
        meal_kcal = random.uniform(100, 1000)
        obj.add_meal(meal_kcal)

    intakes.append(obj)

# Zapis do pliku CSV
save(intakes)

# --- SEKCJA ANALIZY (Zadanie 7) ---

# Wczytanie z pliku (używamy separatora przecinka)
data = np.genfromtxt('data.csv', delimiter=',')

# PAMIĘTAJ: data[:, X] wybiera całą kolumnę o indeksie X
average_kcal = np.mean(data[:, 1])        # Średnia z kolumny kcal (indeks 1)
median_meals = np.median(data[:, 2])      # Mediana z kolumny count (indeks 2)
saturdays_count = np.sum(data[:, 0] == 6) # Suma wystąpień soboty (indeks 0)

print(f"Srednia kcal: {average_kcal:.2f}")
print(f"Mediana posilkow: {median_meals}")
print(f"Liczba sobot w danych: {int(saturdays_count)}")

# --- SEKCJA EKSPORTU (Zadanie 8) ---

results = {
    "average_kcal": float(average_kcal),
    "median_meals": float(median_meals),
}

with open('stats.json', 'w') as file:
    json.dump(results, file, indent=4)

print("Statystyki zostaly zapisane do stats.json!")