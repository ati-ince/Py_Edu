class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

    def insert(self,root,node):
        if root is None:
            root = node 
        else: 
            if root.val < node.val:
                if root.right is None:
                    root.right = node 
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    def IsPresent(self, root, value):
        if not root:
            return False
        if root.val == value:
            return True
        if root.val > value:
            return self.IsPresent(root.left, value)
        return self.IsPresent(root.right, value)

#Create BST
r = Node(50) 
r.insert(r,Node(30)) 
r.insert(r,Node(20)) 
r.insert(r,Node(40)) 
r.insert(r,Node(70)) 
r.insert(r,Node(60)) 
r.insert(r,Node(80))

TestData = [
        10,20,30,40,50,100
           ]

def Test_BST(data,bst):
    for i,dt in enumerate(data):
        res = bst.IsPresent(bst,dt)
        print(i,res)


Test_BST(TestData,r)


# search BST 30 min
# solve 15 min