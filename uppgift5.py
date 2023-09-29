"""Tre luringar!
• Tryck på File, New file
• Tryck på File, Save as ’TreLuringar_1.py’
• I filen skriver vi print(’Skriv in tre heltal!’)
• Under skriver vi num1 = input(’Skriv tal 1: ’)
• Under det skriver vi num2 = input(’Skriv tal 2: ’)
• Under det skriver vi num3 = input(’Skriv tal 3: ’)
• Under det skriver vi print(f’Att {num1} är större än {num2} är {num1>num2}’)
• Under det skriver vi print(f’Att {num2} är större än {num3} är {num2>num3}’)
• Under det skriver vi print(f’Att {num3} är större än {num1} är {num3>num1}’)
• Under det skriver vi
print(f’Medelvärdet av {num1} , {num2} och {num3} är {(num1+num2+num3)/3}’)
• Tryck på File, Save
• Tryck på F5 eller ’play’ knappen i höger hörn så körs programmet
Svårighetsgrad 2
– Skriv ut talen i ordningen störst till minst
– Kontrollera om användaren skrev in negativa tal, om så fallet, skriv ut detta
med ett fint meddelande till användaren!
– Kontrollera om något/alla talen är lika. Om så fallet berätta det för användaren
"""

print('Skriv in tre heltal: ')
num1 = int(input('Skriv tal1: '))
num2 = int(input('Skriv tal2: '))
num3 = int(input('Skriv tal3: '))

if num1 == num2 or num2 == num3 or num3 == num1:
    print('numret ar likadant') 
if num1>0 and num2>0 and num3>0:
    print(f'Att {num1} är större än {num2} är {num1>num2}')
    print(f'Att {num2} är större än {num3} är {num2>num3}')
    print(f'Att {num3} är större än {num1} är {num3>num1}')
    print(f'Medelvardet av {num1}, {num2} och {num3} ar {(num1+num2+num3)/3}')
else:
    print('please write any whole number from 1 not decimal numbers')


nummer12 = [num1, num2, num3]
nummer12.sort(reverse=True)
print('Descending order', nummer12)

""" nummer12 = (num1, num2, num3)
while nummer12 <= 2 :
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3:
        print(num2)    
    else:
        print(num3) """


