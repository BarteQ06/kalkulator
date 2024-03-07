def wykonaj_operacje(operator,x,y):
    # match operator:
    #     case '+':
    #         return dodawanie(x,y)
    #     case '-':
    #         return odejmowanie(x,y)
    #     case '*':
    #         return mnozenie(x,y)
    #     case '/':
    #         return dzielenie(x,y)
    #     case _:
    #         return "Nieprawidłowy operator."

    x = float(input("Podaj pierwszą liczbę: "))
    operator = input("Podaj operator(+,-,/,*) : ")
    y = float(input("Podaj drugą liczbę: "))
    wynik = wykonaj_operacje(operator, x, y)
    print(f"Wynik {x} {operator} {y} = {wynik}")