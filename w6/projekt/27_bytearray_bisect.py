"""
Wykład 6 — slajd „Inne kontenery — przegląd”
Plik: 27_bytearray_bisect.py

bytearray (modyfikowalne bajty) i bisect (wyszukiwanie w posortowanej liście).
"""

import bisect
buf = bytearray(b"Py\x00\xff")  # 4 bajty
buf[0] = ord("p")               # można zmieniać
grades = [2, 3, 3.5, 4, 4.5, 5]  # posortowana!
print(list(buf), bytes(buf))
# miejsce wstawienia 4 (przed istniejącą 4)
print(bisect.bisect_left(grades, 4))


# --- Oczekiwany wynik ----------------------------------------
# [112, 121, 0, 255] b'py\x00\xff'
# 3
