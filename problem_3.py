import sys

# define a Node class
class Node:
    def __init__(self, char, freq):
        self.character = char
        self.frequency = freq
        self.left = None
        self.right = None
        self.huff_code = ''

    def has_left(self):
        return self.left != None

    def has_right(self):
        return self.right != None

def create_node(sorted_freq):
    priority_queue = []
    for i in range(len(sorted_freq)):
        node = Node(sorted_freq[i][0],sorted_freq[i][1])       
        priority_queue.append(node) 
    return priority_queue
  
def huffman_encoding(*arg):
    # input check
    if not arg or len(arg) < 1 or len(arg) > 1:
        print('input error')
        return None, None
    data = arg[0]
    if not data:
        print('please input data')
        return None, None

    # analysis frequency
    data_frequency = dict()
    for a_str in data:
        data_frequency[a_str] = data_frequency.get(a_str, 0) + 1    
    # sort frequency, output the list
    sorted_freq = sorted(data_frequency.items(), key = lambda data_frequency:data_frequency[1], reverse= False)
    #print(sorted_freq)    
    # create queue
    priority_queue = create_node(sorted_freq)

    if len(priority_queue) > 1:
        #print(priority_queue)    
        while len(priority_queue) > 1:
            # take the smallest 1,2 
            node1 = priority_queue[0]
            node2 = priority_queue[1]
            priority_queue.pop(0)
            priority_queue.pop(0)        
            # create new node
            node1_freq = node1.frequency
            node2_freq = node2.frequency
            new_node_freq = node1_freq + node2_freq
            # set 0/1 code in the left and right node
            node1.huff_code = 0
            node2.huff_code = 1
            # create new node
            new_node = Node(None, new_node_freq)
            new_node.left = node1
            new_node.right = node2
            priority_queue.append(new_node)
            priority_queue = sorted(priority_queue, key = lambda x:x.frequency)
            top_node = priority_queue[0]
    else:
        node1 = priority_queue[0]
        node1.huff_code = 0
        top_node = node1
     
    # encoding
    code_table = path_search(top_node)
    #print(code_table)
    HuffmanCode = ''
    for a_str in data:
        HuffmanCode += code_table[a_str]

    return HuffmanCode, top_node

def path_search(nodes):
    encoded_data = dict()   
    results = path_code_finder(encoded_data, nodes)
    return results

def path_code_finder(encoded_data, node, value = ''):
    new_value = value + str(node.huff_code)

    if node.left:        
        path_code_finder(encoded_data, node.left, new_value)
    
    if node.right:        
        path_code_finder(encoded_data, node.right, new_value)
    
    if (not node.left and not node.right):
        encoded_data[node.character] = new_value
        
    return encoded_data
 

def huffman_decoding(data, tree):
    initial_tree = tree
    decoded_string = ''
    for OneCode in data:        
        if OneCode == '0':
            if (tree.left):
                tree = tree.left

        elif OneCode == '1':
            #  = 1
            if (tree.right):
                tree = tree.right   
        else:
            print('error')
        
        if tree.left == None and tree.right == None:
            decoded_string += tree.character
            # re-set tree for next string
            tree = initial_tree

    return decoded_string



print('test normal case')

a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))



print('test edge case 1')
a_great_sentence = "aaaaaaaaaaaaa"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


print('test edge case 2')
a_great_sentence = ""
encoded_data, tree = huffman_encoding(a_great_sentence)
