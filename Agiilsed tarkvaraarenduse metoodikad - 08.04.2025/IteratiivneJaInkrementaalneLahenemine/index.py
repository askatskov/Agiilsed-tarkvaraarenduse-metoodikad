myArr = [0, 0, 0, 0]

def myPlus(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        print("vale sisestamine")
def myMiinus(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a - b
    else:
        print("vale sisestamine")
def myKorrutamine(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a * b
    else:
        print("vale sisestamine")
def myJagamine(a,b):
    if isinstance(a,int) and isinstance(b,int):
        if b != 0:
            return a / b
        else:
            return "ei saa jagada nulliga"
    else:
        print("vale sisestamine")

def displayInfo():
    print("kokku oli ", sum(myArr))
    print("summeerimine töötas: ", myArr[0], "korda")
    print("lahutamine oli: ", myArr[1], "korda")
    print("korrutamine oli: ", myArr[2], "korda")
    print("jagamine oli: ", myArr[3], "korda")

def main():
    while True:
        valik = input("Mida sa tahad teha? (+ = 1, - = 2, * = 3, / = 4): ")
        if valik == "1":
            a = int(input("Sisesta number 1: "))
            b = int(input("Sisesta number 2: "))
            myArr[0] += 1
            result = myPlus(a, b)
            print("Tulemus on: ", result)
        elif valik == "2":
            a = int(input("Sisesta number 1: "))
            b = int(input("Sisesta number 2: "))
            myArr[1] += 1
            result = myMiinus(a, b)
            print("Tulemus on: ", result)
        elif valik == "3":
            a = int(input("Sisesta number 1: "))
            b = int(input("Sisesta number 2: "))
            myArr[2] += 1
            result = myKorrutamine(a, b)
            print("Tulemus on: ", result)
        elif valik == "4":
            a = int(input("Sisesta number 1: "))
            b = int(input("Sisesta number 2: "))
            myArr[3] += 1
            result = myJagamine(a, b)
            print("Tulemus on: ", result)
        else:
            print("Seda valikut ei ole!")
        displayInfo()
main()