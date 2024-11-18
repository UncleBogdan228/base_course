fio = 'Чехута Влад Халахупович'
print(fio)
fioup = fio.upper()
fio_up_list = [el for el in fioup]
print(fio_up_list)
fiolow = fio.lower()
fio_low_list = [el for el in fiolow]
print(fio_low_list)
fioup_codes= [ord(symbol) for symbol in fio_up_list]
print(fioup_codes)
fiolow_codes = [ord(symbol) for symbol in fio_low_list]
print(fiolow_codes)
print('Сумма элементов:', sum(fioup_codes) + sum(fiolow_codes))