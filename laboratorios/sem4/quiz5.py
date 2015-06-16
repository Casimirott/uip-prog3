print("\tStartup ABC\n")
print("\tLista de Supermecados\n")
num=0
lista=[]
print("1.Agregue Productos a la lista")
print("2.Elimine Productos de la lista")
print("3.Ver los Productos de la lista")
print("4.Salir")
while num<=4:
    op=int(input("Ingrese su opcion\n"))
    if op==1:
        inc=input("Ingrese Elemento\n")
        lista.append(inc)
    elif op==2:
        print(lista)
        eli=int(input("Ingrese el numero del elemento a eliminar\n"))
        del lista[eli-1]
    elif op==3:
        print(lista)
