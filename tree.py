import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value, state):
        self.value = value
        self.left = None
        self.right = None
        self.state = state  # 0: left, 1: right

    # creating the tree (0 in all states)
    def insert(self, value, state):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value, state)
                else:
                    self.left.insert(value, state)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeNode(value, state)
                else:
                    self.right.insert(value, state)
            else:
                print("Value already in tree!")
        
def postorderprint(r):
    if r is not None:
        print(r.value, end=" ")
        postorderprint(r.left)
        postorderprint(r.right)
    
if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    root = TreeNode(0, 0)
    for i in nodes:
        root.insert(i, 0)

    
    
    postorderprint(root)
    