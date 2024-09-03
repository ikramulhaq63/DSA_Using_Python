class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.rifht=right

class binarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
         self.root = self.r_insert(self.root,data)
    def r_insert(self,root,data):
        if root is None:
            return Node(data)
        if data <root.item:
            root.left = self.r_insert(root.left,data)
        elif data>root.item:
            root.right = self.r_insert(root.right,data)
        return root
    def search(self,data):
        return self.r_search(self.root,data)
    def r_search(self,root,data):
        if root is None or root.item ==data:
            return root
        if data<root.item:
            return self.r_search(root.left,data)
        else:
            return self.r_search(root.right,data)
    
    def inoder(self):
        result = []
        self.r_inorder(self.root,result)
        return result
    def r_inorder(self,root,result):
        if root:
            self.r_inorder(root.left,result)
            result.append(root.item)
            self.r_inorder(root.right,result)

    def preoder(self):
        result = []
        self.r_preorder(self.root,result)
        return result
    def r_preorder(self,root,result):
        if root:
            result.append(root.item)
            self.r_preorder(root.left,result)
            
            self.r_preorder(root.right,result)

    def postoder(self):
        result = []
        self.r_postorder(self.root,result)
        return result
    def r_postorder(self,root,result):
        if root:
            self.r_postorder(root.left,result)
            
            self.r_postorder(root.right,result)
            result.append(root.item)
    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    def max_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.right
    
    def delete_node(self,data):
        self.root = self.r_delete(self.root,data)
    def r_delete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.r_delete(root.left,data)
        elif data > root.item:
            root.right = self.r_delete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.r_delete(root.right,root.item)
        return root
    def size(self):
        return len(self.inorder())

 
