def createlist(l,n): 
    for i in range(n):
        temp=int(input("enter value"))
        l.append(temp)
    return l
def evensum(l):
    evensum=0
    for i in range(len(l)):
        if (i%2==0): 
           evensum+=l[i]
    return evensum 
    
def oddsum(l):
    oddsum=0
    for i in range (len(l)):
        if(i%2!=0):
            oddsum+=l[i]
    return oddsum
    
    
    
l1=[]
l2=[]
l3=[]
n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
n3=int(input("Enter n3"))
l1=createlist(l1,n1)
print(l1)
l2=createlist(l2,n2)
print(l2)
l3=createlist(l3,n3)
print(l3)

evensum1=evensum(l1)
print(evensum1)
evensum2=evensum(l2)
print(evensum2)
evensum3=evensum(l3)
print(evensum3)

oddsum1=oddsum(l1)
print(oddsum1)
oddsum2=oddsum(l2)
print(oddsum2)
oddsum3=oddsum(l3)
print(oddsum3)
Add=(evensum1+evensum2+evensum3)*(oddsum1+oddsum2+oddsum3)
print(Add)
