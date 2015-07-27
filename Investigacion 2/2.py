import socket
nombre_equipo = socket.gethostname()
direccion= socket.gethostbyname(nombre_equipo)
print("Tu IP es: " +str(direccion))
