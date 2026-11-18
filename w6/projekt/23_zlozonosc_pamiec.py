"""
Wykład 6 — slajd „Złożoność i pamięć”
Plik: 23_zlozonosc_pamiec.py

Pamięć zajmowana przez list, tuple, set i dict z tysiącem elementów.

Uwaga: rozmiary w bajtach zależą od wersji Pythona.
"""

import sys
n = 1000
# te same 1000 liczb w czterech kontenerach
for c in [list(range(n)), tuple(range(n)),
          set(range(n)), dict.fromkeys(range(n))]:
    # rozmiar samego kontenera w bajtach
    print(f"{type(c).__name__:6}{sys.getsizeof(c):>6} B")


# --- Oczekiwany wynik ----------------------------------------
# list    8056 B
# tuple   8040 B
# set    32984 B
# dict   36952 B
