"""
STRÄNGHANTERING
1. STRING #1
Empty string!
"""
name1 = ''
print(f'name1 : {name1}')
 
name2 = ""
print(f'name2 : {name2}')
 
name3 = str()
print(f'name3 : {name3}')

"""
2. STRING #2
Du har en strängvariabel som innehåller följande text, ”Hello, world”
 Ta med hjälp av kod ut första förekomsten av bokstaven w
Skriv ut vilken position bokstaven w har i strängen (H har position 0). Ta fram positionen genom kod.
"""
string_variable = 'Hello, world'
str111 = string_variable[:6]
print(str111)
print(len(str111))
print(string_variable.index('w'))

"""3. STRING #3
Du har strängen string namn="kurt andersson";
Skriv kod så att förnamn och efternamn i variabeln namn börjar med stora bokstäver.
Resultatet skall bli så här "Kurt Andersson"
"""
string_namn = "kurt andersson"
print(string_namn.title())

"""
4. STRING #4
Du har en sträng med texten ”Detta är en sträng som du skall ändra”. Ersätt via kod
alla blanktecken i strängen med tecknet * . Räkna sedan ut via kod hur många
förekomster det finns av tecknet * i strängen.
"""
string_text = 'Detta är en sträng som du skall ändra'
strtext = string_text.replace(' ', '*')
print(strtext)

"""
5. STRING #5
Be användaren mata in en mailadress. Programmet skall kontrollera att inmatningen är
rätt dvs att det finns ett @ tecken och att det finns en . med 2 eller 3 tecken efter.
Meddela användaren om det är rätt eller felaktig adress
"""


"""
6. STRING #6
 Gör ett program där användaren får mata in en mening t ex ”Detta är min text
som jag matar in”. Programmet skall räkna ut hur många ord meningen består av
och meddela användaren om detta.
"""
mata_text = input('Skriv en mening: ')
m = mata_text.split()
print(len(m))

"""
7. STRING #7
Be användare mata in ett ord eller en mening. Programmet skall kontrollera om det
ordet är en palindrom dvs om ordet blir likadant om man läser framifrån och bakifrån.
Exempel på palindrom är namn som ”anna” eller ”otto” eller en mening som ”ni talar
bra latin”. Meddela användaren om det är en palindrom eller ej.
"""

vanlig_text = input('Mata i ett ord eller en mening: ').replace(' ' , '')
check = ""
for i in vanlig_text:
    check = i + check
if vanlig_text == check:
    print('yes')
else:
    print('no')
