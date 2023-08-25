while True:
    try:
        numero_decimal = abs(int(input('Introduce un numero entre 1 y 3999')))
        if numero_decimal > 3999:
            raise ValueError
        elif numero_decimal == 0:
            raise ValueError
        break
    except:
        print('Numero no válido')

numero_cadena = str(numero_decimal)
numero_ceros = numero_cadena.zfill(4)
numero_lista = list(numero_ceros)


print('numero lista', numero_lista)

try:
    unidades = int(numero_lista[-1])
    decenas = int(numero_lista[-2])
    centenas = int(numero_lista[-3])
    unidades_millar = int(numero_lista[-4])
except:
    pass

#print('unidades {} decenas {} centenas {} millares {}'.format(unidades,decenas,centenas,unidades_millar))

# CONVERSOR

def conversor(self):
    ud_roma = []
    if self == 1:
        ud_roma = 'I'
    elif self == 2:
        ud_roma = 'II'
    elif self == 3:
        ud_roma = 'III'
    elif self == 4:
        ud_roma = 'IV'
    elif self == 5:
        ud_roma = 'V'
    elif self == 6:
        ud_roma = 'VI'
    elif self == 7:
        ud_roma = 'VII'
    elif self == 8:
        ud_roma = 'VIII'
    elif self == 9:
        ud_roma = 'IX'
    else:
        ud_roma = ''
    
    return ud_roma

# UNIDADES
 
ud_romana = conversor(unidades)


# DECENAS

dc_roma = conversor(decenas)
if decenas == 9:
    dc_romana = 'XC'
else:
    dc_romana = dc_roma.replace('I','X').replace('V','L')


# CENTENAS

cn_roma = conversor(centenas)
if centenas == 9:
    cn_romana = 'CM'
else:
    cn_romana = cn_roma.replace('I','C').replace('V','D')


# MILLARES

ml_roma = conversor(unidades_millar)
ml_romana = ml_roma.replace('I','M')



numero_romano = ml_romana + cn_romana + dc_romana + ud_romana
print('El numero {} en numeracion romana es {}'.format(numero_cadena,numero_romano))

#print('ROMANAS unidades {} decenas {} centenas {} millares {}'.format(ud_romana,dc_romana,cn_romana,ml_romana))
