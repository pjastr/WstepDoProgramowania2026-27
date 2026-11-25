"""
Wykład 7 — slajd „Studium: szukamy błędu debugerem”
Plik: 40_studium_debug.py

Drugie wywołanie zwraca za dużo nazwisk. Postaw punkt przerwania w pierwszym wierszu
top_students, uruchom Debug i porównaj zmienną result przy obu wywołaniach.
"""

def mean(xs):
    return sum(xs) / len(xs)

def top_students(grades, n=3, result=[]):
    ranking = sorted(grades, reverse=True,
                     key=lambda s: mean(grades[s]))
    for name in ranking[:n]:
        result.append(name)
    return result

g1 = {"Ala": [5, 4], "Jan": [3, 3], "Ola": [4, 5, 5]}
g2 = {"Ewa": [5], "Piotr": [2, 3]}
print(top_students(g1, 2))
print(top_students(g2, 1))      # oczekiwane ['Ewa']


# --- Oczekiwany wynik ----------------------------------------
# ['Ola', 'Ala']
# ['Ola', 'Ala', 'Ewa']
