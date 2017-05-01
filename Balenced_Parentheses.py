p=input()
array = [int(x) for x in raw_input().split()]
len_array=len(array)
count=0
count1=0
buf=[]
buf2=[]
len_buf=len(buf)
j=1
k=0
for i in array:
    if i>0:
        if count1>0 and len(buf)>0:
            count1=0
        buf.append(i)
    elif len(buf)>0:
        topvalue=buf.pop()
        if topvalue+i==0:
            count1=count1+2
        else:
            count1=0
            buf=[]
        if count1>count:
            count=count1
print count
