from arbol_binario import BinaryTree #Para el ejercicio 1


# ejercicio 1
# punto a)
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

pokemons = [
    {'nombre': 'charizard', 'numero': 6, 'tipo': ['fuego', 'volador']},
    #{'nombre': 'lycanroc', 'numero': 745, 'tipo': ['roca']},
    {'nombre': 'bulbasaur', 'numero': 1, 'tipo': ['planta']},
    {'nombre': 'jolteon', 'numero': 135, 'tipo': ['electrico']},
    #{'nombre': 'tyrantrum', 'numero': 697, 'tipo': ['roca', 'dragon']},
    {'nombre': 'marowak', 'numero': 105, 'tipo': ['tierra']},
 ]

for data in pokemons:
    nombres = data['nombre']
    numero = data['numero']
    tipo = data['tipo']

    arbol_nombre.insert_node(nombres, data)
    arbol_numero.insert_node(numero, data)
    for type in tipo:
        arbol_tipo.insert_node(tipo, data)

# punto b)
num = 6 #cambiar a conveniencia
value = arbol_numero.search(num)
if value:
    print(value.other_values) 
else: #en caso de que no se encuentre
    print(f'no hay pokemon con el numero {num}')

print('busqueda por coincidencia')
nombre_buscado = arbol_nombre.search_by_coincidence('bulba')
if nombre_buscado:
    print('pokemones encontrados por nombre')
    for pokemon in nombre_buscado:
        print('nombre', pokemon.value)
        print('datos', pokemon.other_values)

# punto c)
tipo = 'electrico'
print(f'pokemons de tipo {tipo}')
arbol_tipo.inorden_tipos_pokemon(tipo)

# punto d)
print('listado por numero ascendente')
arbol_numero.postorden()
print('listado ascendente nombre ')
arbol_nombre.postorden()
print('listado por nivel nombre')
arbol_nombre.by_level()

# punto e) 
print('datos de jolteon')
node = arbol_nombre.search('jolteon')
if node:
    print(node.other_values)
else:
    print('no se encuentra jolteon')

print('datos de lycanroc')
node = arbol_nombre.search('lycanroc')
if node:
    print(node.other_values)
else:
    print('no se encuentra lycanroc')

print('datos de tyrantrum')
node = arbol_nombre.search('tyrantrum')
if node:
    print(node.other_values)
else:
    print('no se encuentra tyrantrum')

# punto f
print('cantidad de pokemons de tipo electrico')
cantidad =  arbol_tipo.contar_electrico_pokemon()
print(cantidad),

print('cantidad de pokemons de tipo acero')
cantidad = arbol_tipo.contar_acero_pokemon()
print(cantidad)


