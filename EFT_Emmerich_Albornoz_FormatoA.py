juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}
inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

def mostrar_menu():
    print('''
========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================
''')

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese la opcion: "))
            if 1 <= op <= 6:
                return op
            else:
                print("Error. Ingrese una opcion entre 1 y 6.")
        except ValueError:
            print("Error. Ingrese un numero entero.")

def stock_plataforma(plataforma, juegos, inventario):
    total = 0
    for codigo in juegos:
        if juegos[codigo][1].capitalize() == plataforma.capitalize():
            total += inventario[codigo][1]
            print(f"Stock total {plataforma}:{total}")

def busqueda_precio(p_min, p_max, juegos, inventario):
    lista = []
    for codigo in inventario:
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if p_min <= precio <= p_max and stock != 0:
            titulo = juegos[codigo][0]
            lista.append(f"{titulo}---{codigo}")
    if len(lista) == 0:
        print("Error. No se logra encontrar algun juego.")
    else:
        lista.sort()
        for juego in lista:
            print(juego)

def buscar_codigo(codigo,inventario):
    codigo = codigo.upper()
    for cod in inventario:
        if cod.upper() == codigo:
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, inventario):
    codigo = codigo.upper()
    if buscar_codigo(codigo, inventario):
        for cod in inventario:
            inventario[cod][0] = nuevo_precio
            return True
    return False

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    if buscar_codigo(codigo, inventario):
        return False
    juegos[codigo.upper()] = [
                            titulo,
                            plataforma,
                            genero,
                            clasificacion,
                            multiplayer,
                            editor
                            ]
    inventario[codigo.upper()] = [
                                precio,
                                stock
                                ]
    return True

def eliminar_juego(codigo, juegos, inventario):
    codigo = codigo.upper()
    if buscar_codigo(codigo, inventario):
        for cod in list(inventario):
            if cod.upper()== codigo:
                del juegos[cod]
                del inventario[cod]
                return True
    return False

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_plataforma(plataforma):
    return plataforma.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ["E", "T", "M"]

def validar_editor(editor):
    return editor.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_stock(stock):
    return stock >= 0

def main():
    while True:
        mostrar_menu()
        op = leer_opcion()
        if op == 1:
            plataforma = input("Ingrese la plataforma a consultar: ")
            stock_plataforma(plataforma, juegos, inventario)
        elif op == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio minimo: "))
                    p_max = int(input("Ingrese el precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("No se encontraron juegos dentro del rango.")
                except ValueError:
                    print("Error. Ingrese un numero entero")
            busqueda_precio(p_min, p_max, juegos, inventario)
        elif op == 3:
            while True:
                codigo = input("Ingrese el codigo del juego: ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if nuevo_precio >0:
                        if actualizar_precio(codigo, nuevo_precio, inventario):
                            print("Precio Actualizado")
                        else:
                            print("Error. Codigo inexistente")
                        seguir = input("¿Desea actualizar otro precio (s/n)?: ")
                        if seguir == "n":
                            break
                    else:
                        print("Error. El nuevo precio tiene que ser mayor que 0.")
                except ValueError:
                    print("Error. Ingrese un numero entero.")
        elif op == 4:
            codigo = input("Ingrese el codigo del juego: ")
            titulo = input("Ingrese el titulo: ")
            plataforma = input("Ingrese la plataforma: ")
            genero = input("Ingrese el genero: ")
            clasificacion = input("Ingrese la clasificacion: ").upper()
            multiplayer = input("¿Es multiplayer (S/N)?: ").lower()
            editor = input("Ingrese el editor: ")
            try:
                precio = int(input("Ingrese el precio: "))
                stock = int(input("Ingrese el stock: "))
            except ValueError:
                print("Error. El numero tiene que ser entero.")
                continue
            if not validar_titulo(titulo):
                print("Error. El titulo no puede estar vacio.")
            elif buscar_codigo():
                print("Error. El codigo no puede existir ya ni estar vacio.")
            elif not validar_plataforma(plataforma):
                print("Error. La plataforma no puede estar vacia ni tener espacios en blanco.")
            elif not validar_genero(genero):
                print("Error. El genero no puede estar vacio.")
            elif not validar_clasificacion(clasificacion):
                print("Error. Debe ser exactamente 'E', 'T' o 'M'")
            elif not validar_editor(editor):
                print("Error. El editor no puede estar vacio.")
            elif not validar_precio(precio):
                print("Error. Numero entero mayor que cero.")
            elif not validar_stock(stock):
                print("Error. Numero entero mayor o igual a cero.")
            else:
                multiplayer = True if multiplayer == "s" else False
        elif op == 5:
            codigo = input("Ingrese el codigo del juego: ")
            if eliminar_juego(codigo, juegos, inventario):
                print("Juego Eliminado")
            else:
                print("El juego no existe")
        elif op == 6:
            print("Programa finalizado")
            break

main()