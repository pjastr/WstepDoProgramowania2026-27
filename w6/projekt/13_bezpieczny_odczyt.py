"""
Wykład 6 — slajd „Bezpieczny odczyt”
Plik: 13_bezpieczny_odczyt.py

Bezpieczny odczyt ze słownika: in, get, setdefault — i pułapka z `or`.
"""

stock = {"apple": 5, "pear": 0}
item = "plum"
if item in stock:                  # najpierw sprawdź
    print(stock[item])             # tu się nie wykona
# get: wartość albo None / wartość domyślna
print(stock.get(item), stock.get(item, 0))
# pułapka: 0 jest fałszywe, więc działa „or”
print(stock.get("pear") or "unknown")
# setdefault wstawia tylko, gdy klucza brak
print(stock.setdefault("plum", 10),
      stock.setdefault("apple", 10))
print(stock)


# --- Oczekiwany wynik ----------------------------------------
# None 0
# unknown
# 10 5
# {'apple': 5, 'pear': 0, 'plum': 10}
