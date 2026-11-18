"""
Wykład 6 — slajd „Zadania (2/2)”
Plik: 35_zadanie8_recenzja.py

Zadanie 8 (Recenzja): ta funkcja zawiera kilka błędów — znajdź je i popraw.
Dopisz na dole wywołanie, np. print(word_index("a b a c")), i sprawdź, co się dzieje.
"""

def word_index(text):
    index = dict.fromkeys(text.split(), [])
    for i, w in enumerate(text.split()):
        index[w].append(i)
    for w in index:
        if len(index[w]) == 1:
            del index[w]
    return index
