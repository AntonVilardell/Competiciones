def men_generado(mensaje):
    mensaje_generado = []
    indice = mensaje[0][0]
    if mensaje[len(mensaje)-1][1][-1] == 'E':
        if indice < int(lineas[0]):
            indice = indice +1
            mensaje_generado.append([indice, mensaje[len(mensaje)-1][1] + 'E', int(mensaje[len(mensaje)-1][2]) + 1])
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + '!', int(mensaje[len(mensaje)-1][2])  + 4])
    if mensaje[len(mensaje)-1][1][-1] == 'I':
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + 'E', int(mensaje[len(mensaje)-1][2])  + 1])
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + 'I', int(mensaje[len(mensaje)-1][2])  + 2])
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + '!', int(mensaje[len(mensaje)-1][2])  + 4])
    if mensaje[len(mensaje)-1][1][-1] == 'O':
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + 'E', int(mensaje[len(mensaje)-1][2])  + 1])
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + 'I', int(mensaje[len(mensaje)-1][2])  + 2])
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + 'O', int(mensaje[len(mensaje)-1][2])  + 3])
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + '!', int(mensaje[len(mensaje)-1][2])  + 4])
    if mensaje[len(mensaje)-1][1][-1] == '!':
        if indice < int(lineas[0]):
            indice = indice + 1
            mensaje_generado.append([indice,mensaje[len(mensaje)-1][1] + '!', int(mensaje[len(mensaje)-1][2])  + 4])
    return(mensaje_generado)

def men_mayorpeso(mensaje_generado):
    # Buscar el mensaje generado de mayor peso
    peso_max = 0
    mensaje_max = [['', 0]]
    for i in range(len(mensaje_generado)):
        if mensaje_generado[i][2] > peso_max:
            peso_max = mensaje_generado[i][2]
            mensaje_max.append([mensaje_generado[i][0], mensaje_generado[i][1], mensaje_generado[i][2]])
            mensaje_max.pop(0)

    return mensaje_max

if __name__ == '__main__':
    t = int(input())
    lineas=[]
    for i in range(t):
        lineas.append(input())

        if int(lineas[0]) == 1:
            mensaje_generado = [[1,'E',1]]
        if int(lineas[0]) == 2:
            mensaje_generado = [[1, 'E', 1][2, 'I', 2]]
        if int(lineas[0]) == 3:
            mensaje_generado = [[1, 'E', 1][2, 'I', 2][3, 'O', 3]]
        if int(lineas[0]) == 4:
            mensaje_generado = [[1, 'E', 1][2, 'I', 2][3, 'O', 3][4, '!', 4]]
        if int(lineas[0]) > 4:
            mensaje_generado = [[4,'E',1]]
            while  int(mensaje_generado[len(mensaje_generado)-1][0]) <= int(lineas[0]):
                mensaje_generado = men_generado([mensaje_generado[len(mensaje_generado)-1]])

#Buscar el mensaje generado de mayor peso
mensaje_maximo = men_mayorpeso(mensaje_generado)

print(mensaje_generado)
print(mensaje_maximo)