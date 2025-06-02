def Lohnberechnung(arbeitsstunden,stundenlohn):
    if arbeitsstunden <=40:
        return arbeitsstunden * stundenlohn
    else:
        overtime = arbeitsstunden - 40
        return 40 * stundenlohn + overtime * (1.4 * stundenlohn)
    
try:
    hours = float(input('Geben Sie Ihre Stunden ein: '))
    pay = float(input('Geben Sie ihren Stundenlohn ein: '))
    
    gross_pay = Lohnberechnung(hours, pay)
    
    print('Gehalt: ' , gross_pay)
    
except ValueError:
    print('Fehler, bitte geben Sie eine Zahl ein')