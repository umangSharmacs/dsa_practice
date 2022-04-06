class node:
    def __init__(self, value) -> None:
        self.value=value
        self.left=None
        self.right=None

class bin_tree:
    def create_bin_tree(self, arr) -> None:
        curr_val=arr.pop(0)
        root=node(curr_val)
        self.root=root
        q=[root]
        while q and arr!=[]:
            parent=q.pop(0)
            try:
                l=arr.pop(0)
                parent.left=node(l)
                q.append(parent.left)
            except:
                break
            try:
                r=arr.pop(0)
                parent.right=node(r)
                q.append(parent.right)
            except:
                break


    def print_tree(self) -> None:
        q=[self.root]

        while q:
            count=len(q)
            while count>0:

                curr=q.pop(0)
                if curr is not None:
                    print(curr.value, end="  ")
                
                    if curr.left:
                        q.append(curr.left)
                    else:
                        q.append(None)    
                    if curr.right:
                        q.append(curr.right)
                    else:
                        q.append(None)
                else:
                    print("  ", end="")
                count-=1
            print("\n")

arr=[1,2,3,4,5,6,7,8,9]
print("Begin")
tree=bin_tree()
tree.create_bin_tree(arr)
tree.print_tree()




