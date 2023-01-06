f = open('PJT-01/data/fruits.txt', 'r')
text = f.read()
list = text.splitlines()
f.close()

a = 0
for i in list:
    if 'berry' in i:
        a += 1
        print(i)
print(a)
# print('berry' in 'strawberry') # True
