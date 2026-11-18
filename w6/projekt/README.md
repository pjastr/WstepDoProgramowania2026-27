# Wykład 6 — przykłady w Pythonie

Kody ze slajdów wykładu 6 (krotki, zbiory, słowniki, tablice i kolejki, wyrażenia zbiorowe i słownikowe).
Nazwa pliku jest podana nad każdym fragmentem kodu na slajdzie.

## Jak otworzyć w PyCharmie

1. *File → Open…* i wskaż ten folder (`projekt`).
2. Wybierz interpreter: Python 3.10 lub nowszy (*Python Interpreter* w prawym dolnym rogu okna;
   PyCharm może od razu utworzyć wirtualne środowisko `.venv`).
3. Prawy przycisk myszy na pliku → *Run* (lub `Ctrl+Shift+F10`).

Przykłady korzystają tylko z biblioteki standardowej — nic nie trzeba instalować.

## Wskazówki

- Na końcu każdego pliku jest komentarz **Oczekiwany wynik** — porównaj go z konsolą.
- Część przykładów **celowo kończy się błędem** (np. `KeyError`, `TypeError`), tak jak na slajdzie.
  W oczekiwanym wyniku taki wiersz jest oznaczony `<- błąd zamierzony`.
- Wyniki z `hash()` dla napisów, czasy z `timeit` i rozmiary z `getsizeof` zależą od uruchomienia,
  komputera lub wersji Pythona.
- `36_czestosc_slow_stdin.py` czyta tekst ze standardowego wejścia: wpisz tekst w konsoli PyCharma
  i zakończ `Ctrl+D` albo uruchom w terminalu `python 36_czestosc_slow_stdin.py < plik.txt`.
- `35_zadanie8_recenzja.py` to zadanie: kod zawiera błędy do znalezienia i poprawienia.

## Spis plików

| Plik | Slajd |
|---|---|
| `01_krotka_rekord.py` | Krotka jako rekord |
| `02_niezmiennosc_plytka.py` | Niezmienność jest płytka |
| `03_namedtuple.py` | namedtuple — krotka z nazwanymi polami |
| `04_funkcja_hash.py` | Funkcja hash() |
| `05_haszowalnosc.py` | Haszowalność a niezmienność |
| `06_zbior_podstawy.py` | Zbiór — podstawy |
| `07_dzialania_na_zbiorach.py` | Działania na zbiorach |
| `08_metody_zbioru.py` | Metody, operatory, modyfikacja |
| `09_in_lista_czy_zbior.py` | in: lista czy zbiór? |
| `10_frozenset.py` | frozenset — zbiór niezmienny |
| `11_zbior_w_algorytmach.py` | Zbiór w algorytmach |
| `12_slownik_podstawy.py` | Słownik — podstawy |
| `13_bezpieczny_odczyt.py` | Bezpieczny odczyt |
| `14_wstawianie_usuwanie.py` | Wstawianie, łączenie, usuwanie |
| `15_iterowanie_slownik.py` | Iterowanie po słowniku |
| `16_widoki_slownika.py` | Widoki i zmiany w trakcie iteracji |
| `17_zliczanie.py` | Zliczanie — trzy sposoby |
| `18_counter.py` | Counter |
| `19_grupowanie.py` | Grupowanie |
| `20_sortowanie_ekstrema.py` | Sortowanie i ekstrema |
| `21_plansza_krotka_klucz.py` | Krotka jako klucz — plansza |
| `22_tabela_dyspozycyjna.py` | Słownik zamiast if/elif |
| `23_zlozonosc_pamiec.py` | Złożoność i pamięć |
| `24_array.py` | Moduł array — tablica jednego typu |
| `25_deque.py` | deque — kolejka dwustronna |
| `26_heapq.py` | heapq — kolejka priorytetowa |
| `27_bytearray_bisect.py` | Inne kontenery — przegląd |
| `28_cztery_wyrazenia.py` | Cztery rodzaje wyrażeń |
| `29_wyrazenia_slownikowe.py` | Wyrażenia słownikowe — wzorce |
| `30_zasieg_zmiennych.py` | Zasięg zmiennych w wyrażeniach |
| `31_petla_czy_wyrazenie.py` | Kiedy lepsza zwykła pętla? |
| `32_anagramy.py` | Studium: anagramy |
| `33_para_o_sumie.py` | Studium: para o zadanej sumie |
| `34_czestosc_slow.py` | Studium: częstość słów |
| `35_zadanie8_recenzja.py` | Zadania (2/2) |
| `36_czestosc_slow_stdin.py` | Ten sam program: częstość słów |
