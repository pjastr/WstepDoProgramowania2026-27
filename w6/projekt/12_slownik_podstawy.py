"""
Wykład 6 — slajd „Słownik — podstawy”
Plik: 12_slownik_podstawy.py

Słownik: tworzenie, wstawianie, aktualizacja, test `in` (tylko klucze).
"""

ages = {"Ala": 20, "Olek": 22}  # klucz: wartość
ages["Ewa"] = 19            # wstawienie
ages["Ala"] += 1            # aktualizacja
print(ages, len(ages))
# in sprawdza tylko KLUCZE
print("Ewa" in ages, 19 in ages)
# trzy inne sposoby tworzenia słownika
pairs = dict(zip(["x", "y"], [1, 2]))
print(pairs, dict(a=1), dict([("k", 0)]))
print(ages["Zosia"])        # brak klucza → KeyError


# --- Oczekiwany wynik ----------------------------------------
# {'Ala': 21, 'Olek': 22, 'Ewa': 19} 3
# True False
# {'x': 1, 'y': 2} {'a': 1} {'k': 0}
# KeyError: 'Zosia'   <- błąd zamierzony (jak na slajdzie)
