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

def decode_huffman_tree(root, encoded_string):
    decoded_message = []
    node = root
    
    for bit in encoded_string:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.left is None and node.right is None:  
            decoded_message.append(node.char)
            node = root  
    
    return ''.join(decoded_message)

# Example usage
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
encoded_string = '1101100111110'

root = build_huffman_tree(characters, frequencies)
decoded_message = decode_huffman_tree(root, encoded_string)
print(decoded_message)  
