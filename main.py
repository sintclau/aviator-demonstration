import sys

def procentajSucces():
    f = open('values.txt', 'r')
    suma = 0
    numarSucces = 0
    count = 0
    countSucces = 0
    procentaj = 0

    while True:
        line = f.readline()
        if not line:
            break
        line = float(line)
        count += 1
        if line > 1.20:
            countSucces += 1
    f.close()
    procentaj = round((countSucces / count) * 100)
    return procentaj, count, countSucces

def profitCalculator():
    rezultatSucces = procentajSucces()
    procentaj = rezultatSucces[0]
    numarValori = rezultatSucces[1]
    numarSuccese = rezultatSucces[2]
    profit = 0
    pierderi = 0
    f = open('values.txt', 'r')
    print("Enter the bet size:")
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
    print("Number of values entered: " + str(numarValori) + "   Number of successful rounds: " + str(numarSuccese))
    print("Success rate: " + str(procentaj) + "%")
    print("We have obtained a profit of " + str(profit) + " $, however we lost " + str(pierderi) + " $.")
    print("In total we won " + str(total) + " $.")

if __name__ == "__main__":
	profitCalculator()
