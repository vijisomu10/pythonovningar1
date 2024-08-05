"""5. LOOP #5
Skapa ett program där användaren får mata in ett tal. Låt sedan programmet skriva ut
alla siffor som är mindre än det inmatade talet men större än 0. Lös detta med en
loop.
"""
mindre_tal = int(input('Skriv ett heltal: '))
for i in range(1,mindre_tal):
    print(i, end='-')    
    i += 1  
    
print('\n')
i = 1
while i < mindre_tal:
    print(i,end='--')
    i += 1

    
"""
6. LOOP #7 (Överkurs)
Rolling the dice
Kasta två tärningar” och visa resultatet enligt skärmdump ända tills man INTE svarar ”y” eller ”yes” på frågan om igen"""


