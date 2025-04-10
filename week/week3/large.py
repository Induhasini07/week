def largest(elements):
    ele=0
    for i in elements:
        ele=max(ele,i)
    return ele
    
    
def printelements(elements):
    for i in elements:
        print(i,end=" ")
        
        
def smallest(elements,lrgeNum):
    ele=largeNum
    for i in elements:
        ele=min(ele,i)
    return ele
    
    
elements=[]
limit=int(input("Enter the limit :"))
for i in range(limit):
    ele=int(input("Enter :"))
    elements.append(ele)
    
    largeNum=largest(elements)
    printelements(elements)
    smallNum=smallest(elements,largeNum)
    print('largest =',largeNum)
    print('smallest= ',smallNum)
