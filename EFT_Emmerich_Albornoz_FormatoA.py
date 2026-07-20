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