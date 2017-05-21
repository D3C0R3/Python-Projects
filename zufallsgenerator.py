import random
from time import sleep
names = []
eingabe = 0
grenze = 0
inp = 0

print("Zu Anfang befinden sich keine Werte in der Liste! Adden Sie zuerst 2 Werte um den Vorgang zu starten!")
uno = input("Geben Sie den ersten Wert ein: ")
names.append(uno)
dos = input("Geben Sie den zweiten Wert ein: ")
names.append(dos)
print("Ihre Liste beinhaltet nun", names[0], "und", names[1])

while (eingabe != 3 or 2 or 1):
    print("Optionen:\n 1 = Wert hinzufuegen\n 2 = Wert entfernen\n 3 = Den Zufall entscheiden lassen")
    eingabe = int(input("Was wollen Sie tun?: "))
    
    if (eingabe == 1):        
        
        print("Hier koennen Sie die Werte hinzufuegen: ")
        newn = input("Geben Sie einen neuen Wert ein: ")
        
        names.append(newn)
        
        print(names)
        
        while grenze < 10:
            inp = int(input("Moechten Sie noch einen Wert hinzufuegen [1=Ja/2=Nein]?"))
              
            if (inp == 1):
                print("Hier koennen Sie die Werte hinzufuegen: ")
                newn = input("Geben Sie einen neuen Wert ein: ")
        
                names.append(newn)
        
                print(names)
                grenze = grenze + 1 
                continue
             
            elif (inp == 2):
                print("Ihr Liste beinhaltet nun ", len(names), "Werte!")
                break
                
            else:
                print("Ungueltige Eingabe!")
                continue        
    
    elif (eingabe == 2):
        
        print("Hier koennen Sie Werte entfernen: ")
        out = input("Welchen Wert moechten Sie entfernen?: ")
        
        names.remove(out)
        
        print(names)
        print("Ihr Liste beinhaltet nun ", len(names), "Werte!")
        continue
    
    elif (eingabe == 3):
        
        spanne = len(names)
        
        while spanne != 2:
            aussuche = random.choice(names)
            print("5")
            sleep(0.5)
            print("4")
            sleep(0.5)
            print("3")
            sleep(0.5)
            print("2")
            sleep(0.5)
            print("1")
            sleep(0.5)
            print(aussuche, "ist es NICHT!")
            names.remove(aussuche)
            spanne = spanne - 1
        
        print("...............")
        sleep(1)
        print("Jetzt sind nur noch", names[0], "und", names[1], "im Pott!")
        print("...............")
        sleep(5)
        print(random.choice(names), "ist der Random Wert!")
        
        break
    else:
        print("Ungueltige Eingabe!")
        continue
