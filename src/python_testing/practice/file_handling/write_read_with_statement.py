file_name = 'notes.txt'
with open(file_name, "w") as f:
    f.write("Python learning day 10")

with open(file_name, "r") as f:
    content = f.read()
    print(content)
