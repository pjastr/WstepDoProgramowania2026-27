"""
Wykład 6 — slajd „Krotka jako klucz — plansza”
Plik: 21_plansza_krotka_klucz.py

Krotka współrzędnych jako klucz: rzadka plansza i rzadka macierz.
"""

# (wiersz, kolumna) → znak; puste pola pomijamy
board = {(0, 0): "X", (1, 1): "O", (2, 0): "X"}
board[0, 2] = "O"             # to samo co board[(0, 2)]
for r in range(3):
    # brak klucza → kropka (puste pole)
    print(" ".join(board.get((r, c), ".")
                   for c in range(3)))
# pozycje wszystkich X
xs = [pos for pos, mark in board.items() if mark == "X"]
print(xs, len(board))
# rzadka macierz jednostkowa: tylko przekątna
eye = {(i, i): 1.0 for i in range(10**6)}
print(len(eye), eye.get((5, 7), 0.0))


# --- Oczekiwany wynik ----------------------------------------
# X . O
# . O .
# X . .
# [(0, 0), (2, 0)] 4
# 1000000 0.0
