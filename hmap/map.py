from .bucket import Bucket

class Map:

    size = None
    buckets = None
    used = None

    def __init__(self, size = 8):
        self.size = size
        self.buckets = [ Bucket() for b in range(size) ]
        self.used = 0
    
    def put(self, key, value):

        # If map is full then make it twice as big
        if self.used == self.size:
            self.resize(self.size * 2)

        hash = self.__hash(key)

        bucketId = hash % self.size
        bucket = self.buckets[bucketId]

        # If the entry isn't found then it'll be added, 
        # if is found then it'll just be replaced
        if not self.get(key):
            self.used += 1

        bucket.add(key, value)

    def get(self, key):
        hash = self.__hash(key)

        bucketId = hash % self.size
        bucket = self.buckets[bucketId]

        return bucket.find(key)

    def resize(self, size):

        temp_map = Map(size)

        for bucket in self.buckets:
            current_entry = bucket.entries
            while current_entry is not None:
                # Add each entry to the new bigger map
                temp_map.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next
                
        # Update the size and replace the buckets in the original map
        self.size = size
        self.buckets = temp_map.buckets

    def __hash(self, key):

        hash = 7
        for char in key:
            hash = hash * 31 + ord(char)
        return hash

    def __str__(self):
        string = ""
        string += f"map (used: {self.used}, size: {self.size})\n"
        for i in range(len(self.buckets)):
            string += f"bucket({i})\n"
            string += str(self.buckets[i])
        return string