miembros = ["rm", "jin", "suga", "j-hope", "jimin", "v", "jungkook"]

buscar = input("¿Cuál es tu miembro favorito? ").lower()

if buscar != "":
    for  miembro in miembros:
        if buscar == miembro:
            print(f"{miembro.capitalize()} está en BTS ")
             break
    else:
        print("Ese nombre no está en BTS ")
 else:
    print("No ingresaste ningún nombre")