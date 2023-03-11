historial={}
abc = 'abcdefghijklmnopqrstuvwxyz_'



def cifrar(cadena, clave):



    text_cifrado = ''



    for letra in cadena:

        suma = abc.find(letra) + clave

        modulo = int(suma) % len(abc)

        text_cifrado = text_cifrado + str(abc[modulo])



    return text_cifrado



def decifrar(cadena, clave):



    text_cifrado = ''



    for letra in cadena:

        suma = abc.find(letra) - clave

        modulo = int(suma) % len(abc)

        text_cifrado = text_cifrado + str(abc[modulo])



    return text_cifrado



def main():

    c = str(input('cadena a cifrar: ')).lower()

    n = int(input('clave numerica: '))

    print(cifrar(c, n))

def main2():
    q = str(input('cadena a descifrar: ')).lower()

    u = int(input('clave numerica: '))

    print(decifrar(q, u))


def info():
    print("pronto info")


ans=True
while ans:
    print("""
    1 añadir un mensaje
    2 eliminar un mensaje
    3 descifrar un mensaje
    4 exit/salir""")
    ans=input("¿Que quieres hacer?")
    if ans=="1":
        main()
    elif ans=="2":
        print(historial)
    elif ans=="3":
        main2()
    elif ans=="4":
        print("Adios")
        break
    elif ans!="":
        print("no es valido intentalo de nuevo")


