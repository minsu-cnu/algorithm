import sys
input = sys.stdin.readline

class Node():
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        is_prefix = True

        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
                is_prefix = False
            
            cur_node = cur_node.children[char]

            if cur_node.data != None:
                return True

        cur_node.data = string
        return is_prefix

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    trie = Trie()
    result = "YES"

    for _ in range(n):
        string = input().rstrip()
        if trie.insert(string):
            result = "NO"
    
    print(result)
    