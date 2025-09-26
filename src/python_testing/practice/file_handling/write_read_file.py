file_name='notes.txt'
f = open(file_name, "w")
f.write("Python learning day 10")
f.close()

f = open(file_name, "r")
content = f.read()
print(content)
f.close()