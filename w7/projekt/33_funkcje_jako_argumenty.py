"""
Wykład 7 — slajd „Funkcja jako argument”
Plik: 33_funkcje_jako_argumenty.py

Funkcję można przekazać jak każdy inny obiekt: własne funkcje, wbudowane, lambda.
"""

def apply_all(func, values):     # func – funkcja
    return [func(v) for v in values]

def square(x):
    return x * x

print(apply_all(square, [1, 2, 3]))  # bez ()
print(apply_all(abs, [-1, 2, -3]))
print(apply_all(lambda s: s[::-1], ["ab", "cd"]))
words = ["kot", "Ala", "pies"]
print(sorted(words, key=str.lower))
print(max(words, key=len))
print(list(map(int, "1 2 3".split())))
apply_all(square(2), [1])  # 4 to nie funkcja


# --- Oczekiwany wynik ----------------------------------------
# [1, 4, 9]
# [1, 2, 3]
# ['ba', 'dc']
# ['Ala', 'kot', 'pies']
# pies
# [1, 2, 3]
# TypeError: 'int' object is not callable   <- błąd zamierzony (jak na slajdzie)
