"""
Wykład 6 — slajd „Iterowanie po słowniku”
Plik: 15_iterowanie_slownik.py

Iterowanie po słowniku: klucze, values(), items(), sortowanie.
"""

scores = {"Ola": 4.5, "Jan": 3.0, "Ewa": 5.0}
print(*scores)                        # klucze
# values() – same wartości
mean = sum(scores.values()) / len(scores)
print(f"{mean:.2f}")
# items() – pary (klucz, wartość)
for name, score in scores.items():
    print(f"{name:<4}{score:>4}")
print(*sorted(scores))                # klucze A–Z
print(*sorted(scores.values(), reverse=True))


# --- Oczekiwany wynik ----------------------------------------
# Ola Jan Ewa
# 4.17
# Ola  4.5
# Jan  3.0
# Ewa  5.0
# Ewa Jan Ola
# 5.0 4.5 3.0
