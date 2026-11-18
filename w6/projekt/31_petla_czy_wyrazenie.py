"""
Wykład 6 — slajd „Kiedy lepsza zwykła pętla?”
Plik: 31_petla_czy_wyrazenie.py

Kiedy zamiast wyrażenia lepsza jest zwykła pętla for.
"""

# unikaj: lista tylko dla print
[print(x) for x in range(3)]

data = {"a": [1, 2, 3], "b": [4], "c": []}
# trudne do czytania: 2 poziomy
odd = {k: [y for y in v if y % 2]
       for k, v in data.items() if v}

# lepiej: zwykła pętla
for x in range(3):
    print(x)

# lepiej: krok po kroku, z nazwami
odd = {}
for key, vals in data.items():
    if vals:            # pomijamy puste
        odd[key] = [y for y in vals if y % 2]
print(odd)


# --- Oczekiwany wynik ----------------------------------------
# 0
# 1
# 2
# 0
# 1
# 2
# {'a': [1, 3], 'b': []}
