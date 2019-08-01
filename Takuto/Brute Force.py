alphabet="abcdefghijklmnopqrstuvwxyz" \
def decode(Hello):
for key in range(len(alphabet)):
newAlphabet=alphabet[key:] + alphabet[:key]
attemp=""
for i in range(len(Hello)):
    index=alphabet.find(message[i])