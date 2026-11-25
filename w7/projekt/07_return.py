"""
Wykład 7 — slajd „return kończy funkcję”
Plik: 07_return.py

return natychmiast kończy funkcję; kilka punktów wyjścia; samo return.
"""

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
    print("nigdy")      # nieosiągalne – PyCharm wyszarza

def report(xs):
    if not xs:
        print("brak danych")
        return          # samo return – bez wyniku
    print("max:", max(xs))

print(sign(5), sign(-2), sign(0))
report([])
report([3, 8, 1])


# --- Oczekiwany wynik ----------------------------------------
# 1 -1 0
# brak danych
# max: 8
