if __name__ == '__main__':
    t = int(input())
    lineas=[]
    for i in range(t):
        lineas.append(input().split())


for contador_i in range(len(lineas)):
    mensaje = ''
    for contador_p in range(len(lineas[contador_i])):
        if contador_p == 0:
            mensaje += 'O' * int(lineas[contador_i][contador_p])
        elif contador_p == 1:
            mensaje += 'I' * int(lineas[contador_i][contador_p])
        elif contador_p == 2:
            mensaje += 'E' * int(lineas[contador_i][contador_p])
        elif contador_p == 3:
            mensaje += '!' * int(lineas[contador_i][contador_p])
    print(mensaje)

