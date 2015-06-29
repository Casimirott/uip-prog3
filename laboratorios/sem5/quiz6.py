print("\tDirectorio Telefonico\n")

print("1.Imprimir numeros de telefono")

print("2.Agregar numeros de telefono")

print("3.Eliminar numeros de telefono")

print("4.Buscar numeros de telefono")

print("5.Salir")
dir={}
op=0
while op<=4:

	op=int(input("Ingrese su opcion\n"))
    
	if op==1:

		print(dir)
	elif op==2:
		nom=input("Ingrese su nombre\n")
        
		num=input("Ingrese su numero\n")  
		dir[nom]=num  
	elif op==3:

		bor=input("Nombre: ")
		del dir[bor]       
	elif op==4:

		nom=input("Ingresa el nombre: ")
		print(dir[nom])
print("Adios")	