class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
LEVEL ORDER METHOD

sample tree input:

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4

expected output: 1 2 5 3 6 4
"""
def levelOrder(root):
    queue = [root]

    while(queue):
      current = queue[0]
      print(current, end=" ")
      if(current.left): queue.append(current.left)
      if(current.right): queue.append(current.right)
      queue.pop(0)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)