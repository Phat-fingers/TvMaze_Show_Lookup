def menu():
    print('1. Addera')
    print('2. subtrahera')
    print('3. Gånger')
    print('4. Dela med')
    print('4. Visa en gånger tabell')
    print('5. Avsluta')
def addera(a,b):
    return a + b

def sub(a,b):
    return a - b

def gånger(a,b):
    return a * b

def dela(a,b):
    return a / b

def tabell(i):
    
    for a in range(1,11):
        print(a, '*', i, '=', a*i )
        
tabell(4)
    
    













#print('Nu ska vi räkna lite :)')
# while True:
#     menu()
#     val = int(input('Vad vill du göra? '))