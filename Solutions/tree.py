from node import Node

class Tree:
    def __init__(self):
        self.root = None
    
    def addNode(self, value: int) -> None:
        '''
        Allows adding a node to the tree

        Args:
            value (int) : [int value we want to add as a node]
        
        Return:

        '''
        # If the root is empty, we want to fill it
        if self.root is None:
            self.root = Node(value)
            return 

        # Otherwise, we call a recursive function that add a node automatically
        self.addNodeRecur(self.root, value)
    
    def addNodeRecur(self, current: Node, value: int) -> None:
        '''
        Recursive function that adds nodes automatically

        Args:
            current (Node) : [node where the function will start to check if we can add a node]
            value   (int)  : [int value we want to add as a node]

        Return:

        '''
        # The new node is the node we'll add
        newNode = Node(value)
        # If the value of the new node is lower than the current value we are checking and if the left 
        # side is empty, we'll add it there
        if value < current.value:
            if current.left is None:
                current.left = newNode
            else:
                # Otherwise, we'll continue moving to left side
                self.addNodeRecur(current.left, value)
        else:
            # Same as above but for the right side
            if current.right is None:
                current.right = newNode
            else:
                self.addNodeRecur(current.right, value)
        current.height = 1 + max(self.get_hight(current.left), self.get_hight(current.right))

    # Allows add multiple node if you're lazy and don't want to add one by one
    def addMultipleNodes(self, nodes: list) -> None:
        '''
        Add multiples nodes to the tree

        Args:
            nodes (list) : [list of values of the nodes we want to add]
        
        Return:

        '''
        for node in nodes:
            self.addNode(node)
    
    def findNodeFamiliars(self, current: Node, value: int, family: list=[]) -> list:
        '''
        Find all the nodes that belongs to a branch where our node is

        Args:
            current (Node) : [node where our function will start to move]
            value   (int)  : [int value of the node we are looking for the nodes of its branch]
            family  (list) : [list where all those nodes will be added]

        Return:
            (list) : Return the list with each node of the branch where was our node
        '''
        # If the value we are looking for family (as our reach is to find the uncle and grandpa of a node we discard 
        # inmediatly if the node is the root)
        try:
            if value == self.root:
                print('The node has not grandpa and uncle')
                return 

            # We will use the same logic as above, moving through the tree and add the nodes that belong to the branch in
            # our family list

            if value < current.value:
                family.append(current)
                if current.left.value == value:
                    family.append(current.left)
                    return family
                else:
                    family = self.findNodeFamiliars(current.left, value, family)
            else:
                # Same as above but if the node we're looking for its family is in the right side
                family.append(current)
                if current.right.value == value:
                    family.append(current.right)
                    return family
                else:
                    family = self.findNodeFamiliars(current.right, value, family)

            return family
        except AttributeError:
            return None
    
    def get_max_levels(self, root: Node) -> int:
        '''
        Compute the max level of a tree

        Args: 
            root (Node) : [node where the function will start moving to find the level]

        Return:
            (int) : Return the level of the tree
        '''

        # If the root is None, it means the tree is empty so it returns 0
        if root is None:
            return 0
        else:
            # Otherwise, we'll start moving to find our last node and plus 1 value to the end of the tree
            left_levels = self.get_max_levels(root.left)
            right_levels = self.get_max_levels(root.right)

            return max(left_levels, right_levels) + 1

    def levelOrderPrint(self, current: Node) -> None:
        '''
        Print nodes by level

        Args:
            current (Node) : [node where the function will start to print]

        Return:

        '''
        # We need the max level of the tree to create a loop that will start to print one by one 
        height = self.get_max_levels(current)

        # The loop will start at the level 1 to the final level (we add + 1 due to the for in python end and height - 1)
        for level in range(1, height+1):
            # We'll call another function who will loop through the nodes
            print(f'Level {level}', end=': ')
            self.printCurrentLevel(current, level)
            print('\n')
    
    def printCurrentLevel(self, current: Node, level: int) -> None:
        '''
        Print node value by level

        Args:
            current (Node) : [node where the function will start to print]
            level   (int)  : [level of the current node]
        
        Return:

        '''

        if current is None:
            return
        # If we are in the first level, we print the node value
        if level == 1:
            print(f'{current.value}', end=' ')
        # Otherwise, we'll move 'till the level of the node became 1 again to print by the same level
        elif level > 1:
            self.printCurrentLevel(current.left, level-1)
            self.printCurrentLevel(current.right, level-1)

    def getLevel(self, current: Node, value: int, level: int =1) -> int:
        '''
        Compute the level of a determinated node

        Args:
            current (Node) : [node where the function will start to move]
            value   (int)  : [int value of the node we want to know the level]
            level   (int)  : [the level that will be increasing if the node is lower]
        
        Return:
            (int) : Return the level of the node
        '''
        # If the value of the node is the root, we return the root level (is 1)
        if self.root.value == value:
            return level
        try:
            # Same logic as above in addNode(), we'll start moving based in if the value is lower than the root
            if value < current.value:
                level += 1
                # If we find our node, we return the level
                if current.left.value == value:
                    return level 
                else:
                    # Otherwise, we continue moving 
                    level = self.getLevel(current.left, value, level)
            else:
                # Same as above but for the right side
                level += 1
                if current.right.value == value:
                    return level 
                else:
                    level = self.getLevel(current.right, value, level)
        except AttributeError:
            # The function throws an error when it can't find our node
            return f'The node {value} does not exist'
        return level
    
    def get_hight(self, current: Node) -> int:
        '''
        Devuelve la altura del arbol/subarbol de donde estemos tomando la raíz
        Args:
            current (Node) : [Node for which we're trying to find the height]
        '''
        if not current:
            return 0
        #Simplemente retorna el atributo altura
        return current.height
    
    
    def isInTheTree(self, current: Node, value: int, isIn: tuple = (False, None)) -> tuple:
        '''
        Check if a node exist in the tree

        Args:
            current  (Node)  : [node from where will start to move]
            value    (int)   : [int value of the node we are looking]
            isIn     (tuple) : [tuple of 2 elements]
        
        Return:
            (tuple) : Return a tuple in whose first position is True if the node was found
            , otherwise is False. In the second element of the tuple, is the level where
            the node is.
        '''
        # If we couldn't find our node, return False in first position and None in the second one.
        if current is None:
            return isIn 

        # We start moving in the tree
        if value < current.value:
            if value == current.value:
                # If we find our node, return a tuple in whose first positon will be True and in the second the level of the node
                # isIn = ({'Is in the tree?': True}, {'Level where the node is}': self.getLevel(self.root, value)})
                isIn = (True, self.getLevel(self.root, value))
                return isIn 
            else:
                # We continue going down to search the node
                isIn = self.isInTheTree(current.left, value)
        else:
            # Same as above but with right side
            if value == current.value:
                isIn = (True, self.getLevel(self.root, value))
                return isIn 
            else:
                isIn = self.isInTheTree(current.right, value)
                
        return isIn 
    
    
    def encontrarAncestro(self, current: Node, value1: int, value2: int):
        '''
        Encuentra el ancestro más profundo entre 2 nodos

        Args:
            current  (Node)  : [node from where will start to move]
            value1 (int)     : [Value of the first node]
            value2 (int)     : [Value of the second node]
        '''
        # Validacion de si existen los dos nodos
        if self.isInTheTree(self.root, value1)[0] and self.isInTheTree(self.root, value2)[0]:
            #Creamos dos listas que contendran todos los ancestros para cada nodo
            fam1 = [nodo.value for nodo in self.findNodeFamiliars(current, value1, [])]
            fam2 = [nodo.value for nodo in self.findNodeFamiliars(current, value2, [])]
            # Aquí guardaremos los ancestros en común
            ancestros = []

            # Aquí compararemos cada elemento de las listas, en caso tal de encontrar semejantes, la guardamos en ancestros
            for k in range(len(fam1)):
                for j in range(len(fam2)):
                    if fam1[k] == fam2[j]:
                        ancestros.append(fam1[k])
            
            # Si la lista tiene un elemento, significa que el ancestro más profundo es el root
            if len(ancestros) == 1:
                return ancestros[0]
            # Sino entonces retornamos la siguiente posicion de la lista que sera el ancestro más profundo entre los dos nodos
            else:
                for k in range(len(ancestros)):
                    return ancestros[1]
        else:
            # Si alguno de los dos nodos no esta en el arbol (o ambos)
            return 'Los nodos deben pertenecer al árbol'

    def findMinimalRecu(self, current: Node) -> int:
        '''
        Compute the lower value of the tree

        Args: 
            current (Node) : [Node from where will start to move]

        Return:
            (int) : lower value found in the tree 
        '''
        #Retornamos infinito en caso tal de llegar al final dado que al comparar los 3 valores finales, queremos solamente encontrar el mínimo entre left_max
        # y right_max (es para descartar enseguida el infinito porque obviamente no sera el mínimo)
        if current is None:
            return float('inf') 
        # Recorremos todo el arbol y vamos retornando sus respectivos valores con el current, value, así que al final de las iteraciones
        # left_min y right_min tendran los ultimos valores que den en la iteracion
        left_min = self.findMinimalRecu(current.left)
        right_min = self.findMinimalRecu(current.right)
        return min(current.value, left_min, right_min)
    
    def findMaximalRecu(self, root: Node) -> int:
        '''
        Compute the bigger value of the tree

        Args: 
            current (Node) : [Node from where will start to move]

        Return:
            (int) : bigger value found in the tree 
        '''
        # Retornamos -infinito en caso tal de llegar al final dado que al comparar los 3 valores finales, queremos solamente encontrar el maximo entre left_max
        # y right_max (es para descartar enseguida el -infinito porque obviamente no sera el máximo)
        if root is None:
            return float('-inf') # Lo mismo aca
        # Recorremos todo el arbol y vamos retornando sus respectivos valores con el current, value, así que al final de las iteraciones
        # left_min y right_min tendran los ultimos valores que den en la iteracion
        left_max = self.findMaximalRecu(root.left)
        right_max = self.findMaximalRecu(root.right)
        return max(root.value, left_max, right_max)
    
# Nota: la documentación en español es por falta de tiempo en el parcial, lo que esta en inglés son métodos que hice en mi casa con calma y por eso esta en
# inglés, un saludo!