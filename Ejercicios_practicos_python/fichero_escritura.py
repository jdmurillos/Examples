print("FICHERO INICIAL")
flectura=open("fichero_practica_1.txt","r")
texto=flectura.read()
flectura.close()
print(texto)

print("INSERTANDO LÍNEA...\n")

fescritura=open("fichero_practica_1.txt","a")
fescritura.write("Nueva línea en el fichero\n")
fescritura.close()
print("FICHERO INICIAL")

flectura=open("fichero_practica_1.txt","r")
texto=flectura.read()
flectura.close()
print(texto)
