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

    cc = str(input('cadena a decifrar: ')).lower()

    cn = int(input('clave numerica: '))

    print(decifrar(cc, cn))






def info():
    print("pronto info")


ans=True
while ans:
    print("""
    1 añadir un mensaje
    2 eliminar un mensaje
    3 info
    4 exit/salir""")
    ans=input("¿Que quieres hacer?")
    if ans=="1":
        main()
    elif ans=="2":
        print("en proceso")
    elif ans=="3":
        info()
    elif ans=="4":
        print("Adios")
        break
    elif ans!="":
        print("no es valido intentalo de nuevo")


