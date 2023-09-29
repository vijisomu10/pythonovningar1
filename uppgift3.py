"""
2.3 Uppgift 3
Addera
• Tryck på File, New file
• Tryck på File, Save as ’add.py’
• I filen skriver vi print(’Låt mig addera två tal åt dig!’)
• På raden under skriver vi num1 = input(Skriv in det första talet: ’)
• I filen skriver vi num2 = input(Skriv in det andra talet: ’)
• Sedan skriver vi print(’Summan blir’, int(num1)+int(num2))
• Tryck på File, Save
• Tryck på F5 eller ’play’ knappen i höger hörn så körs programmet
Skriv < num1 > och tryck Enter
Skriv < num2 > och tryck Enter

Svårighetsgrad 2– Skriv printsatsen med en f-string istället så att utskriften ser ut som följande:
Summan av < num1 > + < num2 > är < Summan > !

Svårighetsgrad 3+ Kräver if/elif/else + google
– skriv ett program som ovan fast som kontrollerar att användaren skrev in
två stycken heltal! Du får inte använda Try/except block
– Villkoren är att om användaren skrev in två heltal så ska summan skrivas
ut och programmet avslutas! Annars ska ett felmeddelande skrivas ut som
berättar om det första eller det andra eller båda inputen inte är heltal därefter
avslutas programmet!
Kolla metoder för strängar!!
"""
#addition
print("Låt mig addera två tal åt dig!")
num1 = input("Skriv in det första talet: ")
num2 = input("Skriv in det andra talet: ")
summan = int(num1) + int(num2)
print("Summan blir: ", summan)
#svårighetsgrad2
print(f'summan av {num1} och {num2} är {int(num1)+int(num2)}')
#print(f'summan av {num1} och {num2} är {summan}')

