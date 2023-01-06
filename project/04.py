f = open('PJT-01/data/fruits.txt', 'r')
text = f.read()
list = text.splitlines()
f.close()

dict = {}

for i in list:
    if i not in dict:
        dict[i] =  1
    else :
        dict[i] = dict[i] + 1

for a, b in dict.items():
    print(a, b)