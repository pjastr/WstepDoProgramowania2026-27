"""
Wykład 6 — slajd „Sortowanie i ekstrema”
Plik: 20_sortowanie_ekstrema.py

Sortowanie słownika według wartości, ranking z remisami, max z key.
"""

votes = {"Ala": 12, "Bartek": 30, "Celina": 12, "Darek": 25}
# klucz o największej wartości; najmniejsza wartość
print(max(votes, key=votes.get), min(votes.values()))
# sortujemy pary: głosy malejąco (minus), przy remisie imię rosnąco
ranking = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))
for place, (name, v) in enumerate(ranking, 1):   # numeracja od 1
    print(place, name, v)
# nowy słownik ułożony według wartości
by_value = dict(sorted(votes.items(), key=lambda kv: kv[1]))
print(by_value)


# --- Oczekiwany wynik ----------------------------------------
# Bartek 12
# 1 Bartek 30
# 2 Darek 25
# 3 Ala 12
# 4 Celina 12
# {'Ala': 12, 'Celina': 12, 'Darek': 25, 'Bartek': 30}
