import sys

def procentajSucces():
    f = open('values.txt', 'r')
    suma = 0
    numarSucces = 0
    count = 0
    countSucces = 0
    procentaj = 0

    while True:
        count += 1
        
        line = f.readline()
        if not line:
            break
        line = float(line)
        if line > 1.20:
            countSucces += 1
    f.close()
    procentaj = round((countSucces / count) * 100)
    return procentaj, count, countSucces

def profitCalculator():
    rezultatSucces = procentajSucces()
    procentaj = rezultatSucces[0]
    numarValori = rezultatSucces[2]
    numarSuccese = rezultatSucces[1]
    profit = 0
    pierderi = 0
    f = open('values.txt', 'r')
    print("Cat pariem?")
    betSize = float(input())
    if betSize < 0.5:
        print("Bad input!")
    else:
        while True:
            line1 = f.readline()
            if not line1:
                break
            line1 = float(line1)
            if line1 > 1.20:
                profit = (betSize * 1.20) - betSize + profit
            if line1 <= 1.20:
                pierderi = pierderi + betSize
    total = profit - pierderi
    print("Numar de valori introduse: " + str(numarValori) + "   Numarul de succese: " + str(numarSuccese))
    print("Procentajul succeselor: " + str(procentaj) + "%")
    print("Am obtinut un profit de " + str(profit) + " lei, dar am pierdut " + str(pierderi) + " lei.")
    print("In total am ramas cu suma de " + str(total) + " lei.")

if __name__ == "__main__":
	profitCalculator()
