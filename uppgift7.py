"""Uppgift 7
He who seek he finds!
Skriv ett program som gör följande:
• Fråga användaren efter ett sökord.
• Skriv ut alla rader i sample.txt som innehåller detta sökord."""  

""" with open('sample1.txt', 'r', encoding='utf-8')as f:
    word_search = input('Write a word to search in the sample text: ')
    read_the_file = f.readlines()
    for line in read_the_file:
        if line.find(word_search) != -1:
            print(word_search , 'string exists')
            print('Line number: ', read_the_file.index(line))
            print('Line:', line)
 """
"""
Uppgift 8
Ändra innehållet!!!!
Skriv ett program som gör följande:
• Fråga användaren efter en sträng och en ersättningssträng.
• Ersätt alla förekomster av strängen i sample.txt med ersättningssträngen.
"""
""" with open ('sample.txt', 'r', encoding='utf-8') as f:
    read_data = f.read()
    input_string = input('Write a string from the file: ')
    output_string = input('Replace string for the new: ')
    read_data = read_data.replace(input_string,output_string)

with open ('sample.txt', 'w', encoding='utf-8') as f:
    f.write(read_data)
    print('text replaced') """

"""
Uppgift 9
Sortering är moderjords önskan
Skriv ett program som gör följande:
• Läs alla rader i sample.txt, sortera dem och skriv sedan tillbaka dem sorterade till filen."""

""" with open('sample.txt', 'r', encoding='utf-8') as f:    
    read_data = sorted(f.readlines())
    print(read_data)
 """
""" with open('sample.txt', 'w', encoding='utf-8') as f:
    for item in read_data:
        print(f.write("%s" % item)) """


""" while len(read_the_file) != 0:
        print(read_the_file, end='') 
        for item in names:
        # write each item on a new linepip -r 
        fp.write("%s\n" % item)
    print('Done')
    """
"""
Uppgift 10
Statistiken
Skriv ett program som gör följande:
• Beräkna och skriv ut antalet ord, antalet unika ord och 
frekvensen av varje ord i sample.txt."""

count = 0
words_dict = dict()
with open('sample.txt', 'r', encoding='utf-8') as f:       
    for line in f: 
        line = line.split(" ")        
        count = count + len(line)
    print(f'Total number of words in the text file: {count}')
    
with open('sample.txt', 'r', encoding='utf-8') as f:       
    for word_line in f:
        word_trunc = word_line.strip().lower().split(" ")     
        for unique_single_word in word_trunc:
            if unique_single_word in words_dict:
                words_dict[unique_single_word] = words_dict[unique_single_word] + 1
            else:
                words_dict[unique_single_word] = 1

for key in list(words_dict.keys()):
    print(key, ":", words_dict[key])