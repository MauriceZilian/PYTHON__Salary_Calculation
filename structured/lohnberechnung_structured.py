def lohnberechnung(arbeitsstunden, stundenlohn):
    """
    Berechnet das Gehalt basierend auf Arbeitsstunden und Stundenlohn.
    Für Überstunden (über 40 Std.) wird ein Zuschlag von 40% gezahlt.
    """
    if arbeitsstunden <= 40:
        return arbeitsstunden * stundenlohn
    else:
        overtime = arbeitsstunden - 40
        return 40 * stundenlohn + overtime * (1.4 * stundenlohn)

def main():
    try:
        hours = float(input('Geben Sie Ihre Stunden ein: '))
        pay = float(input('Geben Sie Ihren Stundenlohn ein: '))
        
        gross_pay = lohnberechnung(hours, pay)
        print('Gehalt: ', round(gross_pay, 2))
    except ValueError:
        print('Fehler, bitte geben Sie eine gültige Zahl ein')

if __name__ == "__main__":
    main()
