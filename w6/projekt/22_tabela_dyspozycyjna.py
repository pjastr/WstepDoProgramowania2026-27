"""
Wykład 6 — slajd „Słownik zamiast if/elif”
Plik: 22_tabela_dyspozycyjna.py

Tabela dyspozycyjna: słownik symbol → funkcja zamiast łańcucha if/elif.
"""

import operator
# tabela dyspozycyjna: symbol → funkcja
OPS = {"+": operator.add, "-": operator.sub,
       "*": operator.mul, "/": operator.truediv,
       "max": max}

def calc(a, op, b):
    f = OPS.get(op)          # szukamy funkcji
    if f is None:
        return f"unknown operator {op!r}"
    return f(a, b)           # wywołujemy ją

print(calc(6, "*", 7), calc(1, "/", 4), calc(3, "max", 8))
print(calc(2, "^", 3))


# --- Oczekiwany wynik ----------------------------------------
# 42 0.25 8
# unknown operator '^'
