"""
7. IF #7
Be användaren att mata in namnet på ett land där den bor. Om det är Sverige,
Danmark, eller Norge skall användare informeras att-Du bor i Skandinavien. Om
inte meddela användaren att den inte bor i Skandinavien.
"""
scandinavian_stad = ["sverige", "denmark", "norge"]
land_curLocation = input("Hej anvandaren, vilken land du bor nu? ").lower()
print(land_curLocation)

if land_curLocation in scandinavian_stad:
    print("Du bor i scandinavan")
else:
    print('Du bor inte i scandinavian')