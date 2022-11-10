#Rios:
rios = {'Misisipi': 'Minesota','Amazonas':'Colombia','Rio de la plata':'Argentina', 'Nilo':'Sudan','Senegal':'Mali'}
print(rios)


#Imprimir oraciones de rios:
for keys, paises in rios.items():    
    
        print("\nEl rio:",keys, "Recorre a travez de", paises)


#Nombre de cada rio:
print(f"Los rios son: {rios.keys()}")

#Nombre de cada pais:

print(f"Los paises son: {rios.values()}")


#Glosario:
glosario = {'bucles':'secuencia que se repite' , 'Ciclos':'Secuencia de instrucciones', 'variable' :'Almacenar datos', 'int' :'variable tipo entero' , 'java' :'Interprete de un lenguaje'}

for keys, palabras in glosario.items():#ciclo que hace la separacion por intems del diciconario, e imprime llavez = habitacion y el contenido = huesped
    print (keys,':', glosario[keys])
