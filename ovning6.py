#ovning 6 med flytttal
"""
Operators
Skapa en applikation där användaren matar in två tal (heltal!)
 Skriv in Mata in tal 1:
Ta emot detta tal i en variabel
Skriv in Mata in tal 2:
Ta emot värdet på detta tal
Nu ska ni göra massa beräkningar på dessa tal. OBS: lägg resultat i en variabel innan ni skriver ut
resultat = tal1 * tal2
räkna tal1 upphöjd till tal 2 och skriv ut 
räkna tal1 gånger tal 2 och skriv ut 
räkna tal1 delat med tal 2 och skriv ut  (OBS!!! Kolla datatypen på resultat)
räkna tal1 plus tal 2 och skriv ut 
räkna tal1 minus tal 2 och skriv ut 
räkna tal1  heltalsdividerat (%)  tal 2 och skriv ut 
räkna ut resten från heltalsdivision (//) mellan tal1 och  tal 2 och skriv ut 

"""
tal_1 = float(input('Tal 1: '))
tal_2 = float(input('Tal 2: '))
p = f'{tal_1 * tal_2}'
print('Total =', p)

print("Upphojd tal = "f'{tal_1**tal_2}')

print("Delat med = " f'{tal_1/tal_2}')

print("Plus = " f'{tal_1+tal_2}')

print("Minus = " f'{tal_1 - tal_2}')

print("Heltalsdividerat = " f'{tal_1%tal_2}')

print("Heltalsdivision = " f'{tal_1//tal_2}')

