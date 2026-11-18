"""
Wykład 6 — slajd „Zbiór w algorytmach”
Plik: 11_zbior_w_algorytmach.py

Wzorzec „już widziane”: pierwszy powtórzony element i usuwanie duplikatów
z zachowaniem kolejności.
"""

def first_repeat(xs):
    seen = set()          # już widziane
    for x in xs:
        if x in seen:     # O(1)
            return x
        seen.add(x)
    return None           # bez powtórzeń

def unique_in_order(xs):
    seen, out = set(), []
    for x in xs:
        if x not in seen:  # pierwszy raz
            seen.add(x)
            out.append(x)  # zachowuje kolejność
    return out

print(first_repeat([3, 8, 1, 8, 3]),
      first_repeat("abc"))
print(unique_in_order("abracadabra"))
# litery wspólne dla obu nazw
print(sorted(set("kotlin") & set("python")))


# --- Oczekiwany wynik ----------------------------------------
# 8 None
# ['a', 'b', 'r', 'c', 'd']
# ['n', 'o', 't']
