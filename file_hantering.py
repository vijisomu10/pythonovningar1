""" with open("myfile.txt", "w", encoding='utf-8') as a:
    #a.write("Den här texten kommer skrivas till filen\n")
    pass """

list_of_numbers = [i for i in range(10)]

with open("myfile.txt",'w', encoding="utf-8") as f:
    for i in list_of_numbers:
        f.write(f'{i},{i**2},{i**3},{i**4}\n')
        
with open('myfile.txt','r', encoding='utf-8') as f:
    my_dict = {}
    exponent = ("kvadrat","kuben","hyperkuben")
    for line in f:
        numbers = line.strip().split(',')
        numbers = [int(i) for i in numbers]
        my_dict[numbers[0]] = {
            key:value for key,value in zip(exponent,numbers[1:])

        }
    print(my_dict)
for key,value in my_dict.items():
    print(key,'ger',value)