print('COVERTING TEMPERATURE FROM CELCIUS\n')

celcius = float(input('Input the temperature (celcius): '))

print('='*37)

print('Temperature in celcius    = ', celcius, '°C')

reaumur = (4/5) * celcius
print('Temperature in reaumur    = ', reaumur, '°R')

fahrenheit = ((9/5) * celcius) + 32
print('Temperature in fahrenheit = ', fahrenheit, '°F')

kelvin = celcius + 273
print('Temperature in kelvin     = ', kelvin, 'K')
