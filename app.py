#entropy calculator taking text from a text(file)

#open file and read text(text)
with open("test.txt", "r") as file:
    testo = file.read()
    
#calculation of letters
conteggio_lettere = {}
conteggio_carattere = {}
lunghezza_testo = len(testo)

#counting cycle
for carattere in testo:
    if carattere.isalpha():
        if carattere in conteggio_lettere:
            conteggio_lettere[carattere]['conteggio'] += 1
        else:
            conteggio_lettere[carattere] = {'conteggio':1, 'percentuale':0}
    else:
        if carattere in conteggio_lettere:
            conteggio_carattere[carattere]['conteggio'] += 1
        else:
            conteggio_carattere[carattere] = {'conteggio': 1, 'percentuale': 0}
            
#I combine the two dictionaries
conteggio_completo = {**conteggio_lettere, **conteggio_carattere}

#calculation of the percentage
for lettera, info in conteggio_completo.items():
    info['percentuale'] = (info['conteggio'] / lunghezza_testo) * 100

#sort the dictionary
conteggio_completo_ordinato = dict(sorted(conteggio_completo.items(), key=lambda x: x[1]['percentuale'], reverse=True))

#print the result as output
for carattere, info in conteggio_completo_ordinato.items():
    print(f"'{carattere}': Conteggio: {info['conteggio']}, Percentuale: {info['percentuale']:.2f}%")