"""
Skriv en function som tar emot en månadslön och beräknar årskomsten efter skatt.

Tjänar man mindre än 190.000 betala man bara 21% skatt
Tjänar man mellan 190.000 och 450000 tillämpas 31% skatt
Tjänar man över 450.000 om året så tillämpas 44% på allt,
man tjänar över 450.000, men bara 31% på allt upp till 450000
"""
def salary(monthly_salary):      
    income_per_year = monthly_salary * 12

    if income_per_year < 190000:
        yearly_income_after_tax = income_per_year*(1 - 0.21)
        #yearly_income_after_tax = (income_per_year*79)/100

    elif 190000 <= income_per_year <= 450000:
        yearly_income_after_tax = income_per_year * (1 - 0.31)

    else:
        upp_till_450000 = 450000 * (1 - 0.31)
        #income_more_than_450000 = income_per_year - 450000        
        after_tax_more_than_450000 = (income_per_year - 450000) * (1 - 0.44)   
        yearly_income_after_tax = upp_till_450000 + after_tax_more_than_450000
    
    return yearly_income_after_tax


monthly_salary = float(input("How much do you earn per month? "))
print(f'Yearly income after tax: {salary(monthly_salary)}')


