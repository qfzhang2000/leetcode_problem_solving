class TrieNode:
    def __init__(self):
        self.leaf = False
        self.children = {}


class Trie(object):
    '''This problem is template for Trie'''
    '''When we do initilaize, do not convey the children '''
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        a = self.root
        for i in word:
            if(i in a.children):
                a = a.children[i]
            else:
                a.children[i] = TrieNode()
                a =  a.children[i]
        a.leaf = True
        
        return None

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        a = self.root
        for i in word:
            if(i in a.children):
                a = a.children[i]
            else:
                return False 

        if(a.leaf):
            return True
        else:
            return False



    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        a = self.root

        for i in prefix:
            if(i in a.children):
                a = a.children[i]
            else:
                return False 

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
