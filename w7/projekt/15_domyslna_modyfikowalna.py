"""
Wykład 7 — slajd „Pułapka: modyfikowalna wartość domyślna”
Plik: 15_domyslna_modyfikowalna.py

Wartość domyślna jest obliczana raz — przy def. Lista jako wartość domyślna jest wspólna
dla wszystkich wywołań; poprawny wzorzec to None.
"""

def add_grade(grade, grades=[]):  # jedna lista!
    grades.append(grade)
    return grades

print(add_grade(5))
print(add_grade(3))               # niespodzianka
print(add_grade.__defaults__)     # żyje w funkcji

def add_grade_ok(grade, grades=None):
    if grades is None:
        grades = []               # nowa przy każdym
    grades.append(grade)          # wywołaniu
    return grades

print(add_grade_ok(5), add_grade_ok(3))


# --- Oczekiwany wynik ----------------------------------------
# [5]
# [5, 3]
# ([5, 3],)
# [5] [3]
