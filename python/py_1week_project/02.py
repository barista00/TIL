f = open('PJT-01/data/fruits.txt', 'r')
text = f.read()
list = text.splitlines()
f.close()

print(len(list)) # 394