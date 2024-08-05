"""
1. FUNKTIONER #1 
Skriv en funktion som vad en vara kostar! D.v.s. funktionen ska ta in ett pris på en vara, 
exklusive moms, och en momssats i procent. Funktionen ska beräkna priset och sedan returnera värdet.
Calculation rule: (Amount exclusive of VAT) * (100 + VAT percentage as a number) / 100 = Amount inclusive of VAT
"""
def kostnad(varor_pris_utan_VAT):
    momssats_i_procent = int(input('Mata VAT procent for varor: '))
    pris_ingar_VAT = varor_pris_utan_VAT * ((100 + momssats_i_procent)/100)
    return pris_ingar_VAT

varor_pris_utan_VAT = int(input('Skriv en vara kostar: '))
print(kostnad(varor_pris_utan_VAT))


"""
2. FUNKTIONER #2
Skriv en funktion som undersöker hur många stora respektive små bokstäver en sträng har. 
Funktionen ska sedan returnera dessa 2 värden 
"""
#Using dictionaries
#-----------------------------------------------------------------------------
def test_string(bokstaver):
    testa_bokstaver = {'UPPER_CASE': 0, 'LOWER_CASE': 0}

    for alphabetet in bokstaver:
        if alphabetet.isupper():
            testa_bokstaver['UPPER_CASE']+=1
        elif alphabetet.islower():
            testa_bokstaver['LOWER_CASE']+=1
        else:
            pass

    print('Actual string:', bokstaver)
    print('No. of upper case characters:', testa_bokstaver['UPPER_CASE'])    
    print('No. of lower case characters:', testa_bokstaver['LOWER_CASE']) 

bokstaver = input('Skriv en string: ')
test_string(bokstaver)
#-------------------------------------------------------------------------------

#Using loops
#--------------------------------------
def test_string2(astring):    
    count_alpha1 = 0
    count_alpha2 = 0
    for i in astring:
        if i.isupper():
            count_alpha1 += 1
        elif i.islower():
            count_alpha2 += 1
    print(count_alpha1)
    print(count_alpha2)    

astring = input('Enter a string: ')
test_string2(astring)
#----------------------------------------        