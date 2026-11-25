"""
Wykład 7 — slajd „global — zapis do zmiennej modułu”
Plik: 28_global.py

Deklaracja global pozwala przypisać wartość zmiennej modułu wewnątrz funkcji.
"""

calls = 0

def tracked_square(x):
    global calls        # calls – zmienna modułu
    calls += 1
    return x * x

for i in range(3):
    tracked_square(i)
print(calls)

def set_mode():
    global mode         # może utworzyć zmienną
    mode = "debug"

set_mode()
print(mode)


# --- Oczekiwany wynik ----------------------------------------
# 3
# debug
