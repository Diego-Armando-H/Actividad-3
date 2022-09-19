def signoZodiacal(mes, dia):
    if(mes == 1):
        if(dia < 20):
            return "Capricornio"
        return "Acuario"
    if(mes == 2):
        if(dia < 19):
            return "Acuario"
        return "Piscis"
    if(mes == 3):
        if(dia < 21):
            return "Piscis"
        return "Aries"
    if(mes == 4):
        if(dia < 20):
            return "Aries"
        return "Tauro"
    if(mes == 5):
        if(dia < 21):
            return "Tauro"
        return "Géminis"
    if(mes == 6):
        if(dia < 21):
            return "Géminis"
        return "Cancer"
    if(mes == 7):
        if(dia < 23):
            return "Cancer"
        return "Leo"
    if(mes == 8):
        if(dia < 23):
            return "Leo"
        return "Virgo"
    if(mes == 9):
        if(dia < 23):
            return "Virgo"
        return "Libra"
    if(mes == 10):
        if(dia < 22):
            return "Libra"
        return "Escorpio"
    if(mes == 11):
        if(dia < 23):
            return "Escorpio"
        return "Sagitario"
    if(mes == 12):
        if(dia < 23):
            return "Sagitario"
        return "Diciembre"


print("¿Que signo zodiacal eres?\n4")
mes = int(input("Ingrese el mes de nacimiento:\n"))
dia = int(input("Ingrese el día de nacimiento:\n"))

print("El signo zodiacal es: ", signoZodiacal(mes, dia))
