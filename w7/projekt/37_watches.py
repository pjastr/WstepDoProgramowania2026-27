"""
Wykład 7 — slajd „Obserwowanie wyrażeń: Watches i Evaluate”
Plik: 37_watches.py

Funkcja z błędem: dla [9, 2, 5] zwraca 9 zamiast 5. Dodaj do Watches first, second,
x > second i prześledź pętlę; Evaluate Expression (Alt+F8): sorted(xs)[-2].
"""

def second_largest(xs):
    first = second = xs[0]
    for x in xs[1:]:
        if x > first:
            second = first
            first = x
        elif x > second:
            second = x
    return second

print(second_largest([3, 1, 4, 1, 5]))  # 4 – dobrze
print(second_largest([9, 2, 5]))        # oczekiwane 5


# --- Oczekiwany wynik ----------------------------------------
# 4
# 9
