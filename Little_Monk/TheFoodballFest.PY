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
S=Stack()
T = int(input())
for _t in range(T):
    stop, ini = map(int, input().split())
    S.push(ini)
    for _ in range(stop):
        ch = input().split()
        if ch[0] == 'P':
            S.push(int(ch[1]))
        else:
            if S.size()>0:
                b=S.pop()
                bb=S.pop()
                S.push(b)
                S.push(bb)         
print("Player", S.peek())