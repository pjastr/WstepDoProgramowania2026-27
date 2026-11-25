"""
Wykład 7 — slajd „Pełna sygnatura — kolejność parametrów”
Plik: 20_pelna_sygnatura.py

Wszystkie rodzaje parametrów w jednej funkcji; inspect.signature pokazuje sygnaturę.
"""

import inspect

def demo(a, b, /, c, d=4, *args, e, g=6, **kwargs):
    print(a, b, c, d, args, e, g, kwargs)

demo(1, 2, 3, e=5)
demo(1, 2, c=3, e=5, z=0)
demo(1, 2, 3, 4, 7, 8, e=5, g=9)
print(inspect.signature(demo))
print(inspect.signature(sorted))


# --- Oczekiwany wynik ----------------------------------------
# 1 2 3 4 () 5 6 {}
# 1 2 3 4 () 5 6 {'z': 0}
# 1 2 3 4 (7, 8) 5 9 {}
# (a, b, /, c, d=4, *args, e, g=6, **kwargs)
# (iterable, /, *, key=None, reverse=False)
