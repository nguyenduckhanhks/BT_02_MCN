class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class PrefixCodeTree:
    def __init__(self):
        self.root = Node(0)
    def insert(self, codeword, symbol):
        # print(symbol)
        node = self.root
        for word in codeword:
            if word == 0:
                if node.left == None:
                    # print('a')
                    node.left = Node(0)
                    node = node.left
                else:
                    node = node.left
                    # node.val = symbol
            elif word == 1:
                if node.right == None:
                    # print('b')
                    node.right = Node(0)
                    node = node.right
                else:
                    node = node.right
                    # node.val = symbol
        node.val = symbol
    def decode(self, encodeData, datalen):
        dataAsBit = ''.join(format(ord(byte), '08b') for byte in encodeData)
        node = self.root
        result = ''
        for index in range(0,datalen):
            if dataAsBit[index] == '0':
                node = node.left
            elif dataAsBit[index] == '1':
                node = node.right
            if node.val != 0:
                    result += node.val
                    node = self.root
        # print(result)
        return result

    # def pr(self):
    #     print(self.root.right.right.val)

# codebook = {
#     'x1' : [0],
#     'x2' : [1,0,0],
#     'x3' : [1,0,1],
#     'x4' : [1, 1]
# }

# codeTree = PrefixCodeTree()
# for symbol in codebook:
#     codeTree.insert(codebook[symbol], symbol)
# encode = ['1','1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '0', '0', '1', '0', '0']
# data = b'\xd2\x9f\x20'

# codeTree.decode(data, 21)
