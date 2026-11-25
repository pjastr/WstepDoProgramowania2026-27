"""
Wykład 7 — slajd „*args — dowolna liczba argumentów”
Plik: 16_args.py

Parametr *args zbiera nadmiarowe argumenty pozycyjne w krotkę.
"""

def mean(*values):              # krotka argumentów
    print(type(values).__name__, values)
    if not values:
        return None
    return sum(values) / len(values)

print(mean(4, 5, 3))
print(mean())

def tag(name, *classes):        # zwykły, potem *
    joined = " ".join(classes)
    return f'<{name} class="{joined}">'

print(tag("div", "box", "red"))
print(max(3, 9, 2), max([3, 9, 2]))


# --- Oczekiwany wynik ----------------------------------------
# tuple (4, 5, 3)
# 4.0
# tuple ()
# None
# <div class="box red">
# 9 9
