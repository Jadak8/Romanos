def get_decimal_number(self=None):
    while True:
        try:
            get_decimal_number = abs(int(input('Introduce un numero entre 1 y 3999\n>')))
            if get_decimal_number > 3999:
                raise ValueError
            elif get_decimal_number == 0:
                raise ValueError
            return get_decimal_number
            break
        except:
            print('Numero no válido')

def decomposition(self):
    number = self
    mil = number // 1000
    cen = (number % 1000) // 100
    dec = (number % 100) // 10
    unit = (number % 10) // 1
    
    number = (mil,cen,dec,unit)
    return number

def translate(mil=0, cen=0, dec=0, unit=0):
    U = ('','I','II','III','IV','V','VI','VII','VIII','IX','X')
    D = ('','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C')
    C = ('','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M')
    M = ('','M','MM','MMM')
    
    number = M[mil]+C[cen]+D[dec]+U[unit]
    return number

number = get_decimal_number()
decomposition_number = decomposition(number)
translate_number = translate(*decomposition_number)
print('El numero traducido es: ',translate_number)

