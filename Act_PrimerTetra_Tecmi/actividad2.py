import os
import time

print("Bienvenido al programa SORT BUBBLE")
# time.sleep(3)
os.system('cls')
num = int(input("Indica el número de valores que tendrá la lista a ordernar: "))

lista = []
a=1

for a in range(num):
    a = input(print("Dime el número: ", a))

for x in range(num):
    for b in range(num-1):
        if lista[b] > lista[b+1]:
            tempo = lista[b]
            lista[b] = lista[b+1]
            lista[b+1] = tempo

for c in num:
    print(lista[c])