import time
produkter = {}
while True:
    Välj = input(f'Välj mellan dessa tre alternativ: \n'
                 f'1: Skapa en ny produktion\n'
                 f'2: Lista alla produkter\n'
                 f'3: Avsluta\n'
                 f'Svara med endast (1/2/3): ')
    
    if Välj == '1':
        skapa_ny_produkt = input("Mata in produkt ID, 5 siffror.")

        if skapa_ny_produkt in produkter:
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Denna produkt finns redan med i listan!")
            time.sleep(1.5)
            print("Försök igen...")
        else: 
            Ny_produktNamn = input("Ange produktens namn: ")
            Produkt_pris = input("Ange produktens pris: ")
            produkter[skapa_ny_produkt] = Produkt_pris, Ny_produktNamn
            continue

    elif Välj == '2':
        print(f'Här är alla produkter: ')
        print(f'Här är alla produkter: ')
        for key,value in produkter.items():
            Produkt_pris, Ny_produktNamn = value
            print(key,Produkt_pris,Ny_produktNamn)

    elif Välj == '3':
        break

    else:
        print("Fel inmatning, använd dig endast av 1,2 eller 3!")
        continue