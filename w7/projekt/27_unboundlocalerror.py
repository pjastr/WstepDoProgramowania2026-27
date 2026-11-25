"""
Wykład 7 — slajd „UnboundLocalError”
Plik: 27_unboundlocalerror.py

Przypisanie gdziekolwiek w funkcji czyni nazwę lokalną w całej funkcji — także przed tym przypisaniem.
"""

n = 0

def show():
    print(n)            # tylko odczyt – zmienna globalna

def bump():
    n += 1              # przypisanie → n lokalna w CAŁEJ funkcji
    return n

def show_then_set():
    print(n)            # błąd już tutaj!
    n = 5

show()
try:                    # (try/except – później)
    bump()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
show_then_set()


# --- Oczekiwany wynik ----------------------------------------
# 0
# UnboundLocalError: cannot access local variable 'n' where it is not associated with a value
# UnboundLocalError: cannot access local variable 'n' where it is not associated with a value   <- błąd zamierzony (jak na slajdzie)
