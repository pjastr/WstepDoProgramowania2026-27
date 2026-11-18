"""
Wykład 6 — slajd „Moduł array — tablica jednego typu”
Plik: 24_array.py

Moduł array: tablica wartości jednego typu, zwarta w pamięci.

Uwaga: rozmiary w bajtach zależą od wersji Pythona.
"""

from array import array
from sys import getsizeof
a = array("i", [3, 1, 4])        # "i" – C int (4 B)
a.extend(range(5, 8))
print(a, a[1:3], a.itemsize, sum(a))    # wycinek to też array
nums = list(range(10_000))
# lista referencji kontra zwarty blok liczb
print(getsizeof(nums), getsizeof(array("i", nums)))
b = array("b", [100])            # "b" – signed char: −128…127
b[0] += 100                      # 200 się nie mieści → OverflowError


# --- Oczekiwany wynik ----------------------------------------
# array('i', [3, 1, 4, 5, 6, 7]) array('i', [1, 4]) 4 26
# 80056 40080
# OverflowError: signed char is greater than maximum   <- błąd zamierzony (jak na slajdzie)
