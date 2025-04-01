"""
Hash table implementation.
Hash tables support insert/delete/search operations.
They primarily shine with searching. Avg O(1), worst case O(n)
Space requirement O(K) where K = # keys
Hash function maps keys to location in the table that holds data.
Goal: use a hash function that maximizes randomness / distribution and minimizes collisions.
You can handle collisions with chaining (linkedlists)
"""

from src.sample import words
import logging
import random

logger = logging.getLogger(__name__)


class HashTable:
    """custom implementation of a dictionary that leverages Python's built-in hash function"""

    def __init__(self, size=10, load_factor=0.75):
        logger.info({"HashTable.__init__": {"size": size, "load_factor": 0.75}})
        self.size = size
        self.table = [[] for _ in range(size)]  # Array of empty lists for chaining
        self.count = 0
        self.load_factor = load_factor

    def _resize(self, resize_multiple=1.5):
        """Resize hash table -- increase by 1.5 times current size"""
        logger.info({"action": "HashTable.resize", "resize_multiple": resize_multiple})
        new_size = int(self.size * resize_multiple)
        new_table = [[] for _ in range(new_size)]
        # have a new table. need to map current table to new table.
        for bucket in self.table:
            for key, value in bucket:
                # update the index of this key using new size
                new_index = hash(key) % new_size
                new_table[new_index].append([key, value])
        self.size = new_size
        self.table = new_table
        logger.info({"action": "HashTable.resize", "status": "complete"})

    def _hash(self, key):
        """
        Use python's built-in hash function with division / modulo operator
        to map input key to location in table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """insert a value into the table at the key index"""
        # check storage to determine if resize is needed
        logger.info({"action": "HashTable.insert", "key": key, "value": value})
        if self.count / self.size >= self.load_factor:
            logger.info(
                {
                    "action": "HashTable.insert",
                    "msg": (
                        f"storage use (count / size = {self.count} / {self.size}) "
                        f"{int(round(self.count / self.size, 2) * 100)}% exceeds "
                        f"load factor {int(self.load_factor * 100)}%",
                    ),
                }
            )
            self._resize()
        index = self._hash(key)
        data_at_index = self.table[index]
        for pair in data_at_index:
            if pair[0] == key:
                # overwrite key with new value. e.g., mydict['existing'] = 'new val'
                pair[1] = value
                return
        # key not present so add new key, value pair
        self.table[index].append([key, value])
        self.count += 1

    def get(self, key):
        """Retrieve a value by key - return None if key not present"""
        logger.info({"action": "HashTable.get", "key": key})
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """Delete an item by key if present and decrement count if item deleted"""
        logger.info({"action": "HashTable.delete", "key": key})
        index = self._hash(key)
        original_length = len(self.table[index])
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]
        # only decrement count if item was deleted
        if original_length > len(self.table[index]):
            self.count -= 1


flattened_words_list = [w for wlist in words for w in wlist]


def test_hashtable():
    ht = HashTable(size=8)
    for i in range(25):
        ht.insert(random.choice(flattened_words_list), i * i)


if __name__ == "__main__":
    test_hashtable()
