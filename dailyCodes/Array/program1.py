import array as arr
jerNo = arr.array('i',[45,77,18,96,1])
#print(jerNo)
arr = jerNo[::-1]
for i in range(0,len(arr)):
        print(arr[i],end=" ")

for i in jerNo:
    print(i)
