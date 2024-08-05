"""8. IF #8
Be användaren mata in en summa på hur mycket pengar den har. Be sedan
användaren att ange om den har rabatt.
Om summan är mellan 15 och 25 och användaren inte har rabatt skriv – Du kan köpa en liten hamburgare.
Om summan är mellan 15 och 25 och användaren har rabatt skriv – Du kan köpa en liten hamburgare och en pommes frites.
Om summan är större än 25 och mindre än eller lika med 50 och användaren inte har rabatt skriv – Du kan köpa en stor hamburgare.
Om summan är större än 25 och mindre än eller lika med 50 och användaren har rabatt skriv – Du kan köpa en stor hamburgare och pommes frites.
Om summan är större än 60 eller om den är 50 och 60 och användaren har rabatt skriv – Du kan köpa ett meal med dryck.
"""

pengar = int(input('Hejsan! hur mycket pengar du har? '))
har_rabbat = input('Har du rabbat?(j/n) ')

if 15 <= pengar <= 25 and har_rabbat == 'n':
    print('Du kan köpa en liten hamburgare.')
elif 15 <= pengar <= 25 and har_rabbat == 'j':
    print('Du kan köpa en liten hamburgare och en pommes frites')
elif 25 < pengar <= 50 and har_rabbat == 'n':
    print('Du kan köpa en stor hamburgare')
elif 25 < pengar <= 50 and har_rabbat == 'j':
    print('Du kan köpa en stor hamburgare och pommes frites')
elif 50 < pengar and har_rabbat == 'j':
    print('Du kan köpa ett meal och dryck') 
else:
    print('välja mellan kategori att köpa mat')