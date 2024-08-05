"""
3. IF #3
Be användaren mata in två tal.number1 och number2.
Lagra det STÖRSTA talet av dom två i en tredje variabel, largest
Skriv ut: 
Det största talet är <>
"""

tal_1 = int(input('Skriv nummer 1: '))
tal_2 = int(input('Skriv nummer 2: '))
print(type(tal_1))

if tal_1 > tal_2:
    largest = tal_1
    print('tal 1 ar storst')
else:
    largest = tal_2
    print('tal 2 ar storst')
print(f'Det storsta talet tva nummer ar {largest}')


"""
4. IF #4
Gör likadant fast med TRE nummer"""

tal_3 = int(input('Skriv nummer 3: '))

if tal_1 > tal_2 and tal_1 > tal_3 :
    largest = tal_1
    print('tal 1 ar storst')
elif tal_1 < tal_2 > tal_3 :
    largest = tal_2
    print('tal 2 ar storst')
else:
    largest = tal_3
    print('tal 3 ar storst')

print(f'Det storsta talet av tre numret ar {largest}')
print(type(largest))