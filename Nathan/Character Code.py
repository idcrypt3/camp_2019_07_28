numbers = [0x69, 0x44, 0x54, 0x65, 0x63, 0x68]
text = ""
for i in numbers:
    text += chr(i)
print(text)
csi = "\x1b["
color = "37m"
colored_text = csi + color + text
print(colored_text)
