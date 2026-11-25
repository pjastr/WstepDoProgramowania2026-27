"""
Wykład 7 — slajd „Krokowanie”
Plik: 36_krokowanie.py

Przykład do ćwiczenia krokowania i obserwowania stosu wywołań (panel Frames).
Postaw punkt przerwania w wierszu print(count_long(…)) i używaj F7 / F8 / Shift+F8.
"""

def clean(word):
    return word.strip(".,!?").lower()

def count_long(text, min_len):
    count = 0
    for raw in text.split():
        word = clean(raw)   # F7 / F8
        if len(word) >= min_len:
            count += 1
    return count

def main():
    text = "Ala ma kota, a kot ma Alę!"
    print(count_long(text, 3))

main()


# --- Oczekiwany wynik ----------------------------------------
# 4
