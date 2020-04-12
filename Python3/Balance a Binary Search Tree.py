def treeToVine(root: TreeNode) -> int:
    
    vineTail = root
    remainder = vineTail.right
    size = 0
    
    while remainder:
        # If no leftward subtree, move rightward
        if  not remainder.left:
            vineTail = remainder
            remainder = remainder.right
            size += 1
        # else eliminate the leftward subtree by rotations
        else:   # Rightward rotation
            tmp = remainder.left
            remainder.left = tmp.right
            tmp.right = remainder
            remainder = tmp
            vineTail.right = tmp
    return size
            
       
def fullSize(size: int) -> int:
    Rtn = 1
    while Rtn <= size:     # Drive one step PAST FULL
        Rtn = 2 * Rtn + 1   # next pow(2,k)-1
    return Rtn / 2
    
    
def compression(root: TreeNode, count: int) -> None:
    scanner = root
    
    for j in range(int(count)):
        # Leftward rotation
        child = scanner.right
        scanner.right = child.right
        scanner = scanner.right
        child.right = scanner.left
        scanner.left = child
            

def vineToTree(root: TreeNode, size: int) -> None:
    fullCount = fullSize(size)
    compression(root, size - fullCount)
    size = fullCount
    while size > 1:
        compression (root, size / 2)
        size /= 2


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        pseudoRoot = TreeNode(None)
        pseudoRoot.right = root
        size = treeToVine(pseudoRoot)
        vineToTree(pseudoRoot, size)
        return pseudoRoot.right
        
