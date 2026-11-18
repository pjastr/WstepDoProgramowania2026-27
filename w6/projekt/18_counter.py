"""
Wykład 6 — slajd „Counter”
Plik: 18_counter.py

Counter: most_common, update, total, działania + i -, test anagramów.
"""

from collections import Counter
c = Counter("mississippi")   # litera → liczność
print(c)
# 2 najczęstsze; brak klucza → 0
print(c.most_common(2), c["z"])
c.update("sip")              # DODAJE liczności
print(c["s"], c.total())
a, b = Counter("aabbbc"), Counter("abd")
print(a - b)                 # bez wyników ≤ 0
print(a + b)
# anagramy: te same liczności liter
print(Counter("listen") == Counter("silent"))


# --- Oczekiwany wynik ----------------------------------------
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# [('i', 4), ('s', 4)] 0
# 5 14
# Counter({'b': 2, 'a': 1, 'c': 1})
# Counter({'b': 4, 'a': 3, 'c': 1, 'd': 1})
# True
