# create a list with 5 integer 
# l1=[1,2,3,4,5]
# for i in l1:
#     print(i,end=" ")

# create a list with 5 string 
# l2=["a","e","i","o","u"]
# for i in l2:
#     print(i,end=",")

# create a list with string,integer,float... 
# l3=[1,2.4,-3,"4","Abhay"]
# for i in l3:
#     print(i,end=" ")

# create a l4 with range function from 1-5
# l4=list(range(1,6));
# for i in l4:
#     print(i,end=",")


# create a l5 with element 10,20,30,40,50,60  and acess  a 30 by using  index
# l5=[10,20,30,40,50,60]
# print(f"By using +ive indexing {l5[2]}")
# print(f"By using -ive indexing {l5[-4]}")
# print(f"After: {l5[3]}")
# l5[3]=100
# print(f"Before: {l5[3]}")

# create a list from 10,20,30,40,50,60,70 and print the number 20,30,40 using slice
l6=list(range(10,80,10))
# print(l6[1:4])   # by +ive indexing
# print(l6[-6:-3])  # by -ive indexing
# print(l6[1:6:2])   # by +ive indexing
# print(l6[-6:-1:2])  # by -ive indexing

leng=len(l6)
maxm=-1
minm=1000000000
sum=0
for i in l6:
    maxm=max(maxm,i)
    minm=min(minm,i)
    sum+=i;
l6=list(range(10,80,10))
# print(l6[1:4])   # by +ive indexing
# print(l6[-6:-3])  # by -ive indexing
# print(l6[1:6:2])   # by +ive indexing
# print(l6[-6:-1:2])  # by -ive indexing

leng = len(l6)
maxm = -1
minm = 1000000000
total = 0

for x in l6:   # iterate values directly
    maxm = max(maxm, x)
    minm = min(minm, x)
    total += x

print(f"length: {leng}, max: {maxm}, min: {minm}, sum: {total}")
print(max(l6))
print(min(l6))
print(sum(l6))