"""
Wykład 7 — slajd „Docstring i help()”
Plik: 05_docstring.py

Docstring jako dokumentacja funkcji: __doc__, help(), przykład w stylu doctest.
Przykład z docstringu można sprawdzić poleceniem:  python -m doctest -v 05_docstring.py
"""

def clamp(x, lo, hi):
    """Ogranicz x do przedziału [lo, hi].

    >>> clamp(15, 0, 10)
    10
    """
    return max(lo, min(x, hi))

print(clamp(-3, 0, 10), clamp(5, 0, 10))
print(clamp.__doc__.splitlines()[0])
help(clamp)                 # pełny opis


# --- Oczekiwany wynik ----------------------------------------
# 0 5
# Ogranicz x do przedziału [lo, hi].
# Help on function clamp in module __main__:
#
# clamp(x, lo, hi)
#     Ogranicz x do przedziału [lo, hi].
#
#     >>> clamp(15, 0, 10)
#     10
