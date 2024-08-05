"""
3. LOOP #3
Skapa ett program där användaren
a.Får mata in två tal.
b.Skriv sedan till skärmen summan av de två talen.
c.Skriv sedan en fråga- Vill du fortsätta(J/N)?.
d.Svarar användaren J återupprepas punkt a-c
e.Svarar användaren N avbryts programmet
"""
while True:     
    num1 = int(input('Enter number 1:'))
    num2 = int(input('Enter number 2:'))      
    sum_2num = num1 + num2
    print(f'Sum of two numbers: {sum_2num}')
    number_game = input('Want to continue? (y/n)').lower()
    if number_game == 'y': 
        continue
    elif number_game == 'n':
        print('Hej då')
    break        
    
"""
4. LOOP #4
Be användaren mata in ett tal. Spara värdet i en variabel. Upprepa detta 10 gånger. För
varje gång lägg till det inmatade värdet till variabelns värde. När det är klart skriv ut-
Summan av det du matat in är: summan.
"""

var_1 = int(input('Write a number: '))
i = 0
for i in range(11):
    var_1 = var_1 + i
print(f'sum of these numbers are {var_1}')


""" summa = 0
for _ in range(10):
    tal = int(input('Write a number: '))
    summa += tal
print(summa) """
