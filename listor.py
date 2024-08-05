"""
1. LIST #1
Skapa ett program där användaren får upp fyra frågor om att mata in ett tal. Spara alla talen i en lista. 
Loopa igenom lista och ta fram det tal som är störst. 
Skriv tillbaka resultatet på skärmen för användaren
"""
""" 
num1 = int(input('Skriv din ålder: '))
num2 = int(input('Vad är din favorit nummer? '))
num3 = int(input('Hur många syskon/bror har du? '))
num4 = int(input('Hur många vänner har du? '))
new_list = [num1, num2, num3, num4]
print(new_list)

#print(max(new_list))

störst = new_list[0]
for x in new_list:
    if x > störst:
        störst = x
print(f'Största tal i listan: {störst}')         
 """
""" #other way to solve 
lista = []
length = 4
while len(lista) < length:
    item = input('Knappa in 4 tal: ')
    if item not in lista:
        lista.append(item)
print(max(lista)) """


"""
2. LIST #2
Vi bygger ett schackbräde:
board = []
for i in range(8):
   row = [‘ ‘ for i in range(8)]
   board.append(row)
a)	placera ut bönder (lilla ‘b’)  på rad 2 och rad 7
b)	skriv ut schackbrädet 
c)	googla på  python termcolor module och se om du kan skriva ut svarta bönder och vita bönder!
"""

""" from termcolor import colored

empty_list = 8*[' ']
board = [empty_list[:] for i in range(8)]

for i in range(8):
    for j in range(8):
        if (j+i) % 2 == 0:
            färg = 'on_white'
        else:
            färg = 'on_black'
        
        if i == 1:
            ruta = colored('b', color='light_grey', on_color=färg)
        elif i == 6:
            ruta = colored('b', color='dark_grey', on_color=färg)
        else:
            ruta = colored(' ', on_color=färg)
        board[i][j] = ruta

for row in board:
    for item in row:
        print(f'item', end=' ')
    print() """

"""
Dictionary
Skriv en bankapplikation. Skriv först en meny med följande val:  
Skapa konto
Ta bort konto
Lista alla kontonummer
Lista totalsaldo
Lista alla kontonummer och saldo
"""

konto_dictionary = {}

while True:
    print('\nVälkommen till STI bank meny\n')
    meny_val = input(f'Välja en tjänst: \n'
                     f'1. Skapa konto\n' 
                     f'2. Ta bort konto\n'
                     f'3. Lista alla kontonummer\n'
                     f'4. Lista totalsaldo\n'
                     f'5. Lista alla kontonummer och saldo\n'
                     f'6. Avsluta\n'
                     f'Tryck någon siffror: ')                    

    if meny_val == '1':
            
        skapa_konto = input('Skriv ditt personnummer: ')

        if skapa_konto in konto_dictionary:
            print('Personnummer redan finns i listan!')
            
        else:
            ny_konto_namn = input('Ange konto namn: ')
            konto_adress = input('Ange konto adress: ')
            konto_saldo = input('Lägg din saldo: ')
            konto_dictionary[skapa_konto] = ny_konto_namn, konto_adress, konto_saldo
            continue    
            
    elif meny_val == '2':
        print('Ta bort konto')
        del_konto = input('Skriv ditt personnummer att avsluta konto: ')
        del konto_dictionary[del_konto]
        print('Konton deleted successfully\n')
        print(konto_dictionary)
            
    elif meny_val == '3':
        print(f'Här finns listan med alla kontonummer:')
        for key,value in konto_dictionary.items():
            ny_konto_namn, konto_adress, konto_saldo = value
            print(key)
            
    elif meny_val == '4':
            pass
            
    elif meny_val == '5':
            pass
            
    elif meny_val == '6':
            break

    else:
            print('välja en siffror mellan 1 till 6!')
            continue
