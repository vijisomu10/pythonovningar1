"""
2. IF #2
Be användaren att mata in hur många paket mjölk som finns kvar. Är det mindre än
10 skriv- Beställ 30 paket. Är det mellan 10 och 20 skriv- Beställ 20 paket. Annars
skriv-Du behöver inte beställa någon mjölk.
"""

milk_packet = int(input('How many packets of milk left out? '))
 
if milk_packet < 10:
    print('buy 30 milk packets more')
elif 10 < milk_packet < 20:
    print('buy 20 milk packets')
else:
    print('No need to buy milk')
