"""
Wykład 7 — slajd „Parametry tylko nazwane i tylko pozycyjne”
Plik: 19_tylko_nazwane.py

Po * parametry można podać tylko nazwą; przed / — tylko pozycyjnie.
"""

def split_bill(total, people, *, tip=0.0):  # po * – tylko nazwane
    return round(total * (1 + tip) / people, 2)

def distance(x1, y1, x2, y2, /):            # przed / – tylko pozycyjne
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(split_bill(200, 3), split_bill(200, 3, tip=0.1))
print(distance(0, 0, 3, 4))
print(sorted([3, 1, 2], reverse=True))  # key, reverse – tylko nazwane
split_bill(200, 3, 0.1)                 # co znaczy 0.1? → błąd


# --- Oczekiwany wynik ----------------------------------------
# 66.67 73.33
# 5.0
# [3, 2, 1]
# TypeError: split_bill() takes 2 positional arguments but 3 were given   <- błąd zamierzony (jak na slajdzie)
