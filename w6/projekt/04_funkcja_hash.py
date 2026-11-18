"""
Wykład 6 — slajd „Funkcja hash()”
Plik: 04_funkcja_hash.py

Funkcja hash(): równe obiekty mają równe hashe; 1, 1.0 i True to ten sam klucz.
Hash napisu zmienia się przy każdym uruchomieniu programu.

Uwaga: wynik hash("ala") % 8 jest za każdym razem inny.
"""

# hash liczby całkowitej to zwykle ona sama
print(hash(42), hash(-1), hash(-2))
# równe liczby mają równe hashe
print(hash(1) == hash(1.0) == hash(True))
print(hash((1, "a")) == hash((1, "a")))
# 1, 1.0 i True to ten sam klucz
print({1: "int", 1.0: "float", True: "bool"})
print(hash("ala") % 8)  # zależy od uruchomienia
hash([1, 2])            # lista nie ma hasha → błąd


# --- Oczekiwany wynik ----------------------------------------
# 42 -2 -2
# True
# True
# {1: 'bool'}
# 2
# TypeError: unhashable type: 'list'   <- błąd zamierzony (jak na slajdzie)
