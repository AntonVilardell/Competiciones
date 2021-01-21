
linea = input().split()
base = float(linea[0])
altura = float(linea[1])

if base < 0.0 or base > 10.0:
    print("Error en base")
elif altura < 0.0 or altura > 10.0:
    print("Error en altura")
else:
    print (base*altura/2)