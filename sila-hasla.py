# skrypt do analizy siły hasła

def ocen_sile_hasla(haslo):
    # Sprawdź długość hasła
    dlugosc = len(haslo)

    # Sprawdź, czy hasło zawiera małe litery
    małe_litery = any(c.islower() for c in haslo)

    # Sprawdź, czy hasło zawiera duże litery
    duże_litery = any(c.isupper() for c in haslo)

    # Sprawdź, czy hasło zawiera cyfry
    cyfry = any(c.isdigit() for c in haslo)

    # Sprawdź, czy hasło zawiera znaki specjalne
    znaki_specjalne = any(c.isalnum() for c in haslo)

    # Ocen siłę hasła
    sila_hasla = 0
    if dlugosc >= 8:
        sila_hasla += 1
    if małe_litery:
        sila_hasla += 1
    if duże_litery:
        sila_hasla += 1
    if cyfry:
        sila_hasla += 1
    if znaki_specjalne:
        sila_hasla += 1

    return sila_hasla

haslo_uzytkownika = input("Podaj hasło do analizy: ")
wynik = ocen_sile_hasla(haslo_uzytkownika)

print(f"Siła hasła: {wynik}/5")