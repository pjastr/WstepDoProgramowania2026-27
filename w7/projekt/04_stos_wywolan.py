"""
Wykład 7 — slajd „Wywołanie funkcji — stos ramek”
Plik: 04_stos_wywolan.py

Każde wywołanie tworzy ramkę z własnymi zmiennymi; return usuwa ramkę i oddaje wynik.
Uruchom w trybie Debug z punktem przerwania w funkcji square i obejrzyj panel Frames.
"""

def square(x):
    return x * x

def sum_of_squares(a, b):
    sa = square(a)      # ramka square(x=3)
    sb = square(b)      # rysunek: wewnątrz square(4)
    return sa + sb

def main():
    result = sum_of_squares(3, 4)
    print(result)

main()


# --- Oczekiwany wynik ----------------------------------------
# 25
