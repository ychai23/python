#all subsets
def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

def numIslands(self, grid: List[List[str]]) -> int:
        def travel(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]=="0":
                return
		##ONCE WE VISIT LAND...CHANGE IT TO WATER		
            grid[i][j]="0"
            travel(i,j-1)
            travel(i,j+1)
            travel(i-1,j)
            travel(i+1,j)
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="0" and grid[i][j]=="1":
                    travel(i,j)
                    c+=1
        return c            

#find the one signle num
from collections import defaultdict
def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
#find max subarray sum
def maxSubArray(self, nums: List[int]) -> int:
        maxsofar = nums[0]
        maxending = nums[0]
        for i in range(1,len(nums)):
            maxsofar = max(maxsofar+nums[i],nums[i])
            maxending = max(maxending,maxsofar)
        return maxending


#check if the {} is valid using stack
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        else: return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        tree = self.inorderTraversal(root)
        node = TreeNode(tree[0])
        trav = node
        print(tree)
        for i in range(1, len(tree)):
            trav.right = TreeNode(tree[i])
            trav = trav.right
        return node
            
    
def inorderTraversal(self, root):
    res = []
    if root:
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res = res + self.inorderTraversal(root.right)
    return res

#sum num from root to leaf
def sumNumbers(self, root: TreeNode) -> int:
        def dfs(cur, num):
            if not cur:
                return 0
            
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num
            return dfs(cur.left, num) + dfs(cur.right, num)
        
        return dfs(root, 0)

def partition(self, s: str) -> List[List[str]]:
        if not s: return []
        n = len(s)
        def if_palindrome(sub):
            return sub == sub[::-1]
        
        res = []
    
        def dfs(start, path):
            if start == n:
                res.append(path.copy())
                return
            for i in range(start, n):
                if if_palindrome(s[start: i+1]):
                    path.append(s[start: i+1])
                    dfs(i+1, path)
                    path.pop()
              
        dfs(0, [])
        return res