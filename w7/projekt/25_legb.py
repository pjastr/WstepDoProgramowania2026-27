"""
Wykład 7 — slajd „Reguła LEGB”
Plik: 25_legb.py

Kolejność szukania nazwy: Local → Enclosing → Global → Built-in.
"""

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("inner: ", x)     # L
    def inner2():
        print("inner2:", x)     # brak lokalnej → E
    inner()
    inner2()
    print("outer: ", x)

outer()
print("moduł: ", x)             # G
print(len("abc"))               # len – B


# --- Oczekiwany wynik ----------------------------------------
# inner:  local
# inner2: enclosing
# outer:  enclosing
# moduł:  global
# 3
