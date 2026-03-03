with open ('input.txt', 'r') as file: 
    righe = file.readlines() 

numero_righe = len(righe) 

print(f"Il file contiene {numero_righe} righe")