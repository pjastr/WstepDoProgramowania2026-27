"""
Wykład 6 — slajd „Zliczanie — trzy sposoby”
Plik: 17_zliczanie.py

Zliczanie wystąpień słów na trzy sposoby: if/else, get, Counter.
"""

words = "to be or not to be".split()
# 1) if / else
c1 = {}
for w in words:
    if w in c1:
        c1[w] += 1
    else:
        c1[w] = 1    # pierwszy raz
# 2) get z domyślnym 0
c2 = {}
for w in words:
    c2[w] = c2.get(w, 0) + 1

# 3) gotowe narzędzie
from collections import Counter
c3 = Counter(words)
print(c1 == c2 == c3)   # wszystkie trzy równe
print(c2)
print(c3)


# --- Oczekiwany wynik ----------------------------------------
# True
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# Counter({'to': 2, 'be': 2, 'or': 1, 'not': 1})
