from .entry import Entry

class Bucket:

    entries = None

    def __init__(self):
        pass

    def add(self, key, value):
        entry_to_add = Entry(key, value)

        current_entry = self.entries
        previous_entry = current_entry
        while current_entry is not None and current_entry.key != key:
            previous_entry = current_entry
            current_entry = current_entry.next
        
        # Bucket is empty, it has no entries yet
        if previous_entry is None:
            self.entries = entry_to_add
        # There's already an entry with that key, so overwrite the value
        elif current_entry is not None and current_entry.key == key:
            current_entry.value = value
        # The key isn't found, so add a new entry to the end of the bucket
        else:
            previous_entry.next = entry_to_add

    def find(self, key):
        
        current_entry = self.entries
        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next
        
        if current_entry is not None:
            return current_entry.value
        
        return None

    def __str__(self):
        string = ""
        current_entry = self.entries
        while current_entry is not None:
            string += str(current_entry)
            string += "\n"
            current_entry = current_entry.next
        return string