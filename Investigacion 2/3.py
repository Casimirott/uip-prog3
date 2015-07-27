import MySQLdb
bd = MySQLdb.connect("localhost","casimirott","losdelsur","lmfao" )
cursor = bd.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("1.insertar Datos")
print("2.Eliminar Datos")
print("3.Actualizar Datos")
while op<=3
  op=input("Ingrese su opcion: ")
  if op==1:
    dato = raw_input("Dato: ")
    query = "INSERT INTO b (b2) VALUES ('%s')" % dato
    run_query(query)
  if op==2:
    criterio = raw_input("Ingrese criterio p7 eliminar coincidencias: ")
    query = "DELETE FROM b WHERE b2 = '%s'" % criterio
    run_query(query)
  if op==3:
    b1 = raw_input("ID: ")
    b2 = raw_input("Nuevo valor: ")
    query = "UPDATE b SET b2='%s' WHERE b1 = %i" % (b2, int(b1))
    run_query(query)
bd.close()
