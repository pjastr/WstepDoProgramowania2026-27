"""
Wykład 6 — slajd „Studium: częstość słów”
Plik: 34_czestosc_slow.py

Studium: częstość słów w tekście (normalizacja + Counter).
"""

from collections import Counter
text = """Ala ma kota. Kot ma Alę!
A kota ma też Ola, i Ola ma psa."""
# podział na słowa, interpunkcja z brzegów precz, małe litery
words = [w.strip(".,!?").lower() for w in text.split()]
counts = Counter(words)
print(len(words), len(counts))           # wszystkie słowa / różne słowa
for word, n in counts.most_common(3):
    print(f"{word:<5}{n:>2} {'*' * n}")  # prosty wykres z gwiazdek
# słowa występujące dokładnie raz, alfabetycznie
print(sorted(w for w, n in counts.items() if n == 1))


# --- Oczekiwany wynik ----------------------------------------
# 15 10
# ma    4 ****
# kota  2 **
# ola   2 **
# ['a', 'ala', 'alę', 'i', 'kot', 'psa', 'też']
