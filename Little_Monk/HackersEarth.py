class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
s=Stack()
p=input()
array = [int(x) for x in input().split()]
count1=0
count=0
for i in array:
    if i>0:
        if count1>0 and s.size()>0:
            count1=0
        s.push(i)
    elif s.size()>0:
        topvalue=s.pop()
        if topvalue+i==0:
            count1=count1+2
        else:
            count1=0
            s=[]
        if count1>count:
            count=count1
print(count)