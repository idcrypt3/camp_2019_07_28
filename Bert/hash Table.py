phone_book = [
    ("Alice", 4082553555),
    ("", 00000000),
    ("Diane", 9830978345),
    ("Bob", 6503879023),
    ("", 00000000),
    ("Eve", 7642398541),
    ("Charlie", 5052358753)
]
max_size = 19
while len(phone_book) < max_size - 1:
    phone_book.append(("", 00000000))
phone_book.append(("Steven", 1420573857))
search_name = input("Lookup which number?")
search_count = 0
sorted_book = sorted(phone_book, key = lambda phone_book: phone_book[0])
while sorted_book[0][0] == "":
    del(sorted_book[0])
search_index = int(len(sorted_book)/2)
search_max = len(sorted_book) - 1
search_min = 0
search_count = 0
for i in range(len(sorted_book)):
    search_count += 1
    if search_name == sorted_book[search_index][0]:
        print(sorted_book[search_index][1])
        print(search_count)
        break
    elif search_name < sorted_book[search_index][0]:
        search_mac = search_index
        search_index -= int((search_index-search_min)/2 + 0.5)
    elif search_name > sorted_book[search_index][0]:
        search_min = search_index
        search_index += int((search_max-search_index)/2 + 0.5)
    if search_count == len(sorted_book):
        print("Name not Found")
for i in range(len(phone_book)):
    search_count +=1
    if phone_book[i][0] == search_name:
        print("Unsorted book search:")
        print(phone_book[i][1])
        print(search_count)
        break
    if search_count == max_size:
        print("Name not Found")

#Hash Function
phone_hash = []
hashed_book = [("", 0000000000)for i in range(max_size)]
for i in range(len(phone_book)):
    name = phone_book[i][0]
    digest = new_hash(name)
    if digest == -1:
        continue
        phone_hash.append(digest)
        new_index = digest
        hashed_book
        while hashed_book[new_index]!= ("", 0000000000):
            new_index = (new_index + 1)%max_size
            hashed_book[new_index] = phone_book[i]
hash_index = new_hash(search_name)
search_count = 0
for i in range(len(hashed_book)):
    searched_count += 1
    if heashed_book[hash_index][0] == searched_name:
        print(hashed_book[hash_index][1])
        print(search_count)
        break

