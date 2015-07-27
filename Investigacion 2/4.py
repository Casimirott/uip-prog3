import sys
import serial
def scan(num_ports = 20, verbose=True):
	 dispositivos_serie = []
	 if verbose:
		 print ("Escanenado %d puertos serie:" % num_ports)
	   for i in range(num_ports):
		 if verbose:
		   sys.stdout.write("puerto %d: " % i)
		 sys.stdout.flush()
		 try:
		   s = serial.Serial(i)
		 if verbose: print "OK --> %s" % s.portstr
		 dispositivos_serie.append( (i, s.portstr))
		 s.close()
	 	except:
		   if verbose: print "NO"
 	 	pass
		 return dispositivos_serie
 if __name__=='__main__':
   puertos_disponibles=scan(num_ports=20,verbose=True)
   print ("Puertos detectados:")
 	if len(puertos_disponibles)!=0:
	   for n,nombre in puertos_disponibles:
		 print ("  (%d) %s" % (n,nombre))
	else:
	   print ("  Ninguno")
