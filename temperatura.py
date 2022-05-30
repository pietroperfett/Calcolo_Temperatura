
    # temperatura.py v2.0.0

print("""Qual'è l'unità di misura della temperatura ?
°C, °F o °K""")

scelta = input("➞ ")

print("Perfetto in quanti gradi "+ scelta +" è la temperatura ?" )

tempc = input("➞ ")


if scelta == 'C':
    print('La temperatura in °C è di : ' + tempc+'°')

    tempfi1 = str((float(tempc) * 1.8) + 32)
    print('La temperatura in °F è di : ' + tempfi1 +'°' )

    tempk = str(float(tempc) + 273.15)
    print('La temperatura in °k è di : ' + tempk+'°')


elif scelta == 'F':
    print('la temperatura in °F è di : '+ tempc +'°')

    tempC = int(tempc) - 32
    tempC1 = str((float(tempC) / 1.8))
    print('La temperatura in °C è di : ' + tempC1+'°')

    tempK1 = str(((float(tempc)- 32) / 1.8)+ 273.15)
    print('La temperatura in °k è di : ' + str(tempK1)+'°')


elif scelta == 'K':
    print('la temperatura in °k è di : '+ tempc +'°')

    tempck = str(float(tempc) - 273.15)
    print('La temperatura in °C è di : ' + tempck+'°')

    tempfk = tempck = str(((float(tempc) - 273.15) * 1.8) + 32)
    print('La temperatura in °F è di : ' + tempfk+'°')


else :
    print("""Mi spiace non sono riuscito a capipre, usa "C", "K" o "F" per indicare l'unità di misura e riprova.""")

#    ██████╗ ██╗███████╗██████╗ ███████╗██╗   ██╗
#    ██╔══██╗╔╗   ██╔══╝██╔══██╗██╔════╝██║   ██║
#    ██████ Grazie Per leggere il Codice █║   ██║
#    ██╔══╝  ██║  ██║   ██║  ██║██╔══╝  ██║  ██╔╝
#    ██║     ██║  ██║   ██████╔╝███████╗ ╚████╔╝
#    ╚═╝     ╚═╝  ╚═╝   ╚═════╝ ╚══════╝  ╚═══╝

    # @piteasy on telegram
