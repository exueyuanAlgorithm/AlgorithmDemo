class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current_dict = self.trie
        for position, item in enumerate(word):
            next_dict = current_dict.get(item, {})
            current_dict[item] = next_dict
            if position == len(word) - 1:
                next_dict["is_final"] = True
            current_dict = next_dict
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_dict = self.trie
        for position, item in enumerate(word):
            if item not in current_dict:
                return False
            next_dict = current_dict[item]
            if position == len(word) - 1:
                if next_dict.get("is_final", False):
                    return True
                else:
                    return False
            current_dict = next_dict

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_dict = self.trie
        for position, item in enumerate(prefix):
            if item not in current_dict:
                return False
            current_dict = current_dict[item]
        return True

trie = Trie()
trie.insert("apple")
trie.insert("appn")
print(trie.search("appl"))
print(trie.search("apple"))

# print(trie.search("app"))
# print(trie.startsWith("app"))
# print(trie.startsWith("bab"))
# print(trie.search("baba"))

# a = ["Trie", "insert", "search", "startsWith"]
# b = [[], ["app"], ["word"], ["lalla"]]
# daan_list = []
# for position, (item1, item2) in enumerate(zip(a, b)):
#     if item1 == "Trie":
#         daan_list.append(None)
#     if item1 == "insert":
#         trie.insert(item2[0])
#         daan_list.append(None)
#     elif item1 == "search":
#         daan = trie.search(item2[0])
#         daan_list.append(daan)
#     elif item1 == "startsWith":
#         daan = trie.startsWith(item2[0])
#         daan_list.append(daan)
# print(daan_list)
