file_name = input('Enter the filename to open')

try:
    with open(file_name,'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print('Done!')