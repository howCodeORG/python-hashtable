import random
from hmap import Map

def add_random(map):
    # Fill the hash table with dummy data
    for i in range(100):
        alphabet = [ chr((x + 97) % (97+26)) for x in range(26) ]
        key = ''.join(random.choice(alphabet) for _ in range(5))
        map.put(key, f"value {key}")

print("--- Commands ---")
print("new - creates a new map")
print("put <key> <value> - inserts a value into the map")
print("put <key> - retrieves a value from the map")
print("print - prints all the map's buckets")
print("resize <size> - increase the map's size to <size>")
print("add_random - add some random data to the map")
print("----------------")

map = Map()
while True:
    command = input("> ")
    parts = command.split(" ")
    if parts[0] == "new":
        map = Map()
        print("Created a new map.")
    elif parts[0] == "put":
        map.put(parts[1], parts[2])
        print(f"Mapped the key '{parts[1]}' to the value '{parts[2]}'")
    elif parts[0] == "get":
        print(map.get(parts[1]))
    elif parts[0] == "add_random":
        add_random(map)
        print("Added 100 random values to the map.")
    elif parts[0] == "print":
        print(map)
    elif parts[0] == "resize":
        map.resize(int(parts[1]))
        print(f"Resized map to {parts[1]} buckets.")
    else:
        print(f"Invalid command: {parts[0]}, expected new, put, get, resize, add_random or print")
