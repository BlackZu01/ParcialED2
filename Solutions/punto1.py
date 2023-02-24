from node import Node 
from tree import Tree
    
tree = Tree()

tree.addMultipleNodes([7, 4, 2, 5, 6, 1, 8, 10])

# Otros casos
print(tree.encontrarAncestro(tree.root, 1, 6))
print(tree.encontrarAncestro(tree.root, 5, 8))

# Caso carita feliz
print(tree.encontrarAncestro(tree.root, 8, 65))