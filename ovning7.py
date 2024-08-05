# ovning7 och 8
"""
Strängoperatorer
Be användaren mata sitt namn. Lägg det i en variabel som heter namn
Skapa en ny variabel namnUpprepat med namn fem gånger efter varann . Skriv ut den nya variabeln
Vad heter du: Stefan
StefanStefanStefanStefanStefan
"""

namn_1 = input("Vad heter du: ")
print(f'{namn_1*5}')

# ovning8-Jamfor operator
"""
Jämför-operatorer
Skriv ett program som tar ett TAL (int) som input. Det ska skriva ut False om talet är mindre än 100 och True om det är större eller lika med 100, 
OBS: Utan If-satser. (skriv direkt ut resultat från jämförelsen) 
"""
tal_3 = int(input("Skriv ett tal: " ))
print(bool(tal_3<=100))
