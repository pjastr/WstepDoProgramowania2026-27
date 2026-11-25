"""
Wykład 7 — slajd „Zmieniać argument czy zwracać nowy?”
Plik: 22_zmieniac_czy_zwracac.py

Dwie konwencje: zwróć nowy obiekt albo zmień argument i zwróć None; kopia obronna.
"""

def normalized(scores):          # nowa lista
    top = max(scores)
    return [s / top for s in scores]

def normalize(scores):           # w miejscu, None
    top = max(scores)
    for i in range(len(scores)):
        scores[i] /= top

def without_min(scores):
    copy = scores[:]             # kopia obronna
    copy.remove(min(copy))
    return copy

s = [50, 80, 100]
print(normalized(s), s)
print(without_min(s), s)
print(normalize(s), s)


# --- Oczekiwany wynik ----------------------------------------
# [0.5, 0.8, 1.0] [50, 80, 100]
# [80, 100] [50, 80, 100]
# None [0.5, 0.8, 1.0]
