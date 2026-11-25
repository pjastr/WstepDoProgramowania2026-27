# Wykład 7 — przykłady w Pythonie

Kody ze slajdów wykładu 7 (funkcje: definiowanie, parametry i argumenty, zwracanie wartości,
zasięg zmiennych, debugowanie funkcji w PyCharmie).
Nazwa pliku jest podana nad każdym fragmentem kodu na slajdzie.

## Jak otworzyć w PyCharmie

1. *File → Open…* i wskaż ten folder (`projekt`).
2. Wybierz interpreter: Python 3.10 lub nowszy (*Python Interpreter* w prawym dolnym rogu okna;
   PyCharm może od razu utworzyć wirtualne środowisko `.venv`).
3. Prawy przycisk myszy na pliku → *Run* (lub `Ctrl+Shift+F10`).

Przykłady korzystają tylko z biblioteki standardowej — nic nie trzeba instalować.

## Wskazówki

- Na końcu każdego pliku jest komentarz **Oczekiwany wynik** — porównaj go z konsolą.
- Część przykładów **celowo kończy się błędem** (np. `TypeError`, `UnboundLocalError`), tak jak na slajdzie.
  W oczekiwanym wyniku taki wiersz jest oznaczony `<- błąd zamierzony`. Dotyczy to plików: `09`, `10`, `11`, `13`, `18`, `19`, `23`, `24`, `27`, `29`, `31`, `33`, `34`, `35`, `39`, `41`.
- Wyniki na slajdach pochodzą z CPythona 3.13; w starszych wersjach treść niektórych komunikatów
  o błędach może się nieco różnić, a w tracebacku nie ma znaczników `^^^^`.
- `34_traceback.py` pokazuje pełny komunikat o błędzie — ścieżka do pliku w Twoim komputerze będzie inna.

## Debugowanie (pliki 34–42)

Te pliki uruchamiaj przez **Debug** (`Shift+F9` lub prawy przycisk → *Debug*), nie przez *Run*.
Opis zadania jest w docstringu na początku każdego pliku.

| Skrót | Działanie |
|---|---|
| `Ctrl+F8` | postaw / usuń punkt przerwania |
| `F8` | *Step Over* — wykonaj wiersz |
| `F7` | *Step Into* — wejdź do funkcji |
| `Shift+F8` | *Step Out* — dokończ funkcję |
| `Alt+F9` | *Run to Cursor* |
| `F9` | *Resume* — do następnego punktu przerwania |
| `Alt+F8` | *Evaluate Expression* |
| `Ctrl+Shift+F8` | lista punktów przerwania, warunki, punkty na wyjątkach |

Pliki `35`, `37`, `38`, `40` zawierają **celowe błędy** do znalezienia debugerem;
`42_print_debug.py` ma zakomentowane `breakpoint()` — odkomentuj, aby zobaczyć pdb.
`43_zadanie8_recenzja.py` to zadanie: kod zawiera błędy do znalezienia i poprawienia.

## Spis plików

| Plik | Slajd |
|---|---|
| `01_po_co_funkcje.py` | Po co funkcje? |
| `02_anatomia_funkcji.py` | Anatomia funkcji |
| `03_def_tworzy_obiekt.py` | def tworzy obiekt funkcji |
| `04_stos_wywolan.py` | Wywołanie funkcji — stos ramek |
| `05_docstring.py` | Docstring i help() |
| `06_dobra_funkcja.py` | Jak wygląda dobra funkcja? |
| `07_return.py` | return kończy funkcję |
| `08_brak_return.py` | Brak return → None |
| `09_print_czy_return.py` | print czy return? |
| `10_wiele_wartosci.py` | Kilka wyników naraz |
| `11_sciezki_return.py` | Każda ścieżka zwraca wartość |
| `12_czyste_funkcje.py` | Funkcja czysta a efekty uboczne |
| `13_parametry_argumenty.py` | Parametry i argumenty |
| `14_wartosci_domyslne.py` | Wartości domyślne |
| `15_domyslna_modyfikowalna.py` | Pułapka: modyfikowalna wartość domyślna |
| `16_args.py` | *args — dowolna liczba argumentów |
| `17_kwargs.py` | **kwargs — dowolne nazwane |
| `18_rozpakowanie_wywolanie.py` | Rozpakowanie przy wywołaniu |
| `19_tylko_nazwane.py` | Parametry tylko nazwane i tylko pozycyjne |
| `20_pelna_sygnatura.py` | Pełna sygnatura — kolejność parametrów |
| `21_przekazywanie_argumentow.py` | Przekazywanie argumentów |
| `22_zmieniac_czy_zwracac.py` | Zmieniać argument czy zwracać nowy? |
| `23_adnotacje_typow.py` | Adnotacje typów |
| `24_zmienne_lokalne.py` | Zmienne lokalne |
| `25_legb.py` | Reguła LEGB |
| `26_globalne_odczyt.py` | Odczyt zmiennych globalnych |
| `27_unboundlocalerror.py` | UnboundLocalError |
| `28_global.py` | global — zapis do zmiennej modułu |
| `29_nonlocal.py` | Funkcje zagnieżdżone i nonlocal |
| `30_domkniecie.py` | Domknięcie |
| `31_przeslanianie_nazw.py` | Przesłanianie nazw wbudowanych |
| `32_bez_global.py` | Zamiast global: parametry i return |
| `33_funkcje_jako_argumenty.py` | Funkcja jako argument |
| `34_traceback.py` | Czytanie komunikatu o błędzie |
| `35_debug_srednia.py` | Punkt przerwania i tryb Debug |
| `36_krokowanie.py` | Krokowanie |
| `37_watches.py` | Obserwowanie wyrażeń: Watches i Evaluate |
| `38_warunkowy_breakpoint.py` | Warunkowy punkt przerwania |
| `39_breakpoint_wyjatek.py` | Zatrzymanie na wyjątku |
| `40_studium_debug.py` | Studium: szukamy błędu debugerem |
| `41_assert_testy.py` | Sprawdzanie funkcji: assert |
| `42_print_debug.py` | print, breakpoint() czy debuger? |
| `43_zadanie8_recenzja.py` | Zadania (2/2) |
| `44_statystyki.py` | Ten sam program: kilka wyników |
