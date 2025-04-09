tasks = []

def add_task(task):
    tasks.append(task)


def delete_task():
    tasks.remove(task)
    pass


def show_task():
    for elem in tasks:
        print(elem)


def is_done():
    pass


def main():
    while True:
        print("Mida sa tahad teha?")
        print("1 - lisada ülesanne\n2 - kustutada ülesanne\n3 - ülevaadata kõik ülesanded\n4 - muuta seisund")
        
        userInput = input("Sisesta valik: ")

        if userInput == "1":
            task = input("Sisesta tegevus: ")
            add_task(task)
        elif userInput == "2":
            task = input("Millist tegevust tahad kustutada?: ")
            delete_task()
        elif userInput == "3":
            show_task()
        elif userInput == "4":
            is_done()
        else:
            print("Tundmatu valik")

main()

