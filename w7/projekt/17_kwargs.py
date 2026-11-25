"""
Wykład 7 — slajd „**kwargs — dowolne nazwane”
Plik: 17_kwargs.py

Parametr **kwargs zbiera nadmiarowe argumenty nazwane w słownik.
"""

def make_user(login, **extra):
    print(type(extra).__name__, extra)
    return {"login": login, **extra}

print(make_user("ola", age=20, city="Ełk"))
print(make_user("jan"))
print(dict(a=1, b=2))

def report(title, *rows, sep=" | ", **style):
    print(title, rows, repr(sep), style)

report("R", 1, 2, width=40)


# --- Oczekiwany wynik ----------------------------------------
# dict {'age': 20, 'city': 'Ełk'}
# {'login': 'ola', 'age': 20, 'city': 'Ełk'}
# dict {}
# {'login': 'jan'}
# {'a': 1, 'b': 2}
# R (1, 2) ' | ' {'width': 40}
