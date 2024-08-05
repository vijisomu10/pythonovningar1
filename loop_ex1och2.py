"""
1. LOOP #1
Skapa ett program som skriver ut talen 0-10 på skärmen. Lös detta med en for-loop. Lös den igen med en While-loop
"""

#for loop
print('Using for loop')
i = 0
for i in range(111,120):
    print(i, end='--')
    
#while loop
print('\n''Using while loop')
j = 0
while j<11:
    print(j,end=' ')
    j += 1

"""
2. LOOP #2
Skapa ett program där användaren får mata in två tal. Låt sedan programmet skriva ut alla
tal som finns mellan dessa två tal på skärmen. Lös detta med en for-loop. Lös den igen med en While-loop
"""
print('\nMålet att skriva tal mellan dessa två tal med for-loop')
tal_1 = int(input("Mata tal 1: "))
tal_2 = int(input("Mata tal 2: "))
for i in range(tal_1+1,tal_2):
    print(i, end='--')

print('\nMålet att skriva tal mellan dessa två tal med while-loop')
count = tal_1
while count <= tal_2:
    print(count,end='-')
    count += 1
