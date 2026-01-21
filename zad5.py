import json
import os


def dodaj_pracownika(nazwa_pliku='employees.json'):
    if os.path.exists(nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            try:
                pracownicy = json.load(plik)
            except json.JSONDecodeError:
                pracownicy = []
    else:
        pracownicy = []
    print("--- Dodawanie nowego pracownika ---")
    name = input("Podaj imię i nazwisko : ")
    age = input("Podaj wiek pracownika : ")
    department = input("Podaj stanowisko pracownika: ")
    salary = input("Podaj zarobki pracownika: ")

    nowy_pracownik = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary,
    }

    pracownicy.append(nowy_pracownik)

    with open(nazwa_pliku, 'w',) as plik:
        json.dump(pracownicy, plik, indent=4)

    print(f"\nSukces! Pracownik {name} został dodany do pliku.")


dodaj_pracownika()