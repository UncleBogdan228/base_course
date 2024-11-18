name = 'Анюта Мельникова'
print(name)
sep = '_'
namesep = sep.join(name)
print(namesep)
nameup = namesep.upper()
print(nameup)
nameupcodes= [ord(symbol) for symbol in nameup]
print(nameupcodes)

namelow = namesep.lower()
print(namelow)
namelowcodes = [ord(symbol) for symbol in namelow]
print(namelowcodes)

print('Максимальное число:', max(max(namelowcodes), max(nameupcodes)))
print('Минимальное число:', min(min(nameupcodes), min(namelowcodes)))