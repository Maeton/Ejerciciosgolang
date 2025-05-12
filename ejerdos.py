

numeros=[]
for i in range(5):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
promedio  = sum(numeros )/ len(numeros) 
diferencias=[]
for x in numeros:
    diferencia = x - promedio
    cuadrado = diferencia ** 2
    diferencias.append(cuadrado)
prom= sum(diferencias)/ len(diferencias)


    
print(prom)