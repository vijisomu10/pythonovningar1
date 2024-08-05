"""Uppgift 1 Första filen
Skriv ett program som gör följande:
• Skapa en textfil med namnet sample.txt och lägg till några rader text i den.
• Skriv ett Python-program för att läsa och skriva ut innehållet i denna fil."""

with open ('sample.txt','w', encoding='utf-8') as f:
    multilines = ['Welcome to STI!\n', 
            'Kursen syftar till att de studerande ska få grundläggande kunskaper\n',
             'i programmering med fokus på Python och även en introduktion till \n',
             'andra programmeringsspråk som Java och Scala. Speciell vikt läggs \n',
             'vid att lära sig programmera mot data från olika datakällor och \n',
             'dataformat såsom filer/apier och Excel, JSON, XML, CSV. De studerande\n',
             'kommer dessutom få kunskaper i att använda versionshanteringssystem \n',
             '(GIT) både för egen del och som en del i ett team. Färdigheter i att \n',
             'validera och testa sin kod så de uppfyller krav kommer utvecklas.']
    f.writelines(multilines)

with open('sample.txt', 'r', encoding='utf-8') as f:
    print(f.read())

"""
Uppgift 2
Spara input till senare
Skriv ett program som gör följande:
• Be användaren att skriva in en sträng.
• Skriv denna sträng till en ny textfil med namnet user_input.txt"""

strang = input('\nskriv en strang: ')
#with open ('user_input.txt','w') as f:
with open ('user_input.txt','a') as f:
    f.write(strang)

"""
Uppgift 3
Räkna antal rader
Skriv ett program som gör följande:
• Skriv ett Python-program för att räkna antalet rader i sample.txt."""

with open('sample.txt', 'r' ,encoding='utf-8') as f:   
    total_row = 0
    for single_row in f:
        total_row += 1
        print(f"Total no of rows in a text {total_row}")
        
#for count,line in enumerate(f):
     #   pass
    #print('total lines', count+1)

"""
Uppgift 4
Lägg till i en fil
Skriv ett program som gör följande:
• Be användaren att skriva in en sträng.
• Lägg till denna sträng i slutet av sample.txt."""
with open('sample.txt', 'a', encoding='utf-8') as f:
    add_text = input('Add a text in sample file: ')
    f.write(add_text)

"""
Uppgift 5
Kopiera innehåll från en fil till en annan
Skriv ett program som gör följande:
• Skapa en annan textfil med namnet sample_copy.txt.
• Skriv ett Python-program för att kopiera innehållet från sample.txt till sample_copy.txt."""

with open('sample.txt', 'r', encoding='utf-8') as f, open('sample1.txt', 'a', encoding='utf-8') as f1:
    for lines in f:
        f1.write(lines)

#using shutil import
import shutil
shutil.copyfile('sample.txt', 'sample1.txt')

"""Uppgift 6
Udda
Skriv ett program som gör följande:
• Skriv ett program som läser bara de udda raderna i sample.txt och skriver ut dem."""
""" 
with open ('sample.txt', 'r') as f:     
    i = 1   
    for lines in f.readlines():
        if i%2 != 0:
            print(lines)
        i += 1
 """
with open("sample.txt", "r") as file:
    rader = 0
    for i in file:
        rader += 1
        if rader %2 != 0:
            print(i, end='')