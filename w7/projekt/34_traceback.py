"""
Wykład 7 — slajd „Czytanie komunikatu o błędzie”
Plik: 34_traceback.py

Błąd zgłoszony głęboko w łańcuchu wywołań: traceback czytamy od dołu.
W PyCharmie wiersze „File …, line …” są linkami do kodu.
"""

def parse_grade(text):
    return float(text.replace(",", "."))

def average_grade(line):
    parts = line.split(";")
    grades = [parse_grade(p) for p in parts[1:]]
    return sum(grades) / len(grades)

def main():
    print(average_grade("Nowak;4,5;5;3"))
    print(average_grade("Kowalska;5;;4"))

main()


# --- Oczekiwany wynik ----------------------------------------
# 4.166666666666667
# Traceback (most recent call last):
#   File "C:\…\projekt\34_traceback.py", line 21, in <module>
#     main()
#     ~~~~^^
#   File "C:\…\projekt\34_traceback.py", line 19, in main
#     print(average_grade("Kowalska;5;;4"))
#           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\…\projekt\34_traceback.py", line 14, in average_grade
#     grades = [parse_grade(p) for p in parts[1:]]
#               ~~~~~~~~~~~^^^
#   File "C:\…\projekt\34_traceback.py", line 10, in parse_grade
#     return float(text.replace(",", "."))
# ValueError: could not convert string to float: ''   <- błąd zamierzony (jak na slajdzie)
