"""
此题是利用字典与双链表进行插入和删除操作，同时也可以利用一个单链表，对应的 key 记录的是 value 前面的元素
"""

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.mapping = {}

        # concat double linked list
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        cur = self.mapping.get(key)
        if not cur:
            # not exists in the cache
            return -1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.move2tail(cur)
        return cur.value

    def put(self, key: int, value: int) -> None:
        # get 这个方法会把key挪到最末端，因此，不需要再调用 move_to_tail
        if self.get(key) != -1:
            # update value
            self.mapping[key].value=value
            return
        if len(self.mapping) == self.capacity:
            del self.mapping[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        insert = Node(key, value)
        self.mapping[key]=insert
        self.move2tail(insert)

    def move2tail(self, node: Node) -> None:
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        node.next = self.tail



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)