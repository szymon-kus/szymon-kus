while True:
    try:
        n = int(input("Podaj ile liczb całkowitych chcesz dodać: "))
        if n >= 1:
            break 
        else:
            print("Podana liczba musi być większa lub równa 1.")
    except ValueError:
        print("Podana wartość nie jest liczbą całkowitą.")

def suma_n_liczb(n):
    if n <= 0:
        print("Nie można obliczyć sumy dla ilości liczb nie większej niż 0")
        return 0
    else:
        return n + suma_n_liczb(n - 1)

wynik = suma_n_liczb(n)
print(f"Suma ({n}) liczb wynosi: {wynik}")
