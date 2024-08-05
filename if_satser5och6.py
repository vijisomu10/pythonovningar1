"""
5. IF #5
Be användaren ange vilken kategori den tillhör-vuxen, pensionär, student. Om den är
pensionär eller student kostar resan 20 kr . Om den är vuxen kostar resan 30 kr . Annars
skall användaren informeras att den har angett en felaktig kategori.
"""

print('Category type:\n1. Adult\n2. Student\n3. pensioner')
category = int(input('Choose any option: '))

if category == 3 or category == 2:
    print("Resan kostar 20 kr")
elif category == 1:
    print('Resan kostar 30kr')
else:
    print('Vanligen valja mellan kategori')

"""
6. IF #6
Be användaren mata in sitt födelseår. Om det är större eller lika med 1980 men
mindre än 1990 skriv ut –Du är född på 1980-talet. Om det är mindre än 2000 men
större än eller lika med 1990 skriv ut- Du är född på 1990-talet. Om det är mindre
än 1980 eller större än eller lika med 2000, skriv- Du är inte född på 1990 eller
1980-talen.
"""

född_år = int(input("Hitta vilken talet du föddes! Skriv gärna din födelseår: "))

if 1980 <= född_år < 1990:
    print("Du är född på 1980-talet")
elif 1990 <= född_år < 2000:
    print("Du är född på 1990-talet")
elif 2000 <= född_år or född_år < 1980:
    print("Du är inte född på 1990 eller 1980 talet")
else:
    print("Skriv någon nummer")