"""Chat with me!
• Tryck på File, New file
• Tryck på File, Save as ’ChatWithMe_1.py’
• I filen skriver vi MY_NAME = ’< name >’ Ditt egna namn alltså! Notera understrecket
• Under skriver vi MY_AGE = < age > Din ålder, notera int() och understrecket
• Under det skriver vi MY_HOBBY = < hobby > Din hobby, notera understrecket
• Under det skriver vi name = input(’Skriv in ditt namn: ’)
• Under det skriver vi age = int(input(’Skriv in din ålder: ’))
• Under det skriver vi hobby = input(’Skriv in din favorithobby: ’)
• Under det skriver vi print(f’Hejsan {name}, mitt namn är {MY_NAME}.’)
• Under det skriver vi print(f’Du är {age} gammal och jag är {MY_AGE}.’)
• Under det skriver vi print(f’Jag gillar {MY_HOBBY} och du gillar{hobby}.’)
• Under det skriver vi print(f’Trevligt att pratas vid {name}, hoppas vi hörs snart igen!’)
• Tryck på File, Save
• Tryck på F5 eller ’play’ knappen i höger hörn så körs programmet
Skriv ett fake-< name > och tryck Enter
Skriv en fake-< age > och tryck Enter
Skriv en fake-< hobby > oich tryck Enter
Svårighetsgrad 2
– Skriv ut namnen med stora bokstäver!
– Beräkna skillanden i ålder och avgör om du är äldre eller yngre än användaren.
– Svara användaren om ni har samma hobby eller inte!
"""
my_name = 'Viji'
my_age = 42
my_hobby = "puzzle"
name = input("Skriv i ditt namn: ")
age = int(input("Skriv i din ålder: "))
hobby = input("Skriv i din favorithobby: ")

print(f'Hejan {name.upper()}, mitt namn är {my_name.upper()}')

print(f'Du är {age} gammal och jag är {my_age}')
if my_age >= age:
    print("You are younger than me")
else:
    print("You are older than me")

print(f'Jag gillar {my_hobby} och du gillar {hobby}')
if my_hobby == hobby:
    print("We have same hobby")
else:
    print('We have different hobbies')
    
print(f'Trevligt att pratas vid {name}, hoppas vi hörs snart igen!')
