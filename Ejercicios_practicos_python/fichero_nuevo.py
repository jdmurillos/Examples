fcrear=open("ficheronuevo.txt","w")
fcrear.write("Fichero creado desde cero\n")
fcrear.write("Lorem ipsum dolor sir amet, ...")
fcrear.close()

print("### Fichero creado ###")

flectura=open("ficheronuevo.txt","r")
texto=flectura.read()
flectura.close()
print(texto)

