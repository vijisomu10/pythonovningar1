"""
2.2 Uppgift 2
Hej där!
• Tryck på File, New file
• Tryck på File, Save as ’HelloName.py’
• I filen skriver vi name = input(’Hejsan! Skriv in ditt namn: ’)
• Sedan skriver vi på raden under print(’Hejsan’+ ’ ’ + str(name))
• Tryck på File, Save
• Tryck på F5 eller ’play’ knappen i höger hörn så körs programmet
Skriv ditt < name > och tryck Enter

Svårighetsgrad 2:  Skriv printsatsen med en f-string istället!
"""

name = input("Hejsan! Skriv in ditt namn: ")
print('Hejsan'+ ' '+str(name))

print(f'Hejsan {str(name)}')