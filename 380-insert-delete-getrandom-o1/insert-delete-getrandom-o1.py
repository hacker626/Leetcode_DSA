import random
class RandomizedSet(object):

    def __init__(self):
        self.data = {}


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if(val in self.data):
            return False
        self.data[val] = 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if(val not in self.data):
            return 0
        del self.data[val]
        return 1

    def getRandom(self):
        """
        :rtype: int
        """
        temp = random.choice(list(self.data.keys()))
        return temp
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()