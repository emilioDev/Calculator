#!/usr/bin/python3.4

from os import system

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    if y == 0:
        print("Errore, divisione per 0")
    else:
        return x/y
    
def main():
    system("clear")
    for x in range(0,20):
        if(x == 20):
            print("*\n")
        else:
            print("*")
            
    number_one = int(input("Inserire il primo valore: "))
    
    number_two = int(input("Inserire il secondo valore: "))
    print("\n1)Somma\n2)Dividi\n3)Moltiplica\n4)Dividi\n")
    
    val = input("Inserire opzione: ")
    
    if val == '1':
        print(add(number_one, number_two))
    elif val == '2':
        print(sub(number_one, number_two))
    elif val == '3':
        print(mul(number_one, number_two))
    elif val == '4':
        print(div(number_one, number_two))
    else:
        print("Operazione non valida!")

main()

