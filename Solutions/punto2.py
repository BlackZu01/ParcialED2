from tree import Tree

tree = Tree()
tree.addMultipleNodes([5, 7, 3, 1, 73, 37, 15, 11, 2, 3])


# El menor nodo del árbol
min_tree = tree.findMinimalRecu(tree.root)


# El mayor nodo del árbol
max_tree = tree.findMaximalRecu(tree.root)

print(f'El mínimo valor encontrado en un nodo en el arbol es {min_tree} y esta en el nivel {tree.getLevel(tree.root, min_tree)}')

print(f'El máxmimo valor encontrado en un nodo en el arbol es {max_tree} y esta en el nivel {tree.getLevel(tree.root, max_tree)}')