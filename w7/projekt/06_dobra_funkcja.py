"""
Wykład 7 — slajd „Jak wygląda dobra funkcja?”
Plik: 06_dobra_funkcja.py

Funkcja „od wszystkiego” (z ukrytym błędem) kontra małe funkcje, z których każda robi jedno.
"""

# jedna funkcja robi wszystko: liczy i wypisuje
def process(data):
    total = 0
    for x in data:
        if x > 0:
            total += x
    print("suma dodatnich:", total)
    print("średnia dodatnich:", total / len(data))

# lepiej: małe funkcje, każda robi jedno
def positives(xs):
    return [x for x in xs if x > 0]

def mean(xs):
    return sum(xs) / len(xs)

data = [4, -2, 6, -8]
process(data)
pos = positives(data)
print("suma dodatnich:", sum(pos))
print("średnia dodatnich:", mean(pos))


# --- Oczekiwany wynik ----------------------------------------
# suma dodatnich: 10
# średnia dodatnich: 2.5
# suma dodatnich: 10
# średnia dodatnich: 5.0
