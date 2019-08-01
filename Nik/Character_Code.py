numbers = [
    0x69, 0x44, 0x54, 0x65, 0x63, 0x68
]
text = ""
for i in numbers:
    text += chr(i)
print(text)
for c in text:
    N = ord(c)
    # print(N)
    print(hex(N))

## Note to editor: Add the below code for the 2nd code snippet
csi = "\x1b["
color = "34m"
colored_text = csi + color + text
print(colored_text)