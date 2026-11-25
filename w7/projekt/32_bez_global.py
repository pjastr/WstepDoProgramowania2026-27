"""
Wykład 7 — slajd „Zamiast global: parametry i return”
Plik: 32_bez_global.py

Ten sam problem (saldo konta) ze stanem globalnym i ze stanem przekazywanym jawnie.
"""

balance = 100                   # wersja z global – stan ukryty

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount

withdraw(30)
print(balance)

def withdrawn(balance, amount):  # wersja jawna – stan na wejściu i wyjściu
    if amount > balance:
        return balance          # odmowa: saldo bez zmian
    return balance - amount

acc1, acc2 = 100, 500           # dwa konta – bez problemu
acc1 = withdrawn(acc1, 30)
acc2 = withdrawn(acc2, 600)
print(acc1, acc2, withdrawn(100, 30) == withdrawn(100, 30))


# --- Oczekiwany wynik ----------------------------------------
# 70
# 70 500 True
