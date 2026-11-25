"""
Wykład 7 — slajd „Po co funkcje?”
Plik: 01_po_co_funkcje.py

Ten sam wzór przepisywany kilka razy kontra funkcja zapisana raz i wywoływana wielokrotnie.
"""

group_a = [4.5, 3.0, 5.0]
group_b = [3.5, 4.0]
group_c = []
# bez funkcji: ten sam wzór kopiowany dla każdej grupy
avg_a = sum(group_a) / len(group_a) if group_a else 0.0
avg_b = sum(group_b) / len(group_b) if group_b else 0.0
print(avg_a, avg_b)

# z funkcją: wzór zapisany raz, pod nazwą
def mean(xs):
    if not xs:              # pusta lista – umowna średnia 0
        return 0.0
    return sum(xs) / len(xs)

print(mean(group_a), mean(group_b), mean(group_c))


# --- Oczekiwany wynik ----------------------------------------
# 4.166666666666667 3.75
# 4.166666666666667 3.75 0.0
