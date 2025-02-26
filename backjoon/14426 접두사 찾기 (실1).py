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

        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            
            cur_node = cur_node.children[char]
        
        cur_node.data = string

    def is_prefix(self, string):
        cur_node = self.head

        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        
        return True

N, M = map(int, input().rstrip().split())
trie = Trie()
result = 0

for _ in range(N):
    string = input().rstrip()
    trie.insert(string)

for _ in range(M):
    string = input().rstrip()
    if trie.is_prefix(string):
        result += 1

print(result)