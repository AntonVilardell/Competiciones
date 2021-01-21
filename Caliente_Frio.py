'''
f = open("myfile.txt", "r")
lineas = f.readlines()
f.close()
'''

if __name__ == '__main__':
    t = int(input())
    lineas=[]
    for i in range(t):
        lineas.append(input())

if t < 1 or t > 20:
    print("Error en -tiempo-")
    quit()

for contador in range(0, int(t)):
    if float(lineas[contador]) < 0.0 or  float(lineas[contador]) > 100.0:
        print("Error en -temperatura- (%s)" %float(lineas[contador]) )
    elif float(lineas[contador]) < 10.0:
        print('Enciende')
    elif float(lineas[contador]) >= 10.0 and float(lineas[contador]) <= 15.0:
        print('Nada')
    elif float(lineas[contador]) > 15.0:
        print('Apaga')