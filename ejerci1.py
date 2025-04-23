total =0
for i in range(5):
    try:
        num=int(input("Elija numero"))
        total += num
    except TypeError:
        print("Solo numeros ")
toto=total / 5
print("El total es:" + str(toto))        