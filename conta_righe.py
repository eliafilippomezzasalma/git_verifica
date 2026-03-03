with open ('input.txt', 'r') as file: 
    contenuto = file.read() 
    righe = contenuto.split('\n')

numero_righe = len(righe) 

parole = contenuto.split()
numero_parole = len(parole)

print(f"Il file contiene {numero_righe} righe") 
print(f"Il file contiene {numero_parole} parole") 