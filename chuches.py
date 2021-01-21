if __name__ == '__main__':
    n = int(input())
    lineas=[]
    for i in range(n):
        lineas.append(input())

felicidad = 0
if n ==0 :
    print("0")
else:
    for contador in range(n):
        if int(lineas[contador]) > 0:
            felicidad += int(lineas[contador])

    print(felicidad)