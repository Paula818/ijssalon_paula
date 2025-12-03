prijzen = {
    'aardbei': 3,
    'vanille' : 4,
    'chocolade' : 5
}
aanbieding = prijzen['aardbei'] * 0.8
reclame_tekst = f'Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}'
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
el = ['VANDAAG', 'IN', 'DE', 'AANBIEDING:', 'VANILLE-IJS,', '1', 'LITER', 'SLECHTS', '€2.40']
el = [item.lower() for item in el]
for item in el:
    if len(item) >= 5:
        print(item.upper())
    else:
        print(item.lower())