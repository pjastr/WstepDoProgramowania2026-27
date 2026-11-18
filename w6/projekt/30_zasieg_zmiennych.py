"""
Wykład 6 — slajd „Zasięg zmiennych w wyrażeniach”
Plik: 30_zasieg_zmiennych.py

Zasięg zmiennych w wyrażeniach, operator := oraz lambda w pętli.
"""

x = "outer"
squares = [x * x for x in range(4)]
print(x)                   # wyrażenie: własny zasięg
for x in range(4):
    pass
print(x)                   # zmienna pętli zostaje
total = 0
# := zapisuje do zmiennej na zewnątrz
running = [total := total + n for n in [5, 1, 4]]
print(running, total)
# lambda pamięta zmienną i, nie wartość
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
# i=i zamraża wartość w argumencie domyślnym
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])


# --- Oczekiwany wynik ----------------------------------------
# outer
# 3
# [5, 6, 10] 10
# [2, 2, 2]
# [0, 1, 2]
