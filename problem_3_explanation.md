##About

use huffman_encoding funciton to build the huffman code
the algorithm is:

Encoding process:

calc the frequency of data string, save in a dictonary
character as key and frequency as value
use dictonary data strcutrue is quick to read
the time is O(n)
the space of dictonary is O(n)

use sorted function to sort the frequency dictonary 
the time is o(n log n)
space is O(n)

use the create_node function to create a priority queue
transfer each character/frequency into a Node
use node for each data string and frequency and save in a list 
these nodes in list data structure is easy for sorting
just by sorted method, and key = lambda x:x.frequency
the time and space is O(n) for this For loop

use while loop to build huffman tree:
merge the two nodes:
read and remove the lowest 2 frquency nodes
sum of the two frequency
create new node
if the node is in the left, set the huff code 0
if the node is in the right, set the huff code 1
apppend new node the the priority_queue and sort
finally, obtain only one node in the priority queue

using node search recursion to find the end node string and each code in the path
produce a code table by dictonary: str: huffman code

use dictonary data structure is easy for coding string, just use key and obtaining code
also the dictonary is hash table, very quick to read

use a for loop to transfer data string to huffman code
according to the string/code dictonary
and return the code and tree

the time complexity:
the length of priority_queue is decreasing in the loop
so the time of while loop should be O(n log n)
and the max memory space is the length of nodes, space complexity is O(n)

tree path search reccursion is log2(n)
and the encoded_data dictonary space is O(n)

the for loop is O(n)
the length of decoded_string is the length of character, so the space is O(n)

the overall time is O(n log n)
the space is O(n)


Decoding process:

read the code data and tree into huffman_decoding function
copy the input tree for each new node search
a For loop the read data code and search the tree
    if code is 0
        go to left node     

    if code is 1
        go the right node    
    
    if find the end of node 
        read the character and save

        re set the tree to initial tree
finally, return the decorded string

the time is O(n)
the space memory is the length of character, so the space is O(n)

