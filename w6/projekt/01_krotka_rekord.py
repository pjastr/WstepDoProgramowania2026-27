"""
Wykład 6 — slajd „Krotka jako rekord”
Plik: 01_krotka_rekord.py

Krotka jako rekord: funkcja zwracająca kilka wartości, rozpakowanie
(także zagnieżdżone) oraz metody count i index.
"""

def min_max(xs):
    return min(xs), max(xs)    # jedna krotka

lo, hi = min_max([4, 9, 1, 7])  # rozpakowanie
# rekord: (nazwisko, (ocena1, ocena2))
students = [("Nowak", (4, 5)), ("Kowalska", (5, 3))]
# wzorzec po lewej odtwarza strukturę danych
for name, (first, second) in students:
    print(f"{name}: {first + second}")
print(lo, hi, min_max("python"))  # min/max liter
t = (1, 2, 1, 1)
# ile jedynek, gdzie pierwsza 2, powtórzenie
print(t.count(1), t.index(2), t * 2)


# --- Oczekiwany wynik ----------------------------------------
# Nowak: 9
# Kowalska: 8
# 1 9 ('h', 'y')
# 3 1 (1, 2, 1, 1, 1, 2, 1, 1)
