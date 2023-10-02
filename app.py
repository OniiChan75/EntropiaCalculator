#entropy calculator taking text from a text(file)

#open file and read text(text)
with open("test.txt", "r") as file:
    testo = file.read()
    
#calculation of letters
conteggio_lettere = {}
conteggio_carattere = {}

#counting cycle
for carattere in testo:
    if carattere.isalpha():
        if carattere in conteggio_lettere:
            conteggio_lettere[carattere] += 1
        else:
            conteggio_lettere[carattere] = 1
    else:
        if carattere in conteggio_lettere:
            conteggio_carattere[carattere] += 1
        else:
            conteggio_carattere[carattere] = 1
            
#I combine the two dictionaries
conteggio_completo = {**conteggio_lettere, **conteggio_carattere}

#sort the dictionary
conteggio_completo_ordinato = dict(sorted(conteggio_completo.items(), key=lambda x: x[1], reverse=True))

#print the result as output
for carattere, conteggio in conteggio_completo_ordinato.items():
    print(f"'{carattere}': {conteggio}")