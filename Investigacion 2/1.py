import MySQLdb
bd = MySQLdb.connect("localhost","casimirott","losdelsur","lmfao" )
cursor = bd.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Versión Base de Datos : %s " % data)
bd.close()
