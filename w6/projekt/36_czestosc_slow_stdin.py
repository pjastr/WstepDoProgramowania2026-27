"""
Wykład 6 — slajd „Ten sam program: częstość słów”
Plik: 36_czestosc_slow_stdin.py

Ten sam program co w C++, C# i Javie: częstość słów czytanych ze standardowego wejścia.

Jak uruchomić: w PyCharmie Run, wpisz tekst w konsoli i zakończ Ctrl+D;
albo w terminalu:  python 36_czestosc_slow_stdin.py < plik.txt
Oczekiwany wynik poniżej — dla wejścia „to be or not to be / that is the question”.
"""

import sys
from collections import Counter

# całe wejście → lista słów → liczniki
counts = Counter(sys.stdin.read().split())
for word, n in sorted(counts.items()):  # A–Z
    print(word, n)


# --- Oczekiwany wynik ----------------------------------------
# be 2
# is 1
# not 1
# or 1
# question 1
# that 1
# the 1
# to 2
