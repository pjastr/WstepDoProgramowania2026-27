"""
Wykład 6 — slajd „Wyrażenia słownikowe — wzorce”
Plik: 29_wyrazenia_slownikowe.py

Typowe wzorce wyrażeń słownikowych: przekształcenie, filtr, odwrócenie, indeks.
"""

prices = {"apple": 2.5, "kiwi": 4.0, "plum": 6.0}
# cena brutto – przekształcamy wartości
gross = {k: round(v * 1.23, 2) for k, v in prices.items()}
# tylko tanie – filtrujemy pary
cheap = {k: v for k, v in prices.items() if v < 5}
# odwrócenie: wartość → klucz
inverse = {v: k for k, v in prices.items()}
# indeks: słowo → pozycja
index = {w: i for i, w in enumerate("to be or not".split())}
# kwadraty liczb nieparzystych
odd_squares = {n: n * n for n in range(1, 6) if n % 2}
print(gross, cheap, sep="\n")
print(inverse, index, odd_squares, sep="\n")


# --- Oczekiwany wynik ----------------------------------------
# {'apple': 3.08, 'kiwi': 4.92, 'plum': 7.38}
# {'apple': 2.5, 'kiwi': 4.0}
# {2.5: 'apple', 4.0: 'kiwi', 6.0: 'plum'}
# {'to': 0, 'be': 1, 'or': 2, 'not': 3}
# {1: 1, 3: 9, 5: 25}
