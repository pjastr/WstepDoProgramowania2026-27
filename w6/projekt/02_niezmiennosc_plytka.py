"""
Wykład 6 — slajd „Niezmienność jest płytka”
Plik: 02_niezmiennosc_plytka.py

Niezmienność krotki jest „płytka”: krotki nie da się zmienić, ale lista
w jej wnętrzu — tak. Ostatnia operacja na u[1] i zgłasza błąd, i zmienia listę.
"""

t = ("ab", [1, 2])
t[1].append(3)          # zmienia się lista WEWNĄTRZ krotki
print(t)
u = t                   # u i t wskazują ten sam obiekt
t += ("c",)             # nowa krotka; u nadal wskazuje starą
print(t, u, t is u)
try:                    # przechwytujemy błąd (try/except – później)
    u[1] += [4]         # najpierw lista rośnie, potem przypisanie → błąd
except TypeError as e:
    print("TypeError:", e)
print(u)                # lista jednak urosła!


# --- Oczekiwany wynik ----------------------------------------
# ('ab', [1, 2, 3])
# ('ab', [1, 2, 3], 'c') ('ab', [1, 2, 3]) False
# TypeError: 'tuple' object does not support item assignment
# ('ab', [1, 2, 3, 4])
