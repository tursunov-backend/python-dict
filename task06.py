kalit = input('kalit: ')

text = {
    'kalit1': 'salom',
    'kalit2': 'hi',
    'kalit3': 1991,
    'kalit4': 1234,
    'kalit5': 'alik'
}

if kalit in text:
    print(text[kalit])
else:
    print('Topilmadi')
