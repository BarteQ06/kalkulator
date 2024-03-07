import modules

def wykonaj_operacje():
    x = float(input("Podaj pierwszą liczbę: "))
    operator = input("Podaj operator(+,-,/,*) : ")
    y = float(input("Podaj drugą liczbę: "))

    match operator:
        case '+':
            wynik = modules.dodawanie(x, y)
        case '-':
            wynik = modules.odejmowanie(x, y)
        case '*':
            wynik = modules.mnozenie(x, y)
        case '/':
            wynik = modules.dzielenie(x, y)
        case _:
            wynik = "Nieprawidłowy operator."
    print(f"Wynik {x} {operator} {y} = {wynik}")

wykonaj_operacje()