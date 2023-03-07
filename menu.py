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
        print("en proceso")

    elif ans=="2":
        print("en proceso")
    elif ans=="3":
        info()
    elif ans=="4":
        print("Adios")
        break
    elif ans!="":
        print("no es valido intentalo de nuevo")
