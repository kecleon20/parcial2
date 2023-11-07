from grafo import Grafo #Para el ejercicio 2

# ejercicio 2
grafo = Grafo()
grafo.insert_vertice('darth vader')
grafo.insert_vertice('boba fett')
grafo.insert_vertice('c-3po')
grafo.insert_vertice('rey')
grafo.insert_vertice('leila')
grafo.insert_vertice('kylo ren')
grafo.insert_vertice('chewbacca')
grafo.insert_vertice('han solo')
grafo.insert_vertice('r2-d2')
grafo.insert_vertice('bb-8')
grafo.insert_vertice('luke skywalker')
grafo.insert_vertice('yoda')

# aristas
grafo.insert_arist("luke skywalker", "leila", 4)
grafo.insert_arist("luke skywalker", "yoda", 3)
grafo.insert_arist("boba fett", "darth vader", 2)
grafo.insert_arist("c-3po", "r2-d2", 6)
grafo.insert_arist("rey", "kylo ren", 7)
grafo.insert_arist("chewbacca", "han solo", 5)
grafo.insert_arist("han solo", "leila", 4)
grafo.insert_arist("r2-d2", "bb-8", 3)
grafo.insert_arist("yoda", "darth vader", 2)

# punto b
arbol_expancion_min = grafo.kruskal()
for arista in arbol_expancion_min:
    print(arista)

contiene_yoda = False
for arista in arbol_expancion_min:
    if 'yoda' in arista[0] or 'yoda' in arista[1]:
        contiene_yoda = True

if contiene_yoda:
    print('Contiene a yoda')
else:
    print('No contiene a yoda')

# punto c 
max_episodios = 0
personajes_max_episodios = []

for i in range(grafo.size()):
    vertice = grafo.get_element_by_index(i)
    aristas = vertice[1]
    for j in range(aristas.size()):
        arista = aristas.get_element_by_index(j)
        if arista.peso > max_episodios:
            max_episodios = arista.peso
            personajes_max_episodios = [vertice[0], arista.vertice]
        elif arista.peso == max_episodios:
            personajes_max_episodios.append(vertice[0])
            personajes_max_episodios.append(arista.vertice)

print('numero máximo de episodios compartidos:', max_episodios)
print('personajes involucrados en el máximo de episodios compartidos:', personajes_max_episodios)