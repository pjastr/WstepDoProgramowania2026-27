"""
Wykład 6 — slajd „heapq — kolejka priorytetowa”
Plik: 26_heapq.py

heapq — kolejka priorytetowa na zwykłej liście.
"""

import heapq
tasks = []                    # kopiec = zwykła lista
# (priorytet, opis): mniejsza liczba = pilniejsze
heapq.heappush(tasks, (2, "write report"))
heapq.heappush(tasks, (1, "fix bug"))
heapq.heappush(tasks, (3, "coffee"))
print(tasks[0], len(tasks))   # tasks[0] – zawsze minimum
while tasks:
    prio, name = heapq.heappop(tasks)  # zdejmij minimum
    print(prio, name)
nums = [7, 2, 9, 4, 1, 8]
print(heapq.nsmallest(3, nums), heapq.nlargest(2, nums))


# --- Oczekiwany wynik ----------------------------------------
# (1, 'fix bug') 3
# 1 fix bug
# 2 write report
# 3 coffee
# [1, 2, 4] [9, 8]
