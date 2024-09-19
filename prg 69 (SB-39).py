import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(characters, frequencies):
    heap = [Node(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]  

def generate_codes(root):
    codes = {}
    
    def dfs(node, code):
        if node:
            if node.char is not None:
                codes[node.char] = code
            dfs(node.left, code + '0')
            dfs(node.right, code + '1')
    
    dfs(root, '')
    return codes

def huffman_codes(characters, frequencies):
    root = build_huffman_tree(characters, frequencies)
    codes = generate_codes(root)
    return [(char, codes[char]) for char in characters]

characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
print(huffman_codes(characters, frequencies))
