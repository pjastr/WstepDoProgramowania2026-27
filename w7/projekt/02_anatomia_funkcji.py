"""
Wykład 7 — slajd „Anatomia funkcji”
Plik: 02_anatomia_funkcji.py

Elementy definicji funkcji: nagłówek, parametry, docstring, ciało, return; wywołanie z argumentami.
"""

def bmi(mass, height):
    """Zwraca wskaźnik BMI: masa [kg] / wzrost² [m]."""
    index = mass / height ** 2
    return index

result = bmi(70, 1.75)      # wywołanie: argumenty 70 i 1.75
print(f"BMI = {result:.1f}")
print(f"BMI = {bmi(90, 1.80):.1f}")


# --- Oczekiwany wynik ----------------------------------------
# BMI = 22.9
# BMI = 27.8
