print('Temperatura in °C ? ')
tempc = input()

print('La temperatura in °C è di : ' + tempc+'°')

tempf1 = (float(tempc) * 1.8)
tempf = str(tempf1 + 32)
print('La temperatura in °F è di : ' + tempf+'°')

tempk = str(float(tempc) + 273.15)
print('La temperatura in °k è di : ' + tempk+'°')

