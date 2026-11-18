"""
Wykład 6 — slajd „Studium: anagramy”
Plik: 32_anagramy.py

Studium: grupowanie anagramów za pomocą klucza kanonicznego.
"""

from collections import defaultdict

def anagram_groups(words):
    groups = defaultdict(list)                 # klucz kanoniczny → słowa
    for w in words:
        key = "".join(sorted(w.lower()))       # postać kanoniczna: litery A–Z
        groups[key].append(w)
    # zostawiamy grupy z co najmniej dwoma słowami
    return [g for g in groups.values() if len(g) > 1]

print(anagram_groups(["kot", "tok", "lis", "Kto", "sil", "pies", "ok"]))


# --- Oczekiwany wynik ----------------------------------------
# [['kot', 'tok', 'Kto'], ['lis', 'sil']]
