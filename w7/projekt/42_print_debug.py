"""
Wykład 7 — slajd „print, breakpoint() czy debuger?”
Plik: 42_print_debug.py

Szybki podgląd przez print (do usunięcia po poprawce) i wywołanie breakpoint().
Odkomentuj breakpoint(): w trybie Run uruchomi się pdb w konsoli (c – dalej, p n – pokaż n,
q – koniec), w trybie Debug PyCharm zatrzyma się jak na punkcie przerwania.
"""

def digit_sum(n):
    total = 0
    while n > 0:
        print(f"DEBUG {n=} {total=}")  # usuń potem
        total += n % 10
        n //= 10
        # breakpoint()     # pdb lub debuger IDE
    return total

print(digit_sum(4096))


# --- Oczekiwany wynik ----------------------------------------
# DEBUG n=4096 total=0
# DEBUG n=409 total=6
# DEBUG n=40 total=15
# DEBUG n=4 total=15
# 19
