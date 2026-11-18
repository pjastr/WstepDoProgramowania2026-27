"""
Wykład 6 — slajd „deque — kolejka dwustronna”
Plik: 25_deque.py

deque — kolejka dwustronna; maxlen jako bufor cykliczny.
"""

from collections import deque
q = deque([1, 2, 3])
q.append(4)                     # na prawy koniec
q.appendleft(0)                 # na lewy koniec
print(q.popleft(), q.pop(), q)  # zdejmujemy z obu końców
q.rotate(1)                     # przesunięcie cykliczne w prawo
print(q, q[0])
last = deque(maxlen=3)          # 3 najnowsze elementy
for line in ["a", "b", "c", "d", "e"]:
    last.append(line)           # przy pełnej kolejce wypada najstarszy
print(last, list(last))


# --- Oczekiwany wynik ----------------------------------------
# 0 4 deque([1, 2, 3])
# deque([3, 1, 2]) 3
# deque(['c', 'd', 'e'], maxlen=3) ['c', 'd', 'e']
