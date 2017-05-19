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
    print("Options:\n 1 = Add an item\n 2 = Remove an item\n 3 = Let it go!")
    eingabe = int(input("What`s your choice?: "))
    
    if (eingabe == befehl1):        
        
        print("Now you can add an item: ")
        newn = input("Enter an item: ")
        
        names.append(newn)
        
        print(names)
        
        while grenze < 10:
            inp = int(input("Do you wanna add more items [1=Y/2=N]?"))
              
            if (inp == m1):
                print("Now you can add an item: ")
                newn = input("Enter an item: ")
        
                names.append(newn)
        
                print(names)
                grenze = grenze + 1 
                continue
             
            elif (inp == m2):
                print("Your list contains", len(names), "items!")
                break
                
            else:
                print("Error!")
                continue        
    
    elif (eingabe == befehl2):
        
        print("Now you can delete items: ")
        out = input("Which item do you want to remove: ")
        
        names.remove(out)
        
        print(names)
        print("Your list contains", len(names), "items!")
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
            print(aussuche, "isn`t the random item!")
            names.remove(aussuche)
            spanne = spanne - 1
        
        vi1 = names[0]
        vi2 = names[1]
        
        print("...............")
        sleep(1)
        print("Now there are only", vi1, "and", vi2, "in the pot!")
        print("...............")
        sleep(5)
        print(random.choice(names), "is the random item!")
        
        break
    else:
        print("Error!")
        continue
