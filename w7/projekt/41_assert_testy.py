"""
Wykład 7 — slajd „Sprawdzanie funkcji: assert”
Plik: 41_assert_testy.py

Poprawiona funkcja z pliku 35 i proste testy z assert; ostatnia asercja celowo jest błędna.
"""

def trimmed_mean(xs, k):
    ys = sorted(xs)
    kept = ys[k:len(ys) - k]    # poprawka dla k == 0
    return sum(kept) / len(kept)

def test_trimmed_mean():
    assert trimmed_mean([7, 1, 5, 9, 3], 1) == 5
    assert trimmed_mean([7, 1, 5, 9, 3], 0) == 5
    assert trimmed_mean([1, 2, 3, 10], 1) == 2.5
    print("testy OK")

test_trimmed_mean()
assert trimmed_mean([1, 2], 0) == 2, "średnia z 1 i 2"


# --- Oczekiwany wynik ----------------------------------------
# testy OK
# AssertionError: średnia z 1 i 2   <- błąd zamierzony (jak na slajdzie)
