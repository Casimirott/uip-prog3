print("1.Introducir un Texto")
print("2.Cifrar el Texto introducido")
print("3.Descifrar el Texto introducido")
print("4.Imprimir")
z=0
cifro=[]
desc=[]
while z<=4:
	z=int(input("Ingrese su opcion: "))
	if z==1:
		x=input("Introduzca su Texto: ")
	elif z==2:
		n=x
		p=0
		while p < len(n):		#Estoy recorriendo la longitud de la cadena
			l=n[p]			#Asigno la letra a una variable
			k=ord("l")		#Saco el entero de la letra
			u=k+1			
			o=chr("u") 		#Saco el caracter del entero
			cifro[p]=u		#Guardo el entero en una lista
			p+=1	
	elif z==3:
		h=0
		while h < len(cifro):		#Recorro el texto cifrado
			v=cifro[h]		#Asigno el entero a una variable
			e=v-1
			q=chr("e")		#Saco el caracter del entero
			r=ord("q")		#Convierto el caracter del entero
			desc[h]=r		#Guardo el caracter en una lista
			h+=1
	elif z==4:
		print(x+"\t"+cifro+"\t"+desc)
