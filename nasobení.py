import random

spravne = 0
spatne = 0
a = 0
b=0


def scitani():
    global prikald ,a ,b
    a = random.randint(1,100)
    b = random.randint(1,100)
    prikald = f"{a} + {b}= "
    vysledek = a + b
    return vysledek
    
def odcitani():
    global prikald ,a ,b
    a = random.randint(1,100)
    b = random.randint(1,100)    
    prikald = f"{a} - {b}= "
    vysledek = a - b
    return vysledek

def nasobeni():
    global prikald ,a ,b
    a = random.randint(1,100)
    b = random.randint(1,10)
    prikald = f"{a} * {b}= "
    vysledek = a * b
    return vysledek
    
def deleni():
    global prikald ,a ,b
    a = random.randint(1,10)
    b = random.randint(1,10)
    a = a * b
    prikald = f"{a} / {b}= "
    vysledek = a / b
    return vysledek
    
def mocneni():
    global prikald ,a ,b
    a = random.randint(1,10)
    prikald = f"{a}^2= "
    vysledek = a **2
    return vysledek
    
def odmocneni(): 
    global prikald ,a ,b
    cisla = [4,0,25,36,64,49,81,]
    a = random.choice(cisla)
    prikald = f" 2 domcnina z {a} = "
    vysledek = a **(1/2)
    return vysledek

funkce = [scitani,mocneni,odmocneni,deleni,nasobeni,odcitani]

def kontrola(vysledek,zadání):
    global spravne,spatne
    
    if vysledek == zadání:
        print(" ")
        print("ty si ale šikulka")
        spravne += 1
        
    else: 
        print(" ")
        print("boužel ses pletl")
        print(f"správný výsledke je : {vysledek}")
        spatne += 1

for i in range(10):
    vybranafunkce = random.choice(funkce)
    vysledek = vybranafunkce()
    print(" ")
    vasvysledek= int(input(prikald))
    kontrola(vysledek,vasvysledek)
print(f" ")
print(f"správně: {spravne}")
print(f"sptane: {spatne}")
print(" ")


