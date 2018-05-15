class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.idx = 0
        self.size = 0
        self.q = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.get(key):
            self.q.append(self.q.pop(self.q.index(key)))
            self.idx += 1
            return self.cache.get(key).get('val')
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.q:
            if self.q[-1] != key:
                if self.size == self.capacity:
                    if self.cache.get(key) is None:
                        del (self.cache[self.q.pop(0)])
                else:
                    if self.cache.get(key) is None:
                        self.size += 1
        else:
            if self.cache.get(key) is None:
                self.size += 1

        if self.cache.get(key):
            self.q.append(self.q.pop(self.q.index(key)))
        else:
            self.q.append(key)
        self.cache[key] = {'val': value}
        self.idx += 1


def main():
    # # case 1
    # lru = LRUCache(2)
    # lru.put(1, 1)
    # lru.put(2, 2)
    # print(lru.get(1))   # 1
    # lru.put(3, 3)
    # print(lru.get(2))   # -1
    # lru.put(4, 4)
    # print(lru.get(1))   # -1
    # print(lru.get(3))   # 31
    # print(lru.get(4))   # 4
    # print()
    #
    # # case 2
    # lru = LRUCache(2)
    # lru.put(2, 1)
    # lru.put(2, 2)
    # print(lru.get(2))   # 2
    # lru.put(1, 1)
    # lru.put(4, 1)
    # print(lru.get(2))   # -1
    # print()
    #
    # # case 3
    # lru = LRUCache(2)
    # print(lru.get(2))   # -1
    # lru.put(2, 6)
    # print(lru.get(1))   # -1
    # lru.put(1, 5)
    # lru.put(1, 2)
    # print(lru.get(1))   # 2
    # print(lru.get(2))   # 6
    
    # case 4
    lru = LRUCache(10)
    lru.put(10, 13)
    lru.put(3, 17)
    lru.put(6, 11)
    lru.put(10, 5)
    lru.put(9, 10)
    print(lru.get(13))  # -1
    lru.put(2, 19)
    print(lru.get(2))   # 19
    print(lru.get(3))   # 17
    lru.put(5, 25)
    print(lru.get(8))   # -1
    lru.put(9, 22)
    lru.put(5, 5)
    lru.put(1, 30)
    print(lru.get(11))   # -1
    lru.put(9, 12)
    print(lru.get(7))   # -1
    print(lru.get(5))   # 5
    print(lru.get(8))   # -1
    print(lru.get(9))   # 12
    lru.put(4, 30)
    lru.put(9, 3)
    print(lru.get(9))   # 3
    print(lru.get(10))  # 5
    print(lru.get(10))  # 5
    lru.put(6, 14)
    lru.put(3, 1)
    print(lru.get(3))   # 1
    lru.put(10, 11)
    print(lru.get(8))   # -1
    lru.put(2, 14)
    print(lru.get(1))   # 30
    print(lru.get(5))   # 5
    print(lru.get(4))   # 30
    lru.put(11, 4)
    lru.put(12, 24)
    lru.put(5, 18)
    print(lru.get(13))  # -1
    lru.put(7, 23)
    print(lru.get(8))   # -1
    print(lru.get(12))  # 24
    lru.put(3, 27)
    lru.put(2, 12)
    print(lru.get(5))   # 18
    lru.put(2, 9)
    lru.put(13, 4)
    lru.put(8, 18)
    lru.put(1, 7)
    print(lru.get(6))   # -1
    lru.put(9, 29)
    lru.put(8, 21)
    print(lru.get(5))   # 18
    lru.put(6, 30)
    lru.put(1, 12)
    print(lru.get(10))  # -1
    lru.put(4, 15)
    lru.put(7, 22)
    lru.put(11, 26)
    lru.put(8, 17)
    lru.put(9, 29)
    print(lru.get(5))   # 18
    lru.put(3, 4)
    lru.put(11, 30)
    print(lru.get(12))  # -1
    lru.put(4, 29)
    print(lru.get(3))   # 4
    print(lru.get(9))   # 29
    print(lru.get(6))   # 30
    lru.put(3, 4)
    print(lru.get(1))   # 12
    print(lru.get(10))  # -1
    lru.put(3, 29)
    lru.put(10, 28)
    lru.put(1, 20)
    lru.put(11, 13)
    print(lru.get(3))   # 29
    lru.put(3, 12)
    lru.put(3, 8)
    lru.put(10, 9)
    lru.put(3, 26)
    print(lru.get(8))   # 17
    print(lru.get(7))   # 22
    print(lru.get(5))   # 18
    lru.put(13, 17)
    lru.put(2, 27)
    lru.put(11, 15)
    print(lru.get(12))  # -1
    lru.put(9, 19)
    lru.put(2, 15)
    lru.put(3, 16)
    print(lru.get(1))   # 20
    lru.put(12, 17)
    lru.put(9, 1)
    lru.put(6, 19)
    print(lru.get(4))   # -1
    print(lru.get(5))   # 18
    print(lru.get(5))   # 18
    lru.put(8, 1)
    lru.put(11, 7)
    lru.put(5, 2)
    lru.put(9, 28)
    print(lru.get(1)) # 20
    lru.put(2, 2)
    lru.put(7, 4)
    lru.put(4, 22)
    lru.put(7, 24)
    lru.put(9, 26)
    lru.put(13, 28)
    lru.put(11, 26)
 

# expected
# [null,null,null,1,null,-1,null,-1,3,4]
# [null,null,null,2,null,null,-1]
# [null,-1,null,-1,null,null,2,6]
# [null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]

# LC input
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2]
# [1,1]
# [2,2]
# [1]
# [3,3]
# [2]
# [4,4]
# [1]
# [3]
# [4]]
# ["LRUCache","put","put","get","put","put","get"]
# [[2]
# [2,1]
# [2,2]
# [2]
# [1,1]
# [4,1]
# [2]]
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2]
# [2]
# [2,6]
# [1]
# [1,5]
# [1,2]
# [1]
# [2]]
# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]



if __name__ == '__main__':
    main()
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)