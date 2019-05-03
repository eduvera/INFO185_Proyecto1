import numpy as np
class Prob_node:
    def __init__(self, symbol = "", code = "", prob=0):
        self.symbol = symbol
        self.code = code
        self.prob = prob
        self.left_child = None
        self.right_child = None

    def sum_childs(self):
        if self.left_child != None and self.right_child != None:
            self.prob = self.left_child.prob + self.right_child.prob
        else:
            print("Error no childs")

class PrioQueue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.insert(0,item)
        self.__bubbleSort()

    def __bubbleSort(self):
        for passnum in range(len(self.items)-1,0,-1):
            for i in range(passnum):
                if self.items[i].prob>self.items[i+1].prob:
                    temp = self.items[i]
                    self.items[i] = self.items[i+1]
                    self.items[i+1] = temp
                    
    def create_tree(self):
        while(len(self.items)>1):
            min1 = self.items.pop(0)
            min2 = self.items.pop(0)
            
            new_node = Prob_node()
            new_node.left_child = min1
            new_node.right_child = min2
            new_node.left_child.code = "0"
            new_node.right_child.code="1"
            new_node.sum_childs()
            
            self.put(new_node)

        return self.items[0]
    


def huffman_coding(prob_list):
    cola = PrioQueue()

    for i in prob_list:
        cola.put(Prob_node(symbol= i[0],prob = i[1]))

    tree = cola.create_tree()

    dictionary = {}
    
    search_tree_codes(tree,"",dictionary)


    return dictionary

def search_tree_codes(tree,code,dictionary):
    if(tree.left_child!=None and tree.right_child!=None):
        search_tree_codes(tree.left_child,code + tree.code,dictionary)
        search_tree_codes(tree.right_child,code + tree.code,dictionary)
    else:
        dictionary[tree.symbol] = code+tree.code
    

def encode(dictionary, array):
    code = ""
    for i in array:
        code = code + dictionary[i]
        
    print(code[:10], len(code))
    return int(code,2)

def decode(dictionary, string_bin):
    code = ""
    print(len(string_bin),string_bin[:10])
    array = np.zeros(shape=(480*848),dtype=np.uint8)

    cnt = 0
    if (len(string_bin)%2!=0):
        string_bin = string_bin[1:]
    for i in string_bin:
        if i =="b":i = "0"
        code = code + i
        if code in dictionary.values():
            array[cnt] = list(dictionary.keys())[list(dictionary.values()).index(code)]
            code=""
            cnt+=1

    
    return array.reshape(480,848)
        
            