"""
Wykład 7 — slajd „Zmienne lokalne”
Plik: 24_zmienne_lokalne.py

Parametry i zmienne przypisane w funkcji są lokalne — powstają przy każdym wywołaniu
i znikają po jego zakończeniu.
"""

def area(r):
    pi = 3.14159            # pi, result, r – zmienne lokalne
    result = pi * r * r
    print(locals())         # słownik zmiennych lokalnych
    return result

print(round(area(2), 2))
print(round(area(1), 2))    # każde wywołanie – nowe zmienne
print(result)               # poza funkcją nie istnieje → błąd


# --- Oczekiwany wynik ----------------------------------------
# {'r': 2, 'pi': 3.14159, 'result': 12.56636}
# 12.57
# {'r': 1, 'pi': 3.14159, 'result': 3.14159}
# 3.14
# NameError: name 'result' is not defined   <- błąd zamierzony (jak na slajdzie)
