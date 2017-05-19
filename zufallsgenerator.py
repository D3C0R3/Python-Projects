import random
from time import sleep
names = []
eingabe = 0
befehl1 = 1
befehl2 = 2
befehl3 = 3
inp = 0
m1 = 1
m2 = 2
grenze = 0

while (eingabe != befehl3 or befehl2 or befehl1):
    print("Optionen:\n 1 = Wert hinzufuegen\n 2 = Wert entfernen\n 3 = Den Zufall entscheiden lassen")
    eingabe = int(input("Was wollen Sie tun?: "))
    
    if (eingabe == befehl1):        
        
        print("Hier koennen Sie die Werte hinzufuegen: ")
        newn = input("Geben Sie einen neuen Wert ein: ")
        
        names.append(newn)
        
        print(names)
        
        while grenze < 5:
            inp = int(input("Moechten Sie noch einen Wert hinzufuegen [1=Ja/2=Nein]?"))
              
            if (inp == m1):
                print("Hier koennen Sie die Werte hinzufuegen: ")
                newn = input("Geben Sie einen neuen Wert ein: ")
        
                names.append(newn)
        
                print(names)
                grenze = grenze + 1 
                continue
             
            elif (inp == m2):
                print("Ihr Liste beinhaltet nun ", len(names), "Werte!")
                break
                
            else:
                print("Ungueltige Eingabe!")
                continue        
    
    elif (eingabe == befehl2):
        
        print("Hier koennen Sie Werte entfernen: ")
        out = input("Welchen Wert moechten Sie entfernen?: ")
        
        names.remove(out)
        
        print(names)
        print("Ihr Liste beinhaltet nun ", len(names), "Werte!")
        continue
    
    elif (eingabe == befehl3):
        
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
        
        vi1 = names[0]
        vi2 = names[1]
        
        print("...............")
        sleep(1)
        print("Jetzt sind nur noch", vi1, "und", vi2, "im Pott!")
        sleep(5)
        print(random.choice(names), "ist der Random Wert!")
        
        break
    else:
        print("Ungueltige Eingabe!")
        continue
