"""
Wykład 7 — slajd „Adnotacje typów”
Plik: 23_adnotacje_typow.py

Adnotacje opisują typy parametrów i wyniku, ale Python ich nie sprawdza podczas działania.
Wywołanie average("abc") podkreśli PyCharm i zgłosi mypy, jednak interpreter je wykona.
"""

def average(values: list[float]) -> float | None:
    """Średnia lub None dla pustej listy."""
    if not values:
        return None
    return sum(values) / len(values)

print(average([4.5, 5.0]), average([]))
print(average.__annotations__)
print(average((3, 4)))      # krotka – działa mimo adnotacji
average("abc")              # Python nie sprawdza typów → błąd w sum


# --- Oczekiwany wynik ----------------------------------------
# 4.75 None
# {'values': list[float], 'return': float | None}
# 3.5
# TypeError: unsupported operand type(s) for +: 'int' and 'str'   <- błąd zamierzony (jak na slajdzie)
