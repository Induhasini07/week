d={}
size=5
for i in range (5):
    key=int(input('enter the key: '))
    value=input('enter the value: ')
    d[key]=value
    d[value]=key
print(d)
