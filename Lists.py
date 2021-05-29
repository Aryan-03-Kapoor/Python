#Perform all sorts of functions on the list and get an easy wasy to learn lists.
#insert i e: Insert integer e at position i.
#print: Print the list.
#remove e: Delete the first occurrence of integer e.
#append e: Insert integer e at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

#Code strating from here 
N = int(input())
L=[]
for i in range(0,N):
    c=input().split()
    if c[0]== "insert":
        L.insert(int(c[1]),int(c[2]))
    elif c[0]== "append":
         L.append(int(c[1]))
    elif c[0]== "pop":
            L.pop()
    elif c[0]== "print":
        print(L)
    elif c[0]== "remove":
        L.remove(int(c[1]))
    elif c[0]== "sort":
        L.sort()
    else:
        L.reverse()