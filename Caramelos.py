from math import ceil, floor

if __name__ == '__main__':
    t = int(input())
    lineas=[]
    for i in range(t*2):
        lineas.append(input().split())

for contador_i in range(len(lineas)):
    if contador_i%2 == 0:
        amigos = int(lineas[contador_i][0])
        caramelos = lineas[contador_i][1]
    if contador_i%2 != 0:
        suma = 0
        for p in range(len(lineas[contador_i])):
            suma += int((lineas[contador_i][p])) / amigos
        superior = ceil(suma)
        inferior = floor(suma)
        if inferior == 0:
            inferior = 1
        print("%s %s" %(superior, inferior))
