"""
Wykład 7 — slajd „def tworzy obiekt funkcji”
Plik: 03_def_tworzy_obiekt.py

def jest instrukcją wykonywaną w chwili, gdy interpreter do niej dojdzie; funkcja to obiekt,
który można nazwać inaczej, a ponowne def podmienia funkcję.
"""

try:                    # (try/except – później)
    greet("Ola")        # funkcji jeszcze nie ma
except NameError as e:
    print("NameError:", e)

def greet(name):
    return f"Cześć, {name}!"

print(greet("Ola"))
print(type(greet).__name__, callable(greet))
say = greet             # druga nazwa obiektu
print(say("Jan"), say is greet)

def greet(name):        # nowe def podmienia
    return f"Witaj, {name}."

print(greet("Ewa"), say("Ewa"))


# --- Oczekiwany wynik ----------------------------------------
# NameError: name 'greet' is not defined
# Cześć, Ola!
# function True
# Cześć, Jan! True
# Witaj, Ewa. Cześć, Ewa!
