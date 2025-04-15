def mySum(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else :
        print("VALE")

print (mySum(55,32))

def mySubtract(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a - b
    else :
        print("VALE")

print (mySubtract(55,32))

def myMultiply(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a * b
    else :
        print("VALE")

print (myMultiply(55,32))

def myDivide(a,b):
    try:
        if isinstance(a,int) and isinstance(b,int):
            return a / b
        else :
            print("VALE")
    except ZeroDivisionError:
        print("EI SAA")

print (myDivide(55,2))


def main():
    while true:
        print("1.Liitmine")
        print("2.Lahutamine")
        print("3.Korrutamine")
        print("4.Jagamine")
        valik = input("Tee valik (1-4):")

        
        if valik == "1":
            a = int(input("sisesta number 1: "))
            b = int(input("sisesta number 2: "))
            myArr[0] += 1
            result = mySum(a,b)
            print("Tulemus on: ", result)
        elif valik == "2":
            a = int(input("sisesta number 1: "))
            b = int(input("sisesta number 2: "))
            myArr[1] += 1
            result = mySubtract(a,b)
            print("Tulemus on: ", result)
        elif valik == "3":
            a = int(input("sisesta number 1: "))
            b = int(input("sisesta number 2: "))
            myArr[2] += 1
            result = myMultiply(a,b)
            print("Tulemus on: ", result)
        elif valik == "4":
            a = int(input("sisesta number 1: "))
            b = int(input("sisesta number 2: "))
            myArr[3] += 1
            result = myDivide(a,b)
            print("Tulemus on: ", result)
        else:
            print("Seda valiku pole")
    main()

def displayInfo():
    print("kokku oli: ", sum(myArr))
    print("Liitmine töötas: ", myArr[0], "korda")
    print("Lahutamine töötas: ", myArr[1], "korda")
    print("Korrutamine töötas: ", myArr[2], "korda")
    print("Jagamine töötas: ", myArr[3], "korda")
    
myArr = [0,0,0,0]






