import random

n = random.randint(1,10)
zahl = 1

while zahl > 0:
    
    n = random.randint(1,10)
    zahl = int(input("rate mal was das für eine zahl ist > "))
    
    if zahl == n:
        print("JA")
    else:
        print("NEIN")